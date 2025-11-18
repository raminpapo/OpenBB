# Documentation: repo_book_gen.py

## File Metadata
- **Path**: `repo_book_gen.py`
- **Size**: 20,536 characters, 616 lines
- **Words**: 1,688
- **Extension**: .py
- **Classification**: Text file

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
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import re

class RepoBookGenerator:
    def __init__(self, repo_root, output_dir="docs"):
        self.repo_root = Path(repo_root).resolve()
        self.output_dir = self.repo_root / output_dir
        self.output_dir.mkdir(exist_ok=True)

        self.manifest = {
            "generator_version": "1.0.0",
            "repo_name": "OpenBB",
            "repo_source": str(self.repo_root),
            "repo_fingerprint": "",
            "commit_sha": "",
            "scan_timestamp": datetime.utcnow().isoformat(),
            "files_scanned": 0,
            "docs_created": 0,
            "bytes_written": 0,
            "file_map": {},
            "checksums": {}
        }

        self.progress = {
            "files_processed": 0,
            "last_file": "",
            "errors": []
        }

        # Classification
        self.text_extensions = {
            '.py', '.js', '.ts', '.tsx', '.jsx', '.java', '.c', '.cpp', '.h', '.hpp',
            '.md', '.txt', '.json', '.yaml', '.yml', '.toml', '.ini', '.cfg', '.conf',
            '.xml', '.html', '.css', '.scss', '.sass', '.sh', '.bash', '.zsh',
            '.rs', '.go', '.rb', '.php', '.swift', '.kt', '.scala', '.r', '.sql',
            '.dockerfile', '.env', '.gitignore', '.editorconfig', '.lock'
        }

        self.binary_extensions = {
            '.png', '.jpg', '.jpeg', '.gif', '.ico', '.svg', '.pdf', '.zip', '.tar',
            '.gz', '.bz2', '.xz', '.pyc', '.pyo', '.so', '.dll', '.exe', '.bin',
            '.woff', '.woff2', '.ttf', '.eot', '.mp4', '.mp3', '.wav', '.avi'
        }

        self.keywords_global = defaultdict(list)

    def get_commit_sha(self):
        """Get current git commit SHA."""
        try:
            import subprocess
            result = subprocess.run(
                ['git', 'rev-parse', 'HEAD'],
                cwd=self.repo_root,
                capture_output=True,
                text=True
            )
            return result.stdout.strip()
        except:
            return "unknown"

    def compute_fingerprint(self, file_list):
        """Compute repository fingerprint from file list."""
        h = hashlib.sha256()
        for f in sorted(file_list):
            h.update(f.encode('utf-8'))
        return h.hexdigest()[:16]

    def classify_file(self, file_path):
        """Classify file as text, binary, or large."""
        path = Path(file_path)

        if not path.exists():
            return "missing"

        size = path.stat().st_size
        ext = path.suffix.lower()

        # Check size first
        if size > 100 * 1024 * 1024:  # 100MB
            return "very_large"

        # Check extension
        if ext in self.binary_extensions:
            return "binary"

        if ext in self.text_extensions or not ext:
            # Try to read as text
            try:
                with open(path, 'r', encoding='utf-8', errors='strict') as f:
                    f.read(1024)
                return "text"
            except:
                return "binary"

        # Use mimetype
        mime, _ = mimetypes.guess_type(str(path))
        if mime and mime.startswith('text'):
            return "text"

        return "binary"

    def scan_repository(self):
        """Scan all files and build file map."""
        print("Scanning repository...")

        exclude_dirs = {'.git', 'docs', '.venv', 'node_modules', '__pycache__', '.pytest_cache'}

        all_files = []
        for root, dirs, files in os.walk(self.repo_root):
            # Filter directories
            dirs[:] = [d for d in dirs if d not in exclude_dirs]

            for file in files:
                full_path = Path(root) / file
                rel_path = full_path.relative_to(self.repo_root)
                all_files.append(str(rel_path))

        # Classify files
        for rel_path in sorted(all_files):
            full_path = self.repo_root / rel_path
            classification = self.classify_file(full_path)

            self.manifest['file_map'][rel_path] = {
                'classification': classification,
                'size': full_path.stat().st_size if full_path.exists() else 0,
                'extension': full_path.suffix
            }

        self.manifest['files_scanned'] = len(all_files)
        self.manifest['repo_fingerprint'] = self.compute_fingerprint(all_files)
        self.manifest['commit_sha'] = self.get_commit_sha()

        print(f"Scanned {len(all_files)} files")
        return all_files

    def extract_keywords(self, content, file_path):
        """Extract keywords from file content."""
        keywords = set()

        # Python identifiers
        if file_path.endswith('.py'):
            # Classes
            keywords.update(re.findall(r'class\s+(\w+)', content))
            # Functions
            keywords.update(re.findall(r'def\s+(\w+)', content))
            # Imports
            keywords.update(re.findall(r'(?:from|import)\s+([\w.]+)', content))

        # JavaScript/TypeScript
        elif file_path.endswith(('.js', '.ts', '.tsx', '.jsx')):
            keywords.update(re.findall(r'(?:class|function|const|let|var)\s+(\w+)', content))
            keywords.update(re.findall(r'export\s+(?:default\s+)?(?:class|function)?\s*(\w+)', content))

        # General: camelCase and snake_case identifiers
        keywords.update(re.findall(r'\b[a-z_][a-z0-9_]{2,}\b', content.lower()))

        return sorted(list(keywords))[:1000]  # Limit to 1000 keywords per file

    def generate_file_docs(self, rel_path):
        """Generate documentation for a single file."""
        full_path = self.repo_root / rel_path
        classification = self.manifest['file_map'][rel_path]['classification']

        # Create output directory structure
        output_path = self.output_dir / rel_path.replace(os.sep, '/')
        output_path.parent.mkdir(parents=True, exist_ok=True)

        doc_file = output_path.parent / f"{output_path.name}_docs.md"
        kw_file = output_path.parent / f"{output_path.name}_kw.md"

        if classification == "binary":
            # Binary file documentation
            content = f"""# Binary File: {rel_path}

**File Type**: Binary
**Size**: {self.manifest['file_map'][rel_path]['size']:,} bytes
**Extension**: {Path(rel_path).suffix}

This is a binary file and cannot be displayed as text.

## Suggested Handling
- Use appropriate binary viewers or tools for this file type
- File location: `{rel_path}`
"""
            doc_file.write_text(content, encoding='utf-8')
            self.manifest['docs_created'] += 1
            return

        elif classification == "very_large":
            # Very large file
            content = f"""# Large File: {rel_path}

**File Type**: Very Large File (>100MB)
**Size**: {self.manifest['file_map'][rel_path]['size']:,} bytes

This file is very large and requires special handling.

## File Information
- Location: `{rel_path}`
- Size: {self.manifest['file_map'][rel_path]['size'] / (1024*1024):.2f} MB
"""
            doc_file.write_text(content, encoding='utf-8')
            self.manifest['docs_created'] += 1
            return

        # Text file - full documentation
        try:
            with open(full_path, 'r', encoding='utf-8', errors='replace') as f:
                file_content = f.read()
        except Exception as e:
            self.progress['errors'].append(f"Error reading {rel_path}: {str(e)}")
            return

        # Generate docs.md
        lines = file_content.split('\n')
        line_count = len(lines)
        char_count = len(file_content)
        word_count = len(file_content.split())

        # Extract structure based on file type
        structure_info = self.analyze_structure(file_content, rel_path)

        # Prepare source content
        if len(file_content) < 500000:
            source_content = file_content
        else:
            source_content = file_content[:500000] + '\n... [truncated]'

        docs_content = f"""# Documentation: {rel_path}

## File Metadata
- **Path**: `{rel_path}`
- **Size**: {char_count:,} characters, {line_count:,} lines
- **Words**: {word_count:,}
- **Extension**: {Path(rel_path).suffix}
- **Classification**: Text file

## Original Source

```{self.get_language_hint(rel_path)}
{source_content}
```

## High-Level Overview

{self.generate_overview(file_content, rel_path)}

## Detailed Structure

{structure_info}

## Key Components

{self.extract_components(file_content, rel_path)}

## Usage & Examples

{self.generate_usage(file_content, rel_path)}

## Related Files

{self.find_related_files(file_content, rel_path)}

## Notes
- Generated: {datetime.utcnow().isoformat()}
- Generator: World's Best Repo Book Generator v1.0.0
"""

        doc_file.write_text(docs_content, encoding='utf-8')
        self.manifest['bytes_written'] += len(docs_content)

        # Generate keywords.md
        keywords = self.extract_keywords(file_content, rel_path)
        kw_content = f"""# Keywords: {rel_path}

## Extracted Keywords ({len(keywords)} total)

"""

        for kw in keywords[:500]:  # Limit to 500 for readability
            kw_content += f"- **{kw}** - Appears in `{rel_path}`\n"
            self.keywords_global[kw].append(rel_path)

        kw_file.write_text(kw_content, encoding='utf-8')
        self.manifest['bytes_written'] += len(kw_content)
        self.manifest['docs_created'] += 2

        self.progress['files_processed'] += 1
        self.progress['last_file'] = rel_path

    def get_language_hint(self, path):
        """Get language hint for syntax highlighting."""
        ext = Path(path).suffix.lower()
        mapping = {
            '.py': 'python',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.tsx': 'tsx',
            '.jsx': 'jsx',
            '.java': 'java',
            '.c': 'c',
            '.cpp': 'cpp',
            '.h': 'c',
            '.hpp': 'cpp',
            '.rs': 'rust',
            '.go': 'go',
            '.rb': 'ruby',
            '.php': 'php',
            '.sh': 'bash',
            '.yaml': 'yaml',
            '.yml': 'yaml',
            '.json': 'json',
            '.toml': 'toml',
            '.xml': 'xml',
            '.html': 'html',
            '.css': 'css',
            '.md': 'markdown'
        }
        return mapping.get(ext, '')

    def generate_overview(self, content, path):
        """Generate high-level overview."""
        lines = content.split('\n')

        # Look for docstrings or comments at top
        overview = []
        in_docstring = False

        for i, line in enumerate(lines[:50]):  # First 50 lines
            stripped = line.strip()

            if path.endswith('.py'):
                if stripped.startswith('"""') or stripped.startswith("'''"):
                    in_docstring = not in_docstring
                    overview.append(stripped.strip('"\' '))
                elif in_docstring:
                    overview.append(stripped)
                elif stripped.startswith('#') and not stripped.startswith('#!'):
                    overview.append(stripped.lstrip('# '))

            elif stripped.startswith('//') or stripped.startswith('/*'):
                overview.append(stripped.lstrip('/ *'))

        if overview:
            return '\n'.join(overview[:20])

        return f"This is a {Path(path).suffix} file containing {len(lines)} lines of code."

    def analyze_structure(self, content, path):
        """Analyze file structure."""
        if path.endswith('.py'):
            classes = re.findall(r'class\s+(\w+)', content)
            functions = re.findall(r'def\s+(\w+)', content)
            imports = re.findall(r'(?:from|import)\s+([\w.]+)', content)

            structure = f"""### Python File Structure

**Classes** ({len(classes)}):
{', '.join(f'`{c}`' for c in classes[:20]) if classes else 'None'}

**Functions** ({len(functions)}):
{', '.join(f'`{f}`' for f in functions[:20]) if functions else 'None'}

**Imports** ({len(imports)}):
{', '.join(f'`{i}`' for i in imports[:20]) if imports else 'None'}
"""
            return structure

        elif path.endswith(('.js', '.ts', '.tsx', '.jsx')):
            classes = re.findall(r'class\s+(\w+)', content)
            functions = re.findall(r'(?:function|const|let|var)\s+(\w+)\s*[=\(]', content)
            imports = re.findall(r'import\s+.*?from\s+[\'"](.+?)[\'"]', content)

            structure = f"""### JavaScript/TypeScript Structure

**Classes**: {len(classes)}
**Functions**: {len(functions)}
**Imports**: {len(imports)}
"""
            return structure

        return "Standard text file."

    def extract_components(self, content, path):
        """Extract key components."""
        components = []

        if path.endswith('.py'):
            # Extract class definitions with docstrings
            class_pattern = r'class\s+(\w+).*?:\s*(?:"""(.*?)"""|\'\'\'(.*?)\'\'\')?'
            for match in re.finditer(class_pattern, content, re.DOTALL):
                class_name = match.group(1)
                doc = match.group(2) or match.group(3) or "No documentation"
                components.append(f"**Class `{class_name}`**: {doc.strip()[:200]}")

        if len(components) > 20:
            components = components[:20]

        return '\n\n'.join(components) if components else "No major components extracted."

    def generate_usage(self, content, path):
        """Generate usage examples."""
        # Look for common patterns
        if path.endswith('.py'):
            if 'if __name__ == "__main__"' in content:
                return "This file can be run as a script. See the `__main__` block for entry point."
            elif 'def main(' in content:
                return "This file contains a `main()` function. It may be executable."

        return "See source code for usage details."

    def find_related_files(self, content, path):
        """Find related files based on imports."""
        related = []

        # Python imports
        imports = re.findall(r'from\s+([\w.]+)\s+import|import\s+([\w.]+)', content)
        for imp in imports[:10]:
            module = imp[0] or imp[1]
            if module:
                related.append(f"- `{module}`")

        return '\n'.join(related) if related else "No direct file references found."

    def save_progress(self):
        """Save progress checkpoint."""
        progress_file = self.output_dir / ".progress.log"
        with open(progress_file, 'w') as f:
            json.dump(self.progress, f, indent=2)

    def save_manifest(self):
        """Save manifest.json."""
        manifest_file = self.output_dir / "manifest.json"
        with open(manifest_file, 'w') as f:
            json.dump(self.manifest, f, indent=2)
        print(f"Manifest saved to {manifest_file}")

    def generate_global_index(self):
        """Generate global index.md."""
        index_content = f"""# OpenBB Repository Documentation

**Generated**: {datetime.utcnow().isoformat()}
**Repository**: OpenBB
**Commit**: {self.manifest['commit_sha']}
**Files Scanned**: {self.manifest['files_scanned']}
**Documentation Files Created**: {self.manifest['docs_created']}

## Navigation

- [Comprehensive Book](comprehensive_book.md) - Complete stitched documentation
- [Global Keywords](keywords.md) - A-Z keyword index
- [Verification Report](verification_report.md) - Validation and checks

## Directory Structure

"""
        # Add directory links
        dirs = set()
        for file_path in self.manifest['file_map'].keys():
            parts = Path(file_path).parts
            if len(parts) > 1:
                dirs.add(parts[0])

        for d in sorted(dirs):
            index_content += f"- [{d}/]({d}/index.md)\n"

        index_file = self.output_dir / "index.md"
        index_file.write_text(index_content, encoding='utf-8')
        print(f"Global index saved to {index_file}")

    def generate_keywords_index(self):
        """Generate global keywords.md."""
        kw_content = f"""# Global Keywords Index

**Total Unique Keywords**: {len(self.keywords_global)}

## A-Z Index

"""

        for kw in sorted(self.keywords_global.keys())[:5000]:  # Limit to 5000
            files = self.keywords_global[kw][:10]  # Max 10 files per keyword
            kw_content += f"### {kw}\n"
            kw_content += f"Found in {len(self.keywords_global[kw])} file(s):\n"
            for f in files:
                kw_content += f"- `{f}`\n"
            kw_content += "\n"

        kw_file = self.output_dir / "keywords.md"
        kw_file.write_text(kw_content, encoding='utf-8')
        print(f"Keywords index saved to {kw_file}")

    def generate_verification_report(self):
        """Generate verification_report.md."""
        report = f"""# Verification Report

**Generated**: {datetime.utcnow().isoformat()}

## Summary

- **Files Scanned**: {self.manifest['files_scanned']}
- **Documentation Files Created**: {self.manifest['docs_created']}
- **Bytes Written**: {self.manifest['bytes_written']:,}
- **Errors**: {len(self.progress['errors'])}

## File Classification

"""

        classifications = defaultdict(int)
        for info in self.manifest['file_map'].values():
            classifications[info['classification']] += 1

        for cls, count in sorted(classifications.items()):
            report += f"- **{cls}**: {count} files\n"

        report += "\n## Errors\n\n"

        if self.progress['errors']:
            for err in self.progress['errors']:
                report += f"- {err}\n"
        else:
            report += "No errors encountered.\n"

        report += "\n## Binary Files\n\n"
        binary_files = [k for k, v in self.manifest['file_map'].items() if v['classification'] == 'binary']
        for bf in binary_files[:100]:
            report += f"- `{bf}`\n"

        report_file = self.output_dir / "verification_report.md"
        report_file.write_text(report, encoding='utf-8')
        print(f"Verification report saved to {report_file}")

    def run(self, max_files=None):
        """Main execution."""
        print("=" * 80)
        print("World's Best Repo Book Generator")
        print("=" * 80)

        # Step 1: Scan
        all_files = self.scan_repository()

        # Step 2: Process text files
        text_files = [
            f for f, info in self.manifest['file_map'].items()
            if info['classification'] == 'text'
        ]

        print(f"\nProcessing {len(text_files)} text files...")

        if max_files:
            text_files = text_files[:max_files]

        for i, rel_path in enumerate(text_files):
            if i % 50 == 0:
                print(f"Progress: {i}/{len(text_files)} files...")
                self.save_progress()

            self.generate_file_docs(rel_path)

        # Step 3: Generate global files
        print("\nGenerating global indexes...")
        self.generate_global_index()
        self.generate_keywords_index()
        self.generate_verification_report()

        # Step 4: Save manifest
        self.save_manifest()
        self.save_progress()

        # Final summary
        summary = {
            "repo_source": str(self.repo_root),
            "repo_fingerprint": self.manifest['repo_fingerprint'],
            "commit_sha": self.manifest['commit_sha'],
            "files_scanned": self.manifest['files_scanned'],
            "docs_created": self.manifest['docs_created'],
            "words_estimated": self.manifest['bytes_written'] // 5,  # Rough estimate
            "bytes_written": self.manifest['bytes_written'],
            "errors": self.progress['errors']
        }

        print("\n" + "=" * 80)
        print("GENERATION COMPLETE")
        print("=" * 80)
        print(json.dumps(summary, indent=2))

        return summary


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate comprehensive repo documentation")
    parser.add_argument('--source', default='.', help='Repository root path')
    parser.add_argument('--out', default='docs', help='Output directory')
    parser.add_argument('--max-files', type=int, help='Maximum files to process (for testing)')

    args = parser.parse_args()

    generator = RepoBookGenerator(args.source, args.out)
    generator.run(max_files=args.max_files)

```

## High-Level Overview


World's Best Repo Book Generator
Generates comprehensive documentation for entire repository.

Classification

## Detailed Structure

### Python File Structure

**Classes** (2):
`RepoBookGenerator`, `definitions`

**Functions** (20):
`__init__`, `get_commit_sha`, `compute_fingerprint`, `classify_file`, `scan_repository`, `extract_keywords`, `generate_file_docs`, `get_language_hint`, `generate_overview`, `analyze_structure`, `extract_components`, `generate_usage`, `main`, `find_related_files`, `save_progress`, `save_manifest`, `generate_global_index`, `generate_keywords_index`, `generate_verification_report`, `run`

**Imports** (16):
`os`, `sys`, `json`, `hashlib`, `mimetypes`, `pathlib`, `Path`, `datetime`, `datetime`, `collections`, `defaultdict`, `re`, `subprocess`, `file`, `file`, `argparse`


## Key Components

**Class `RepoBookGenerator`**: No documentation

**Class `definitions`**: No documentation

## Usage & Examples

This file can be run as a script. See the `__main__` block for entry point.

## Related Files

- `os`
- `sys`
- `json`
- `hashlib`
- `mimetypes`
- `pathlib`
- `datetime`
- `collections`
- `re`
- `subprocess`

## Notes
- Generated: 2025-11-18T07:54:43.862334
- Generator: World's Best Repo Book Generator v1.0.0
