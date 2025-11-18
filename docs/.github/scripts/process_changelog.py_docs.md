# Documentation: .github/scripts/process_changelog.py

## File Metadata
- **Path**: `.github/scripts/process_changelog.py`
- **Size**: 2,753 characters, 69 lines
- **Words**: 329
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
# process_changelog.py
import logging
import re
import sys

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def process_changelog(file_path, release_pr_number):
    # Attempt to open and read the file content
    try:
        with open(file_path) as file:  # Default mode is 'r' for read
            lines = file.readlines()
    except OSError as e:  # Catching file I/O errors
        logging.error(f"Failed to open or read file: {e}")
        return

    pr_occurrences = {}  # Dictionary to track occurrences of PR numbers

    # Iterate through each line to find PR numbers
    for i, line in enumerate(lines):
        match = re.search(r"\(#(\d+)\)", line)  # Regex to find PR numbers
        if match:
            pr_number = int(match.group(1))
            # Add line index to the list of occurrences for the PR number
            if pr_number not in pr_occurrences:
                pr_occurrences[pr_number] = []
            pr_occurrences[pr_number].append(i)

    # Set of indices to remove: includes all but last occurrence of each PR number
    to_remove = {i for pr, indices in pr_occurrences.items() if len(indices) > 1 for i in indices[:-1]}
    # Also remove any PR entries less than or equal to the specified release PR number
    to_remove.update(i for pr, indices in pr_occurrences.items() for i in indices if pr <= release_pr_number)

    # Filter out lines marked for removal
    processed_lines = [line for i, line in enumerate(lines) if i not in to_remove]

    # Final sweep: Ensure no missed duplicates, keeping only the last occurrence
    final_lines = []
    seen_pr_numbers = set()  # Track seen PR numbers to identify duplicates
    for line in reversed(processed_lines):  # Start from the end to keep the last occurrence
        match = re.search(r"\(#(\d+)\)", line)
        if match:
            pr_number = int(match.group(1))
            if pr_number in seen_pr_numbers:
                continue  # Skip duplicate entries
            seen_pr_numbers.add(pr_number)
        final_lines.append(line)
    final_lines.reverse()  # Restore original order

    # Write the processed lines back to the file
    try:
        with open(file_path, "w") as file:
            file.writelines(final_lines)
    except OSError as e:  # Handling potential write errors
        logging.error(f"Failed to write to file: {e}")


if __name__ == "__main__":
    # Ensure correct command line arguments
    if len(sys.argv) < 3:
        logging.error("Usage: python process_changelog.py <changelog_file> <release_pr_number>")
        sys.exit(1)

    file_path = sys.argv[1]
    release_pr_number = int(sys.argv[2])
    process_changelog(file_path, release_pr_number)

```

## High-Level Overview

process_changelog.py
Set up basic configuration for logging
Attempt to open and read the file content
Iterate through each line to find PR numbers
Add line index to the list of occurrences for the PR number
Set of indices to remove: includes all but last occurrence of each PR number
Also remove any PR entries less than or equal to the specified release PR number
Filter out lines marked for removal
Final sweep: Ensure no missed duplicates, keeping only the last occurrence

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (1):
`process_changelog`

**Imports** (4):
`logging`, `re`, `sys`, `the`


## Key Components

No major components extracted.

## Usage & Examples

This file can be run as a script. See the `__main__` block for entry point.

## Related Files

- `logging`
- `re`
- `sys`

## Notes
- Generated: 2025-11-18T07:54:34.561335
- Generator: World's Best Repo Book Generator v1.0.0
