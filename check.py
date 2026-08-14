import re
from pathlib import Path

# Path to the directory
TARGET_DIR = Path("_posts/alifta")

# Regex pattern matching 'shia', 'shi'a', or 'shi`a' as standalone words
# \b handles word boundaries; case-insensitive flag handles Shia, SHIA, etc.
PATTERN = re.compile(r"\b(shia|shi'a|shi`a|shiah|shi'ah|shi`ah|shiites|shiis|ismailis|ismailiyyah|"
    r"shi'ites|isma'iliyyah|khomeiniyyah|khomeinism|khomeini|imamate|imamis|"
    r"imamiyah|imamiyyah|shi'i|shi'is|shi`i|shi`is|shi''ah|Al-Quburiyyah|Al-Quburiyyun|Al-Quburis|sufism|sufi|sufis|grave-worshippers|grave-worship|Al-Mu'tazilah|Al-Jahmiyyah)\b", re.IGNORECASE)


def find_matching_posts(directory: Path):
    if not directory.exists():
        print(f"Directory not found: {directory.resolve()}")
        return

    matching_files = []

    # Recursively find all .md files in all subdirectories
    for file_path in directory.rglob("*.md"):
        try:
            # Read file content safely with UTF-8 encoding
            content = file_path.read_text(encoding="utf-8")

            # Check if any variant exists in the content
            if PATTERN.search(content):
                matching_files.append(file_path)

        except UnicodeDecodeError:
            # Fallback for files with alternative encodings if UTF-8 fails
            try:
                content = file_path.read_text(encoding="latin-1")
                if PATTERN.search(content):
                    matching_files.append(file_path)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    # Display results
    print(
        f"Found {len(matching_files)} matching file(s) in '{directory}':\n"
    )
    for path in matching_files:
        print(path)


if __name__ == "__main__":
    find_matching_posts(TARGET_DIR)