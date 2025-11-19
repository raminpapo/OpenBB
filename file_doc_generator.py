#!/usr/bin/env python3
"""
File Documentation Generator
Generates _docs.md and _kw.md for each file in the repository.
"""

import os
import sys
import json
import hashlib
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set
from collections import defaultdict

DOCS_DIR = Path("./docs")
MANIFEST_PATH = DOCS_DIR / "manifest.json"
PROGRESS_LOG = DOCS_DIR / ".progress.log"


class FileDocGenerator:
    """Generates documentation for individual files."""

    def __init__(self):
        self.manifest = self._load_manifest()
        self.processed_files = set()
        self.docs_created = 0
        self.errors = []
        self._load_progress()

    def _load_manifest(self) -> Dict:
        """Load manifest file."""
        with open(MANIFEST_PATH, 'r') as f:
            return json.load(f)

    def _load_progress(self):
        """Load processing progress."""
        if PROGRESS_LOG.exists():
            with open(PROGRESS_LOG, 'r') as f:
                for line in f:
                    self.processed_files.add(line.strip())

    def _save_progress(self, file_path: str):
        """Save processing progress."""
        with open(PROGRESS_LOG, 'a') as f:
            f.write(f"{file_path}\n")

    def process_all(self):
        """Process all files in manifest."""
        files = self.manifest.get('files', [])
        text_files = [f for f in files if not f['is_binary']]

        print(f"Processing {len(text_files)} text files...")

        for idx, file_info in enumerate(text_files, 1):
            file_path = file_info['path']

            if file_path in self.processed_files:
                print(f"[{idx}/{len(text_files)}] Skipping {file_path} (already processed)")
                continue

            try:
                print(f"[{idx}/{len(text_files)}] Processing {file_path}...")
                self._process_file(file_info)
                self._save_progress(file_path)
                self.docs_created += 2  # _docs.md + _kw.md

                if idx % 50 == 0:
                    print(f"Progress: {idx}/{len(text_files)} files ({idx*100//len(text_files)}%)")

            except Exception as e:
                error_msg = f"Error processing {file_path}: {str(e)}"
                print(f"  ERROR: {error_msg}")
                self.errors.append(error_msg)

        print(f"\nProcessing complete!")
        print(f"Docs created: {self.docs_created}")
        print(f"Errors: {len(self.errors)}")

    def _process_file(self, file_info: Dict):
        """Process a single file."""
        file_path = Path(file_info['abs_path'])
        rel_path = file_info['path']
        category = file_info['category']

        # Read file content
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception as e:
            content = f"[ERROR: Could not read file - {str(e)}]"

        # Create docs directory for this file
        doc_dir = DOCS_DIR / Path(rel_path).parent
        doc_dir.mkdir(parents=True, exist_ok=True)

        # Generate _docs.md
        docs_md = self._generate_docs_md(file_path, rel_path, content, category, file_info)
        docs_path = doc_dir / f"{file_path.name}_docs.md"
        with open(docs_path, 'w', encoding='utf-8') as f:
            f.write(docs_md)

        # Generate _kw.md
        kw_md = self._generate_kw_md(file_path, rel_path, content, category)
        kw_path = doc_dir / f"{file_path.name}_kw.md"
        with open(kw_path, 'w', encoding='utf-8') as f:
            f.write(kw_md)

    def _generate_docs_md(self, file_path: Path, rel_path: str, content: str,
                         category: str, file_info: Dict) -> str:
        """Generate _docs.md for a file."""
        lines = content.split('\n')
        num_lines = len(lines)
        file_size = file_info['size']

        # Determine if content should be truncated
        max_content_lines = 10000
        truncated = num_lines > max_content_lines
        display_content = '\n'.join(lines[:max_content_lines])
        if truncated:
            display_content += f"\n\n... (truncated {num_lines - max_content_lines} lines) ..."

        # Build documentation
        doc = f"""# File Documentation: {file_path.name}

## Metadata
- **Path**: `{rel_path}`
- **Size**: {file_size:,} bytes
- **Lines**: {num_lines:,}
- **Category**: {category}
- **Extension**: {file_path.suffix}

---

## Original Source

```{self._get_language_hint(file_path.suffix)}
{display_content}
```

{f"**Note**: Source truncated for display. Full file has {num_lines:,} lines." if truncated else ""}

---

## High-Level Overview

"""

        # Add overview based on file type
        doc += self._generate_overview(file_path, content, category)

        doc += """

---

## Detailed Analysis

"""

        # Add detailed analysis
        doc += self._generate_detailed_analysis(file_path, content, category)

        doc += """

---

## Related Files

"""

        # Add related files section
        doc += self._find_related_files(rel_path, content)

        doc += """

---

## Performance & Security Notes

"""

        doc += self._generate_performance_security_notes(content, category)

        doc += f"""

---

**Generated**: {datetime.utcnow().isoformat()}Z
**Generator**: World's Best Repo Book Generator v1.0
"""

        return doc

    def _generate_kw_md(self, file_path: Path, rel_path: str, content: str, category: str) -> str:
        """Generate _kw.md for a file."""
        keywords = self._extract_keywords(content, category)

        kw_doc = f"""# Keywords: {file_path.name}

**File**: `{rel_path}`
**Total Keywords**: {len(keywords)}

---

## Keyword Index (A→Z)

"""

        # Group keywords by first letter
        by_letter = defaultdict(list)
        for kw in sorted(keywords, key=str.lower):
            first_letter = kw[0].upper()
            by_letter[first_letter].append(kw)

        # Generate A-Z sections
        for letter in sorted(by_letter.keys()):
            kw_doc += f"\n### {letter}\n\n"
            for kw in by_letter[letter]:
                # Create anchor-safe link
                anchor = self._create_anchor(kw)
                kw_doc += f"- **{kw}** → [`{file_path.name}_docs.md#{anchor}`](./{file_path.name}_docs.md#{anchor})\n"

        kw_doc += f"""

---

**Generated**: {datetime.utcnow().isoformat()}Z
"""

        return kw_doc

    def _get_language_hint(self, ext: str) -> str:
        """Get language hint for code blocks."""
        mapping = {
            '.py': 'python',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.jsx': 'jsx',
            '.tsx': 'tsx',
            '.md': 'markdown',
            '.json': 'json',
            '.yaml': 'yaml',
            '.yml': 'yaml',
            '.toml': 'toml',
            '.sh': 'bash',
            '.bash': 'bash',
            '.html': 'html',
            '.css': 'css',
            '.r': 'r',
            '.R': 'r',
            '.sql': 'sql',
        }
        return mapping.get(ext, '')

    def _generate_overview(self, file_path: Path, content: str, category: str) -> str:
        """Generate high-level overview."""
        overview = f"This is a **{category}** file named `{file_path.name}`.\n\n"

        if category == 'python':
            # Find classes and functions
            classes = re.findall(r'class\s+(\w+)', content)
            functions = re.findall(r'def\s+(\w+)', content)
            imports = re.findall(r'(?:from\s+[\w.]+\s+)?import\s+([\w.,\s]+)', content)

            overview += f"**Python Module**\n\n"
            if classes:
                overview += f"- **Classes** ({len(classes)}): {', '.join(classes[:10])}"
                if len(classes) > 10:
                    overview += f" ... and {len(classes)-10} more"
                overview += "\n"
            if functions:
                overview += f"- **Functions** ({len(functions)}): {', '.join(functions[:10])}"
                if len(functions) > 10:
                    overview += f" ... and {len(functions)-10} more"
                overview += "\n"
            if imports:
                overview += f"- **Import Statements**: {len(imports)}\n"

        elif category == 'documentation':
            # Count sections
            headings = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)
            overview += f"**Documentation File**\n\n"
            if headings:
                overview += f"- **Sections**: {len(headings)}\n"
                overview += f"- **Main Topics**: {', '.join(headings[:5])}\n"

        elif category == 'config':
            overview += f"**Configuration File**\n\n"
            overview += f"This file contains configuration settings for the project.\n"

        else:
            # Generic analysis
            lines = content.split('\n')
            overview += f"This file contains {len(lines)} lines of code/text.\n"

        return overview

    def _generate_detailed_analysis(self, file_path: Path, content: str, category: str) -> str:
        """Generate detailed analysis of file contents."""
        analysis = ""

        if category == 'python':
            # Analyze Python code structure
            analysis += self._analyze_python_code(content)
        elif category == 'config':
            analysis += "### Configuration Structure\n\n"
            analysis += "This configuration file defines settings and parameters for the project.\n"
        elif category == 'documentation':
            analysis += "### Documentation Structure\n\n"
            headings = re.findall(r'^(#+)\s+(.+)$', content, re.MULTILINE)
            if headings:
                analysis += "**Table of Contents**:\n\n"
                for level, heading in headings[:20]:
                    indent = "  " * (len(level) - 1)
                    analysis += f"{indent}- {heading}\n"
        else:
            analysis += "This file contains code or text data. See the original source above for full details.\n"

        return analysis

    def _analyze_python_code(self, content: str) -> str:
        """Analyze Python code structure."""
        analysis = "### Python Code Structure\n\n"

        # Find all class definitions
        class_pattern = r'class\s+(\w+)(\([^)]*\))?:'
        classes = re.findall(class_pattern, content)

        if classes:
            analysis += "#### Classes\n\n"
            for class_name, inheritance in classes[:20]:
                analysis += f"- **`{class_name}`**{inheritance}\n"

        # Find all function definitions
        func_pattern = r'def\s+(\w+)\s*\(([^)]*)\):'
        functions = re.findall(func_pattern, content)

        if functions:
            analysis += "\n#### Functions\n\n"
            for func_name, params in functions[:30]:
                analysis += f"- **`{func_name}({params})`**\n"

        # Find decorators
        decorators = re.findall(r'@(\w+)', content)
        if decorators:
            unique_decorators = set(decorators)
            analysis += f"\n#### Decorators Used\n\n"
            analysis += f"{', '.join(sorted(unique_decorators))}\n"

        return analysis

    def _find_related_files(self, rel_path: str, content: str) -> str:
        """Find related files based on imports and references."""
        related = "The following files may be related based on imports and references:\n\n"

        # Python imports
        imports = re.findall(r'from\s+([\w.]+)\s+import', content)
        imports += re.findall(r'import\s+([\w.]+)', content)

        if imports:
            related += "**Imported Modules**:\n"
            for imp in sorted(set(imports))[:15]:
                related += f"- `{imp}`\n"
        else:
            related += "*No direct imports detected.*\n"

        return related

    def _generate_performance_security_notes(self, content: str, category: str) -> str:
        """Generate performance and security notes."""
        notes = ""

        # Security checks
        security_patterns = [
            (r'eval\s*\(', 'Uses `eval()` - potential security risk'),
            (r'exec\s*\(', 'Uses `exec()` - potential security risk'),
            (r'os\.system\s*\(', 'Uses `os.system()` - potential command injection risk'),
            (r'subprocess\.(call|run|Popen)', 'Uses subprocess - validate input carefully'),
            (r'pickle\.loads?', 'Uses pickle - only use with trusted data'),
            (r'input\s*\(', 'Uses `input()` - validate user input'),
        ]

        security_issues = []
        for pattern, warning in security_patterns:
            if re.search(pattern, content):
                security_issues.append(warning)

        if security_issues:
            notes += "### Security Considerations\n\n"
            for issue in security_issues:
                notes += f"- ⚠️ {issue}\n"
        else:
            notes += "No obvious security concerns detected in static analysis.\n"

        return notes

    def _extract_keywords(self, content: str, category: str) -> Set[str]:
        """Extract keywords from content."""
        keywords = set()

        if category == 'python':
            # Classes
            keywords.update(re.findall(r'class\s+(\w+)', content))
            # Functions
            keywords.update(re.findall(r'def\s+(\w+)', content))
            # Imports
            keywords.update(re.findall(r'from\s+[\w.]+\s+import\s+(\w+)', content))
            keywords.update(re.findall(r'import\s+([\w]+)', content))
            # Variables
            keywords.update(re.findall(r'\b([A-Z][A-Z_]+)\b', content))  # Constants

        # Generic identifiers
        keywords.update(re.findall(r'\b([A-Z][a-zA-Z0-9]+)\b', content))  # CamelCase
        keywords.update(re.findall(r'\b([a-z_][a-z0-9_]{3,})\b', content))  # snake_case

        # Filter common words
        common = {'the', 'and', 'for', 'with', 'this', 'that', 'from', 'import',
                 'true', 'false', 'none', 'null', 'self', 'return', 'class', 'def'}
        keywords = {k for k in keywords if k.lower() not in common and len(k) > 2 and len(k) < 50}

        # Limit to reasonable number
        return set(sorted(keywords)[:1000])

    def _create_anchor(self, text: str) -> str:
        """Create URL-safe anchor from text."""
        anchor = text.lower()
        anchor = re.sub(r'[^a-z0-9_-]', '-', anchor)
        anchor = re.sub(r'-+', '-', anchor)
        return anchor.strip('-')


def main():
    print("=" * 80)
    print("FILE DOCUMENTATION GENERATOR")
    print("=" * 80)

    generator = FileDocGenerator()
    generator.process_all()

    # Report summary
    summary = {
        'docs_created': generator.docs_created,
        'errors': len(generator.errors),
        'error_messages': generator.errors[:10]  # First 10 errors
    }

    print("\n" + "=" * 80)
    print("GENERATION SUMMARY:")
    print(json.dumps(summary, indent=2))
    print("=" * 80)


if __name__ == '__main__':
    main()
