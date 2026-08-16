from pathlib import Path
import yaml

def get_alifta_posts_with_muftis(base_dir="_posts/alifta"):
    """
    Scans the Jekyll _posts/alifta directory (including subdirectories), 
    parses front matter, and extracts post titles and muftis data.
    """
    posts_path = Path(base_dir)
    
    if not posts_path.exists():
        print(f"Directory '{base_dir}' not found.")
        return []

    posts_data = []

    # rglob("*.md") searches recursively inside _posts/alifta and any subfolders
    for file_path in posts_path.rglob("*.md"):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            # Jekyll front matter is enclosed between ---
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    front_matter_raw = parts[1]
                    front_matter = yaml.safe_load(front_matter_raw)
                    
                    if front_matter:
                        post_info = {
                            "filepath": str(file_path),
                            "title": front_matter.get("title", "Untitled"),
                            "date": front_matter.get("date"),
                            "muftis": front_matter.get("muftis", {})
                        }
                        posts_data.append(post_info)
        except Exception as e:
            print(f"Error parsing {file_path.name}: {e}")

    return posts_data

if __name__ == "__main__":
    posts = get_alifta_posts_with_muftis("_posts/alifta")
    
    print(f"Found {len(posts)} posts in _posts/alifta.\n")
    
    for post in posts:
        print(f"**File:** {post['filepath']}")
        print(f"**Title:** {post['title']}")
        print("**Muftis Structure:**")
        
        muftis = post.get("muftis", {})
        if muftis:
            # Handle chairman
            if muftis.get("chairman"):
                print("  - Chairman:")
                for c in muftis["chairman"]:
                    if c and c.get("name"):
                        print(f"    * {c['name']} ({c.get('url', '#')})")
            
            # Handle deputy chairman
            if muftis.get("deputy_chairman"):
                print("  - Deputy Chairman:")
                for dc in muftis["deputy_chairman"]:
                    if dc and dc.get("name"):
                        print(f"    * {dc['name']} ({dc.get('url', '#')})")
            
            # Handle members
            if muftis.get("members"):
                print("  - Members:")
                for m in muftis["members"]:
                    if m and m.get("name"):
                        print(f"    * {m['name']} ({m.get('url', '#')})")
        else:
            print("  - No muftis data found (or fields are empty).")
            
        print("-" * 40)