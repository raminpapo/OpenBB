#!/usr/bin/env python3
"""
Folder Documentation Generator
Generates index.md, doc.md, and sub.md for each folder.
"""

import os
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import re

DOCS_DIR = Path("./docs")
MANIFEST_PATH = DOCS_DIR / "manifest.json"


class FolderDocGenerator:
    """Generates documentation for folders."""

    def __init__(self):
        self.manifest = self._load_manifest()
        self.folder_structure = self._build_folder_structure()
        self.docs_created = 0

    def _load_manifest(self):
        """Load manifest file."""
        with open(MANIFEST_PATH, 'r') as f:
            return json.load(f)

    def _build_folder_structure(self):
        """Build folder structure from manifest files."""
        structure = defaultdict(lambda: {'files': [], 'subdirs': set()})

        for file_info in self.manifest.get('files', []):
            file_path = Path(file_info['path'])
            folder = str(file_path.parent)

            # Add file to folder
            structure[folder]['files'].append({
                'name': file_path.name,
                'path': file_info['path'],
                'category': file_info['category'],
                'is_binary': file_info['is_binary'],
                'size': file_info['size']
            })

            # Track parent relationships
            if folder != '.':
                parent = str(file_path.parent.parent)
                structure[parent]['subdirs'].add(folder)

        return structure

    def process_all(self):
        """Process all folders."""
        print(f"Processing {len(self.folder_structure)} folders...")

        for idx, folder in enumerate(sorted(self.folder_structure.keys()), 1):
            try:
                print(f"[{idx}/{len(self.folder_structure)}] Processing folder: {folder}")
                self._process_folder(folder)
                self.docs_created += 3  # index.md + doc.md + sub.md
            except Exception as e:
                print(f"  ERROR: {e}")

        print(f"\nFolder documentation complete! Created {self.docs_created} docs.")

    def _process_folder(self, folder: str):
        """Process a single folder."""
        folder_info = self.folder_structure[folder]

        # Create docs directory for this folder
        if folder == '.':
            doc_dir = DOCS_DIR
            rel_doc_dir = "."
        else:
            doc_dir = DOCS_DIR / folder
            rel_doc_dir = folder

        doc_dir.mkdir(parents=True, exist_ok=True)

        # Generate index.md
        index_md = self._generate_index_md(folder, folder_info)
        with open(doc_dir / "index.md", 'w', encoding='utf-8') as f:
            f.write(index_md)

        # Generate doc.md
        doc_md = self._generate_doc_md(folder, folder_info)
        with open(doc_dir / "doc.md", 'w', encoding='utf-8') as f:
            f.write(doc_md)

        # Generate sub.md (keyword aggregation)
        sub_md = self._generate_sub_md(folder, folder_info)
        with open(doc_dir / "sub.md", 'w', encoding='utf-8') as f:
            f.write(sub_md)

    def _generate_index_md(self, folder: str, folder_info: dict) -> str:
        """Generate index.md for a folder."""
        folder_name = folder if folder != '.' else 'Root'

        index = f"""# Folder Index: {folder_name}

**Path**: `{folder}`

---

## Overview

This folder contains {len(folder_info['files'])} files and {len(folder_info['subdirs'])} subdirectories.

---

## Files in This Folder

"""

        # Sort files by category
        by_category = defaultdict(list)
        for file in folder_info['files']:
            by_category[file['category']].append(file)

        for category in sorted(by_category.keys()):
            index += f"\n### {category.title()} Files\n\n"
            for file in sorted(by_category[category], key=lambda x: x['name']):
                if file['is_binary']:
                    index += f"- `{file['name']}` ({self._format_size(file['size'])}) *[binary]*\n"
                else:
                    # Link to file docs
                    index += f"- [`{file['name']}`](./{file['name']}_docs.md) ({self._format_size(file['size'])})\n"

        # Subdirectories
        if folder_info['subdirs']:
            index += "\n---\n\n## Subdirectories\n\n"
            for subdir in sorted(folder_info['subdirs']):
                subdir_name = Path(subdir).name
                relative_path = os.path.relpath(subdir, folder if folder != '.' else '.')
                index += f"- [`{subdir_name}/`](./{relative_path}/index.md)\n"

        index += f"""

---

**Generated**: {datetime.utcnow().isoformat()}Z
"""

        return index

    def _generate_doc_md(self, folder: str, folder_info: dict) -> str:
        """Generate doc.md with narrative context for folder."""
        folder_name = folder if folder != '.' else 'Root'

        doc = f"""# Documentation: {folder_name}

**Path**: `{folder}`

---

## Purpose & Role

"""

        # Infer purpose from folder name and contents
        doc += self._infer_folder_purpose(folder, folder_info)

        doc += """

---

## Contents Summary

"""

        # Categorize and summarize contents
        by_category = defaultdict(list)
        for file in folder_info['files']:
            by_category[file['category']].append(file)

        doc += f"This folder contains **{len(folder_info['files'])} files** across **{len(by_category)} categories**:\n\n"

        for category in sorted(by_category.keys()):
            count = len(by_category[category])
            total_size = sum(f['size'] for f in by_category[category])
            doc += f"- **{category.title()}**: {count} files ({self._format_size(total_size)})\n"

        if folder_info['subdirs']:
            doc += f"\n**Subdirectories**: {len(folder_info['subdirs'])}\n"

        doc += """

---

## Key Concepts

"""

        # Extract key concepts from file names and structure
        doc += self._extract_key_concepts(folder, folder_info)

        doc += f"""

---

**Generated**: {datetime.utcnow().isoformat()}Z
"""

        return doc

    def _generate_sub_md(self, folder: str, folder_info: dict) -> str:
        """Generate sub.md with aggregated keywords from child files."""
        folder_name = folder if folder != '.' else 'Root'

        sub = f"""# Aggregated Keywords: {folder_name}

**Path**: `{folder}`

---

## Keyword Index (A→Z)

This index aggregates keywords from all files in this folder and its subdirectories.

"""

        # Collect keywords from all _kw.md files in this folder
        keywords_by_letter = defaultdict(list)

        if folder == '.':
            doc_dir = DOCS_DIR
        else:
            doc_dir = DOCS_DIR / folder

        # Scan for _kw.md files
        if doc_dir.exists():
            for kw_file in doc_dir.glob("*_kw.md"):
                try:
                    with open(kw_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Extract keywords (simplified - just get words in bold)
                        kws = re.findall(r'\*\*(\w+)\*\*', content)
                        for kw in kws[:50]:  # Limit per file
                            first_letter = kw[0].upper()
                            keywords_by_letter[first_letter].append({
                                'keyword': kw,
                                'file': kw_file.name
                            })
                except Exception as e:
                    pass

        # Generate A-Z sections
        if keywords_by_letter:
            for letter in sorted(keywords_by_letter.keys()):
                sub += f"\n### {letter}\n\n"
                seen = set()
                for item in keywords_by_letter[letter]:
                    kw = item['keyword']
                    if kw not in seen:
                        sub += f"- **{kw}**\n"
                        seen.add(kw)
        else:
            sub += "\n*No keywords extracted yet. Keywords will be populated after file documentation is complete.*\n"

        sub += f"""

---

**Generated**: {datetime.utcnow().isoformat()}Z
"""

        return sub

    def _infer_folder_purpose(self, folder: str, folder_info: dict) -> str:
        """Infer folder purpose from name and contents."""
        purpose = ""

        folder_name = Path(folder).name.lower() if folder != '.' else 'root'

        # Common folder patterns
        if folder_name in ['tests', 'test']:
            purpose = "This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.\n"
        elif folder_name in ['docs', 'documentation']:
            purpose = "This folder contains **documentation** for the project.\n"
        elif folder_name in ['src', 'source']:
            purpose = "This folder contains the **source code** for the project.\n"
        elif folder_name in ['scripts', 'tools']:
            purpose = "This folder contains **utility scripts and tools** for development and maintenance.\n"
        elif folder_name in ['config', 'conf', 'configuration']:
            purpose = "This folder contains **configuration files** for the project.\n"
        elif folder_name in ['assets', 'static', 'resources']:
            purpose = "This folder contains **static assets and resources** used by the project.\n"
        elif folder_name in ['examples', 'demos']:
            purpose = "This folder contains **examples and demonstrations** of how to use the project.\n"
        elif 'api' in folder_name:
            purpose = "This folder contains **API-related code**, including endpoints, handlers, and API utilities.\n"
        elif 'model' in folder_name:
            purpose = "This folder contains **data models and schemas** for the project.\n"
        elif 'util' in folder_name or 'helper' in folder_name:
            purpose = "This folder contains **utility functions and helper code** used throughout the project.\n"
        elif folder == '.':
            purpose = "This is the **root directory** of the project. It contains top-level configuration files, documentation, and entry points.\n"
        else:
            # Generic description
            purpose = f"This folder is part of the project structure and contains code/resources for `{folder_name}`.\n"

        # Add info based on file types
        by_category = defaultdict(list)
        for file in folder_info['files']:
            by_category[file['category']].append(file)

        if 'python' in by_category and len(by_category['python']) > 10:
            purpose += f"\nContains a substantial Python codebase with {len(by_category['python'])} Python files.\n"

        return purpose

    def _extract_key_concepts(self, folder: str, folder_info: dict) -> str:
        """Extract key concepts from folder."""
        concepts = "Key concepts and components in this folder:\n\n"

        # Extract from file names
        file_names = [f['name'] for f in folder_info['files'] if not f['is_binary']]

        # Look for common patterns
        if any('test' in name.lower() for name in file_names):
            concepts += "- **Testing**: Contains test files and testing utilities\n"
        if any('api' in name.lower() for name in file_names):
            concepts += "- **API**: Contains API-related code\n"
        if any('model' in name.lower() for name in file_names):
            concepts += "- **Models**: Contains data models or model definitions\n"
        if any('util' in name.lower() or 'helper' in name.lower() for name in file_names):
            concepts += "- **Utilities**: Contains utility and helper functions\n"
        if any('config' in name.lower() for name in file_names):
            concepts += "- **Configuration**: Contains configuration management\n"

        # Count Python modules
        py_files = [f for f in folder_info['files'] if f['category'] == 'python']
        if py_files:
            concepts += f"- **Python Modules**: {len(py_files)} Python source files\n"

        return concepts

    def _format_size(self, size: int) -> str:
        """Format byte size as human-readable string."""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} TB"


def main():
    print("=" * 80)
    print("FOLDER DOCUMENTATION GENERATOR")
    print("=" * 80)

    generator = FolderDocGenerator()
    generator.process_all()

    print("\n" + "=" * 80)
    print(f"COMPLETE: {generator.docs_created} folder docs created")
    print("=" * 80)


if __name__ == '__main__':
    main()
