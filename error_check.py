import re
from pathlib import Path

TARGET_DIR = Path("_posts")

# Pattern to capture double frontmatter blocks at the start of the file
# Matches:
# ---
# <frontmatter 1>
# ---
# <frontmatter 2>
# ---
DOUBLE_FRONTMATTER_PATTERN = re.compile(
    r"^---\r?\n(.*?)\r?\n---\r?\n(?:\s*\r?\n)?---\r?\n(.*?)\r?\n---",
    re.DOTALL
)

def check_double_frontmatter(file_path: Path) -> bool:
    try:
        content = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            content = file_path.read_text(encoding="latin-1")
        except Exception:
            return False

    match = DOUBLE_FRONTMATTER_PATTERN.match(content)
    if not match:
        return False

    first_fm = match.group(1)

    # Check that the top block contains lang, mass_edited, and any hijri date
    has_lang = "lang: en" in first_fm
    has_mass_edited = "mass_edited: true" in first_fm
    has_hijri = "hijri:" in first_fm

    return has_lang and has_mass_edited and has_hijri


def main():
    if not TARGET_DIR.exists():
        print(f"Directory not found: {TARGET_DIR.resolve()}")
        return

    matching_files = []
    total_scanned = 0

    for file_path in sorted(TARGET_DIR.rglob("*.md")):
        total_scanned += 1
        if check_double_frontmatter(file_path):
            matching_files.append(file_path)

    print(f"Scanned {total_scanned} file(s) under '{TARGET_DIR}'.\n")
    print(f"Found {len(matching_files)} post(s) with double frontmatter containing any hijri date:\n")

    for path in matching_files:
        print(path)


if __name__ == "__main__":
    main()