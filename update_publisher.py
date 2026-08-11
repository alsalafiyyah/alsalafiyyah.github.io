from pathlib import Path
import re

# Configuration
POSTS_DIR = Path("_posts")
OLD_EMAIL = "alsalafiyyah@icloud.com"
NEW_EMAIL = "alsalafiyyah.manhaj@gmail.com"

# Regex pattern to target 'publisher:' key inside YAML frontmatter
# Supports trailing comments, quotes, and optional surrounding whitespace
FRONTMATTER_REGEX = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
PUBLISHER_REGEX = re.compile(
    rf'^(publisher:\s*["\']?){re.escape(OLD_EMAIL)}(["\']?.*)$', re.MULTILINE
)


def update_frontmatter(file_path: Path) -> bool:
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

    # Check if file has frontmatter
    match = FRONTMATTER_REGEX.match(content)
    if not match:
        return False

    frontmatter = match.group(1)

    # Check if OLD_EMAIL is present in the publisher field
    if OLD_EMAIL not in frontmatter:
        return False

    # Replace publisher value within frontmatter only
    updated_frontmatter = PUBLISHER_REGEX.sub(rf"\1{NEW_EMAIL}\2", frontmatter)

    # If no replacement was made, skip
    if updated_frontmatter == frontmatter:
        return False

    # Reconstruct full content
    new_content = f"---\n{updated_frontmatter}\n---" + content[match.end() - 1 :]

    # Write changes back to file
    file_path.write_text(new_content, encoding="utf-8")
    return True


def main():
    if not POSTS_DIR.exists():
        print(f"Directory '{POSTS_DIR}' not found. Please run script from site root.")
        return

    updated_count = 0
    scanned_count = 0

    print("Scanning posts...")

    # Recursively traverse all subdirectories inside _posts/
    for file_path in POSTS_DIR.rglob("*"):
        if file_path.is_file() and file_path.suffix in [".md", ".markdown"]:
            scanned_count += 1
            if update_frontmatter(file_path):
                updated_count += 1
                print(f"Updated: {file_path}")

    print("\n--- Execution Summary ---")
    print(f"Total markdown files scanned: {scanned_count}")
    print(f"Total files updated: {updated_count}")


if __name__ == "__main__":
    main()