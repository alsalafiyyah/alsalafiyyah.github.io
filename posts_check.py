import re
from pathlib import Path

# Path to the parent posts directory
TARGET_DIR = Path("_posts")

# Regex to check if 'summary:' exists inside the frontmatter
SUMMARY_PATTERN = re.compile(r"^summary:\s*\S+", re.MULTILINE | re.IGNORECASE)


def has_valid_summary(file_path: Path) -> bool:
    """Checks if a file's YAML frontmatter contains a non-empty 'summary:' field."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            content = file_path.read_text(encoding="latin-1")
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return True  # Skip broken files

    # Match YAML frontmatter between starting and closing '---'
    frontmatter_match = re.search(r"^---\r?\n(.*?)\r?\n---", content, re.DOTALL)

    if not frontmatter_match:
        # File doesn't have valid YAML frontmatter at all
        return False

    frontmatter = frontmatter_match.group(1)

    # Check if 'summary:' with actual text content exists in the frontmatter
    return bool(SUMMARY_PATTERN.search(frontmatter))


def find_posts_missing_summary(directory: Path):
    if not directory.exists():
        print(f"Directory not found: {directory.resolve()}")
        return

    missing_summary_files = []
    total_files = 0

    # Recursively find all markdown files in _posts and all subdirectories
    for file_path in sorted(directory.rglob("*.md")):
        total_files += 1
        if not has_valid_summary(file_path):
            missing_summary_files.append(file_path)

    # Print results summary
    print(f"Scanned {total_files} file(s) across '{directory}'\n")
    print(f"Found {len(missing_summary_files)} post(s) missing a summary:\n")

    for path in missing_summary_files:
        print(path)

    return missing_summary_files


if __name__ == "__main__":
    find_posts_missing_summary(TARGET_DIR)