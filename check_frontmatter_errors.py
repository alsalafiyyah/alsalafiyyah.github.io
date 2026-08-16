from pathlib import Path
import yaml

def check_frontmatter_errors(base_dir="_posts"):
    """
    Scans all markdown files in the specified Jekyll directory recursively,
    validates YAML front matter syntax, and checks for empty or malformed muftis data.
    """
    posts_path = Path(base_dir)
    
    if not posts_path.exists():
        print(f"Directory '{base_dir}' not found.")
        return

    total_files = 0
    error_count = 0

    print(f"Scanning '{base_dir}' for front matter errors...\n" + "="*50)

    for file_path in posts_path.rglob("*.md"):
        total_files += 1
        file_errors = []
        
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            # Check if file starts with front matter delimiter
            if not content.startswith("---"):
                file_errors.append("Missing opening '---' front matter delimiter at the very top.")
            else:
                parts = content.split("---", 2)
                if len(parts) < 3:
                    file_errors.append("Malformed front matter block (missing closing '---').")
                else:
                    front_matter_raw = parts[1]
                    try:
                        front_matter = yaml.safe_load(front_matter_raw)
                        
                        if front_matter is None:
                            file_errors.append("Front matter block is completely empty.")
                        elif not isinstance(front_matter, dict):
                            file_errors.append("Front matter is not a valid YAML key-value dictionary.")
                        else:
                            # Specific check for your 'muftis' structure errors/formatting issues
                            muftis = front_matter.get("muftis")
                            if muftis is not None:
                                if not isinstance(muftis, dict):
                                    file_errors.append("'muftis' field must be a dictionary/mapping.")
                                else:
                                    roles = ["chairman", "deputy_chairman", "members"]
                                    for role in roles:
                                        if role in muftis:
                                            role_data = muftis[role]
                                            # If it's defined but empty or not a list
                                            if role_data is not None:
                                                if not isinstance(role_data, list):
                                                    file_errors.append(f"'muftis -> {role}' must be a list of items.")
                                                else:
                                                    for index, item in enumerate(role_data):
                                                        if item is None:
                                                            # Empty bullet like `- ` without name/url
                                                            file_errors.append(f"'muftis -> {role}' item at index {index} is empty.")
                                                        elif not isinstance(item, dict):
                                                            file_errors.append(f"'muftis -> {role}' item at index {index} is improperly formatted.")
                                                        else:
                                                            if "name" not in item or "url" not in item:
                                                                file_errors.append(f"'muftis -> {role}' item at index {index} is missing 'name' or 'url'.")
                                                            elif not item.get("name") or not item.get("url"):
                                                                file_errors.append(f"'muftis -> {role}' item at index {index} has a blank 'name' or 'url'.")
                                                                
                    except yaml.YAMLError as ye:
                        file_errors.append(f"YAML Syntax Error: {ye}")
                        
        except Exception as e:
            file_errors.append(f"File reading error: {e}")

        # Report findings for this file if any errors exist
        if file_errors:
            error_count += 1
            print(f"File: {file_path}")
            for err in file_errors:
                print(f"  ❌ {err}")
            print("-" * 50)

    print(f"\nScan complete. Scanned {total_files} files. Found errors in {error_count} file(s).")

if __name__ == "__main__":
    check_frontmatter_errors("_posts")