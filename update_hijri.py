import os
import re
from datetime import datetime
import yaml
from hijridate import Gregorian

# Updated target directory for testing
POSTS_DIR = "_posts/alifta/"

# Regex to match Jekyll post filenames: YYYY-MM-DD-title.md
FILENAME_REGEX = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-(.+)\.md$")

def process_posts():
    if not os.path.exists(POSTS_DIR):
        print(f"Error: Directory '{POSTS_DIR}' not found.")
        return

    # Using os.walk to safely check the folder and any nested subdirectories
    processed_count = 0
    for root, _, files in os.walk(POSTS_DIR):
        for filename in files:
            if not filename.endswith(".md"):
                continue

            match = FILENAME_REGEX.match(filename)
            if not match:
                print(f"Skipping (name format mismatch): {filename}")
                continue

            year, month, day, _ = match.groups()
            gregorian_date_str = f"{year}-{month}-{day}"
            
            # Convert Gregorian date to Hijri
            try:
                g_date = datetime.strptime(gregorian_date_str, "%Y-%m-%d").date()
                hijri_obj = Gregorian(g_date.year, g_date.month, g_date.day).to_hijri()
                # Format as YYYY-MM-DD (e.g., 1448-02-27)
                hijri_formatted = f"{hijri_obj.year:04d}-{hijri_obj.month:02d}-{hijri_obj.day:02d}"
            except Exception as e:
                print(f"Skipping {filename}: Error converting date ({e})")
                continue

            filepath = os.path.join(root, filename)
            update_file_frontmatter(filepath, hijri_formatted)
            processed_count += 1

    print(f"\nTest complete! Processed {processed_count} files in '{POSTS_DIR}'.")

def update_file_frontmatter(filepath, new_hijri_date):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Split frontmatter using Jekyll standard delimiters (---)
    frontmatter_pattern = re.compile(r"^(---[\s\S]*?---)([\s\S]*)$")
    match = frontmatter_pattern.match(content)

    if not match:
        print(f"Skipping {filepath}: No valid YAML frontmatter found.")
        return

    frontmatter_raw = match.group(1)
    body = match.group(2)

    # Parse YAML frontmatter
    try:
        yaml_content = frontmatter_raw.strip().strip("---").strip()
        data = yaml.safe_load(yaml_content)
        if not isinstance(data, dict):
            data = {}
    except yaml.YAMLError as e:
        print(f"Skipping {filepath}: YAML parsing error ({e})")
        return

    # Update or add 'hijri' key
    data["hijri"] = new_hijri_date

    # Dump back to YAML string
    new_yaml_content = yaml.dump(data, sort_keys=False, allow_unicode=True).strip()
    new_frontmatter = f"---\n{new_yaml_content}\n---\n"

    # Recombine with post body
    new_content = new_frontmatter + body

    # Write back changes to file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Updated: {os.path.basename(filepath)} -> hijri: {new_hijri_date}")

if __name__ == "__main__":
    process_posts()