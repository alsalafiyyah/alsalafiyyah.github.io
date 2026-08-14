import re
from pathlib import Path

try:
    import yaml
except ImportError:
    print("WARNING: 'pyyaml' library is not installed. Run 'pip install pyyaml' for full YAML syntax checking.")
    yaml = None

TARGET_DIR = Path("_posts")

# Regex to detect stacked duplicate frontmatter blocks
STACKED_FM_PATTERN = re.compile(
    r"^---\r?\n(.*?)\r?\n---\r?\n(?:\s*\r?\n)?---\r?\n(.*?)\r?\n---",
    re.DOTALL
)


def validate_file_frontmatter(file_path: Path) -> list[str]:
    errors = []

    try:
        content = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            content = file_path.read_text(encoding="latin-1")
        except Exception as e:
            return [f"Encoding Error: Cannot read file ({e})"]
    except Exception as e:
        return [f"Read Error: {e}"]

    # 1. Check if file starts with '---'
    if not content.startswith("---"):
        errors.append("Missing starting '---' delimiter on line 1")
        return errors

    # 2. Check for stacked double frontmatter blocks
    if STACKED_FM_PATTERN.match(content):
        errors.append("Multiple/stacked duplicate frontmatter blocks detected")

    # 3. Find closing '---' delimiter
    fm_delimiters = list(re.finditer(r"^---\r?$", content, re.MULTILINE))

    if len(fm_delimiters) < 2:
        errors.append("Unclosed frontmatter: Missing closing '---' delimiter")
        return errors

    # Extract primary frontmatter block content
    start_pos = fm_delimiters[0].end()
    end_pos = fm_delimiters[1].start()
    fm_raw = content[start_pos:end_pos]

    if not fm_raw.strip():
        errors.append("Frontmatter block is empty")
        return errors

    # 4. Parse YAML Syntax with PyYAML (if installed)
    if yaml:
        try:
            parsed_data = yaml.safe_load(fm_raw)
            if not isinstance(parsed_data, dict) and parsed_data is not None:
                errors.append(f"Invalid YAML structure (expected key-value pairs, got {type(parsed_data).__name__})")
        except yaml.YAMLError as exc:
            # Format YAML parser error cleanly
            clean_err = str(exc).replace("\n", " ").strip()
            errors.append(f"YAML Syntax Error: {clean_err}")

    return errors


def main():
    if not TARGET_DIR.exists():
        print(f"Directory not found: {TARGET_DIR.resolve()}")
        return

    all_files = sorted(TARGET_DIR.rglob("*.md"))
    error_count = 0

    print(f"Scanning {len(all_files)} files in '{TARGET_DIR}' for frontmatter errors...\n")

    for file_path in all_files:
        errors = validate_file_frontmatter(file_path)
        if errors:
            error_count += 1
            print(f"❌ {file_path}")
            for err in errors:
                print(f"   └── {err}")
            print()

    print("=" * 60)
    if error_count == 0:
        print("✅ No frontmatter errors found! All posts are valid.")
    else:
        print(f"⚠️ Found errors in {error_count} file(s).")


if __name__ == "__main__":
    main()