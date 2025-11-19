# File Documentation: repo_book_generator.py

## Metadata
- **Path**: `repo_book_generator.py`
- **Size**: 9,544 bytes
- **Lines**: 293
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
#!/usr/bin/env python3
"""
World's Best Repo Book Generator
Generates comprehensive documentation for entire repository.
"""

import os
import sys
import json
import hashlib
import mimetypes
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set, Tuple
from collections import defaultdict

# Configuration
DOCS_DIR = Path("./docs")
PROGRESS_LOG = DOCS_DIR / ".progress.log"
CHECKPOINT_FILE = DOCS_DIR / ".checkpoint.json"
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB
CHUNK_SIZE = 50 * 1024 * 1024  # 50MB for streaming

# Ignore patterns
IGNORE_PATTERNS = [
    ".git/", "docs/", "node_modules/", "__pycache__/", ".pyc",
    ".egg-info/", "dist/", "build/", ".pytest_cache/", ".mypy_cache/",
    ".tox/", ".coverage", ".DS_Store", "*.so", "*.dylib", "*.dll"
]

# Binary extensions
BINARY_EXTENSIONS = {
    '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico', '.svg',
    '.pdf', '.zip', '.tar', '.gz', '.bz2', '.xz', '.7z',
    '.exe', '.dll', '.so', '.dylib', '.bin', '.dat',
    '.mp3', '.mp4', '.avi', '.mov', '.wav',
    '.ttf', '.woff', '.woff2', '.eot',
    '.pickle', '.pkl', '.npy', '.npz',
    '.parquet', '.arrow', '.feather'
}


class RepoScanner:
    """Scans repository and classifies files."""

    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.files_info = []
        self.stats = {
            'total_files': 0,
            'text_files': 0,
            'binary_files': 0,
            'large_files': 0,
            'ignored_files': 0,
            'total_bytes': 0
        }

    def should_ignore(self, path: str) -> bool:
        """Check if file should be ignored."""
        for pattern in IGNORE_PATTERNS:
            if pattern in path:
                return True
        return False

    def is_binary(self, file_path: Path) -> bool:
        """Determine if file is binary."""
        if file_path.suffix.lower() in BINARY_EXTENSIONS:
            return True

        try:
            with open(file_path, 'rb') as f:
                chunk = f.read(8192)
                if b'\x00' in chunk:
                    return True
        except:
            return True

        return False

    def scan(self) -> List[Dict]:
        """Scan repository and classify all files."""
        print("Scanning repository...")

        for root, dirs, files in os.walk(self.repo_root):
            # Filter out ignored directories
            dirs[:] = [d for d in dirs if not self.should_ignore(os.path.join(root, d))]

            for filename in files:
                file_path = Path(root) / filename
                rel_path = file_path.relative_to(self.repo_root)

                if self.should_ignore(str(rel_path)):
                    self.stats['ignored_files'] += 1
                    continue

                try:
                    file_size = file_path.stat().st_size
                    is_binary = self.is_binary(file_path)
                    is_large = file_size > MAX_FILE_SIZE

                    file_info = {
                        'path': str(rel_path),
                        'abs_path': str(file_path),
                        'size': file_size,
                        'is_binary': is_binary,
                        'is_large': is_large,
                        'extension': file_path.suffix,
                        'category': self._categorize(file_path, is_binary, is_large)
                    }

                    self.files_info.append(file_info)
                    self.stats['total_files'] += 1
                    self.stats['total_bytes'] += file_size

                    if is_binary:
                        self.stats['binary_files'] += 1
                    else:
                        self.stats['text_files'] += 1

                    if is_large:
                        self.stats['large_files'] += 1

                except Exception as e:
                    print(f"Error scanning {rel_path}: {e}")

        print(f"Scan complete: {self.stats['total_files']} files, "
              f"{self.stats['text_files']} text, {self.stats['binary_files']} binary")

        return self.files_info

    def _categorize(self, file_path: Path, is_binary: bool, is_large: bool) -> str:
        """Categorize file type."""
        if is_binary:
            return 'binary'
        if is_large:
            return 'large_text'

        ext = file_path.suffix.lower()
        if ext in {'.py', '.pyx', '.pyi'}:
            return 'python'
        elif ext in {'.js', '.jsx', '.ts', '.tsx'}:
            return 'javascript'
        elif ext in {'.md', '.rst', '.txt'}:
            return 'documentation'
        elif ext in {'.json', '.yaml', '.yml', '.toml', '.ini', '.cfg'}:
            return 'config'
        elif ext in {'.html', '.htm', '.css', '.scss'}:
            return 'web'
        elif ext in {'.sh', '.bash', '.zsh'}:
            return 'shell'
        else:
            return 'text'


class ManifestBuilder:
    """Builds and manages manifest.json."""

    def __init__(self, repo_root: Path, commit_sha: str):
        self.repo_root = repo_root
        self.commit_sha = commit_sha
        self.manifest = {
            'generator_version': '1.0.0',
            'repo_name': repo_root.name,
            'repo_fingerprint': commit_sha,
            'generated_at': datetime.utcnow().isoformat() + 'Z',
            'file_count': 0,
            'docs_count': 0,
            'bytes_written': 0,
            'files': [],
            'checksums': {}
        }

    def add_files(self, files_info: List[Dict]):
        """Add scanned files to manifest."""
        self.manifest['files'] = files_info
        self.manifest['file_count'] = len(files_info)

    def add_checksum(self, doc_path: str, checksum: str):
        """Add checksum for generated doc."""
        self.manifest['checksums'][doc_path] = checksum

    def increment_docs_count(self, count: int = 1):
        """Increment docs count."""
        self.manifest['docs_count'] += count

    def add_bytes_written(self, bytes_count: int):
        """Add to bytes written."""
        self.manifest['bytes_written'] += bytes_count

    def save(self):
        """Save manifest to disk."""
        manifest_path = DOCS_DIR / "manifest.json"
        with open(manifest_path, 'w') as f:
            json.dump(self.manifest, f, indent=2)
        print(f"Manifest saved to {manifest_path}")


def compute_sha256(file_path: Path) -> str:
    """Compute SHA256 checksum of file."""
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            sha256.update(chunk)
    return sha256.hexdigest()


def extract_keywords_from_content(content: str, file_type: str) -> List[str]:
    """Extract keywords from file content."""
    keywords = set()

    # Common patterns
    if file_type == 'python':
        # Classes
        keywords.update(re.findall(r'class\s+(\w+)', content))
        # Functions
        keywords.update(re.findall(r'def\s+(\w+)', content))
        # Imports
        keywords.update(re.findall(r'from\s+[\w.]+\s+import\s+(\w+)', content))
        keywords.update(re.findall(r'import\s+([\w.]+)', content))

    elif file_type in ['javascript', 'typescript']:
        # Functions
        keywords.update(re.findall(r'function\s+(\w+)', content))
        keywords.update(re.findall(r'const\s+(\w+)\s*=', content))
        keywords.update(re.findall(r'let\s+(\w+)\s*=', content))
        # Classes
        keywords.update(re.findall(r'class\s+(\w+)', content))

    # Generic identifiers (CamelCase and snake_case)
    keywords.update(re.findall(r'\b[A-Z][a-zA-Z0-9]+\b', content))
    keywords.update(re.findall(r'\b[a-z_][a-z0-9_]{3,}\b', content))

    # Filter out common words
    common_words = {'the', 'and', 'for', 'with', 'this', 'that', 'from', 'import', 'true', 'false', 'none', 'null'}
    keywords = {k for k in keywords if k.lower() not in common_words and len(k) > 2}

    return sorted(list(keywords))


def main():
    """Main entry point."""
    print("=" * 80)
    print("WORLD'S BEST REPO BOOK GENERATOR")
    print("=" * 80)

    repo_root = Path.cwd()

    # Get commit SHA
    import subprocess
    try:
        commit_sha = subprocess.check_output(['git', 'rev-parse', 'HEAD'],
                                            cwd=repo_root).decode().strip()
    except:
        commit_sha = hashlib.sha256(str(datetime.utcnow()).encode()).hexdigest()

    print(f"Repository: {repo_root.name}")
    print(f"Fingerprint: {commit_sha}")

    # Create docs directory
    DOCS_DIR.mkdir(exist_ok=True)

    # Step 1: Scan
    scanner = RepoScanner(repo_root)
    files_info = scanner.scan()

    # Step 2: Create manifest
    manifest = ManifestBuilder(repo_root, commit_sha)
    manifest.add_files(files_info)
    manifest.save()

    print("\nBootstrap complete!")
    print(f"Files scanned: {scanner.stats['total_files']}")
    print(f"Text files: {scanner.stats['text_files']}")
    print(f"Binary files: {scanner.stats['binary_files']}")
    print(f"Total size: {scanner.stats['total_bytes'] / 1024 / 1024:.2f} MB")

    return {
        'repo_source': str(repo_root),
        'repo_fingerprint': commit_sha,
        'files_scanned': scanner.stats['total_files'],
        'text_files': scanner.stats['text_files'],
        'binary_files': scanner.stats['binary_files']
    }


if __name__ == '__main__':
    result = main()
    print("\n" + "=" * 80)
    print("BOOTSTRAP SUMMARY:")
    print(json.dumps(result, indent=2))
    print("=" * 80)

```



---

## High-Level Overview

This is a **python** file named `repo_book_generator.py`.

**Python Module**

- **Classes** (2): RepoScanner, ManifestBuilder
- **Functions** (14): __init__, should_ignore, is_binary, scan, _categorize, __init__, add_files, add_checksum, increment_docs_count, add_bytes_written ... and 4 more
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`RepoScanner`**
- **`ManifestBuilder`**

#### Functions

- **`__init__(self, repo_root: Path)`**
- **`__init__(self, repo_root: Path, commit_sha: str)`**
- **`add_files(self, files_info: List[Dict])`**
- **`add_checksum(self, doc_path: str, checksum: str)`**
- **`increment_docs_count(self, count: int = 1)`**
- **`add_bytes_written(self, bytes_count: int)`**
- **`save(self)`**
- **`main()`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Dict`
- `Path`
- `collections`
- `datetime`
- `defaultdict`
- `hashlib`
- `json`
- `mimetypes`
- `os`
- `pathlib`
- `re`
- `subprocess`
- `sys`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:15:18.720066Z
**Generator**: World's Best Repo Book Generator v1.0
