import os
import frontmatter
from ruamel.yaml import YAML

def normalize_urls(data):
    """Recursively strip trailing slashes from URLs in dictionaries/lists 
       to ensure matching works regardless of slight trailing-slash discrepancies."""
    if isinstance(data, dict):
        return {k: normalize_urls(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [normalize_urls(item) for item in data]
    elif isinstance(data, str):
        return data.rstrip('/')
    return data

# Define the exact criteria structures mapped to their target groups
# URLs are normalized (trailing slashes stripped) for robust matching.
GROUP_RULES = {
    "group1": {
        "chairman": [{"name": "Shaykh Ibn Baz", "url": "/biography/binbaz"}],
        "deputy_chairman": [{"name": "Shaykh Abdul-Razzaq Afifi", "url": "/biography/afifi"}],
        "members": [
            {"name": "Shaykh Abdullah ibn Ghudayyan", "url": "/biography/ghudayyan"},
            {"name": "Shaykh Abdullah ibn Qa'ud", "url": "/biography/qaud"}
        ]
    },
    "group2": {
        "chairman": [{"name": "Shaykh Ibn Baz", "url": "/biography/binbaz"}],
        "deputy_chairman": [{"name": "Shaykh Abdul-Aziz Aal Al-Shaykh", "url": "/biography/abdulaziz"}],
        "members": [
            {"name": "Shaykh Abdullah ibn Ghudayyan", "url": "/biography/ghudayyan"},
            {"name": "Shaykh Salih Al-Fawzan", "url": "/biography/fawzan"},
            {"name": "Shaykh Bakr Abu Zayd", "url": "/biography/bakr"}
        ]
    },
    "group3": {
        "chairman": [{"name": "Shaykh Ibn Baz", "url": "/biography/binbaz"}],
        "deputy_chairman": [{"name": "Shaykh Abdul-Razzaq Afifi", "url": "/biography/afifi"}],
        "members": [
            {"name": "Shaykh Abdullah ibn Ghudayyan", "url": "/biography/ghudayyan"},
            {"name": "Shaykh Abdullah ibn Muni'", "url": "/biography/mani"}
        ]
    },
    "group4": {
        "chairman": [{"name": "Shaykh Abdul-Razzaq Afifi", "url": "/biography/afifi"}],
        "members": [
            {"name": "Shaykh Abdullah ibn Ghudayyan", "url": "/biography/ghudayyan"},
            {"name": "Shaykh Abdullah ibn Muni'", "url": "/biography/mani"}
        ]
    },
    "group5": {
        "chairman": [{"name": "Shaykh Abdul-Aziz Aal Al-Shaykh", "url": "/biography/abdulaziz"}],
        "members": [
            {"name": "Shaykh Abdullah ibn Ghudayyan", "url": "/biography/ghudayyan"},
            {"name": "Shaykh Salih Al-Fawzan", "url": "/biography/fawzan"},
            {"name": "Shaykh Bakr Abu Zayd", "url": "/biography/bakr"}
        ]
    },
    "group6": {
        "chairman": [{"name": "Shaykh Ibn Baz", "url": "/biography/binbaz"}],
        "deputy_chairman": [{"name": "Shaykh Abdul-Razzaq Afifi", "url": "/biography/afifi"}],
        "members": [{"name": "Shaykh Abdullah ibn Ghudayyan", "url": "/biography/ghudayyan"}]
    },
    "group7": {
        "chairman": [{"name": "Shaykh Ibn Baz", "url": "/biography/binbaz"}],
        "deputy_chairman": [{"name": "Shaykh Abdul-Razzaq Afifi", "url": "/biography/afifi"}],
        "members": [
            {"name": "Shaykh Abdullah ibn Ghudayyan", "url": "/biography/ghudayyan"},
            {"name": "Shaykh Abdul-Aziz Aal Al-Shaykh", "url": "/biography/abdulaziz"},
            {"name": "Shaykh Salih Al-Fawzan", "url": "/biography/fawzan"},
            {"name": "Shaykh Bakr Abu Zayd", "url": "/biography/bakr"}
        ]
    },
    "group8": {
        "chairman": [{"name": "Shaykh Ibn Baz", "url": "/biography/binbaz"}],
        "members": [{"name": "Shaykh Abdullah ibn Ghudayyan", "url": "/biography/ghudayyan"}]
    },
    "group9": {
        "chairman": [{"name": "Shaykh Ibn Baz", "url": "/biography/binbaz"}],
        "deputy_chairman": [{"name": "Shaykh Abdul-Razzaq Afifi", "url": "/biography/afifi"}],
        "members": [{"name": "Shaykh Abdullah ibn Qa'ud", "url": "/biography/qaud"}]
    },
    "group10": {
        "chairman": [{"name": "Shaykh Ibn Baz", "url": "/biography/binbaz"}],
        "members": [{"name": "Shaykh Abdullah ibn Qa'ud", "url": "/biography/qaud"}]
    },
    "group11": {
        "chairman": [{"name": "Shaykh Ibrahim ibn Muhammad Aal Al-Shaykh", "url": "/biography/ibrahim"}],
        "deputy_chairman": [{"name": "Shaykh Abdul-Razzaq Afifi", "url": "/biography/afifi"}],
        "members": [{"name": "Shaykh Abdullah ibn Sulayman Ibn Muni'", "url": "/biography/mani"}]
    },
    "group12": {
        "chairman": [{"name": "Shaykh Ibn Baz", "url": "/biography/binbaz"}],
        "deputy_chairman": [{"name": "Shaykh Abdul-Razzaq Afifi", "url": "/biography/afifi"}]
    },
    "group13": {
        "chairman": [{"name": "Shaykh Ibn Baz", "url": "/biography/binbaz"}],
        "members": [
            {"name": "Shaykh Abdul-Aziz Aal Al-Shaykh", "url": "/biography/abdulaziz"},
            {"name": "Shaykh Salih Al-Fawzan", "url": "/biography/fawzan"},
            {"name": "Shaykh Bakr Abu Zayd", "url": "/biography/bakr"}
        ]
    },
    "group14": {
        "chairman": [{"name": "Shaykh Abdul-Aziz ibn Baz", "url": "/biography/binbaz"}],
        "members": [
            {"name": "Shaykh Abdul-Aziz Aal Al-Shaykh", "url": "/biography/abdulaziz"},
            {"name": "Shaykh Abdullah ibn Ghudayyan", "url": "/biography/ghudayyan"},
            {"name": "Shaykh Salih Fawzan", "url": "/biography/fawzan"},
            {"name": "Shaykh Bakr Abu Zayd", "url": "/biography/bakr"}
        ]
    },
    "group15": {
        "chairman": [{"name": "Shaykh Ibn Baz", "url": "/biography/binbaz"}],
        "members": [
            {"name": "Shaykh Abdul-Aziz Aal Al-Shaykh", "url": "/biography/abdulaziz"},
            {"name": "Shaykh Salih Al-Fawzan", "url": "/biography/fawzan"}
        ]
    },
    "group16": {
        "chairman": [{"name": "Shaykh Abdul-Aziz Aal Al-Shaykh", "url": "/biography/abdulaziz"}],
        "deputy_chairman": [{"name": "Shaykh Abdul-Razzaq Al-Afifi", "url": "/biography/afifi"}],
        "members": [
            {"name": "Shaykh Abdullah ibn Ghudayyan", "url": "/biography/ghudayyan"},
            {"name": "Shaykh Salih Fawzan", "url": "/biography/fawzan"},
            {"name": "Shaykh Bakr Abu Zayd", "url": "/biography/bakr"}
        ]
    },
    "group17": {
        "chairman": [{"name": "Abdul-Aziz ibn Abdullah Aal Al-Shaykh", "url": "/biography/abdulaziz"}],
        "members": [
            {"name": "Shaykh Salih Fawzan", "url": "/biography/fawzan"},
            {"name": "Shaykh Bakr ibn Abdullah Abu Zayd", "url": "/biography/bakr"}
        ]
    },
    "group18": {
        "chairman": [{"name": "Shaykh Abdul-Aziz Ibn Baz", "url": "/biography/binbaz"}],
        "members": [
            {"name": "Shaykh Abdullah Ibn Ghudayyan", "url": "/biography/ghudayyan"},
            {"name": "Shaykh Abdullah Ibn Qa'ud", "url": "/biography/qaud"}
        ]
    },
    "group19": {
        "chairman": [{"name": "Shaykh Ibn Baz", "url": "/biography/binbaz"}],
        "deputy_chairman": [{"name": "Shaykh Abdul-Razzaq Afifi", "url": "/biography/afifi"}],
        "members": [
            {"name": "Shaykh Abdul-Aziz Aal Al-Shaykh", "url": "/biography/abdulaziz"},
            {"name": "Shaykh Salih Al-Fawzan", "url": "/biography/fawzan"},
            {"name": "Shaykh Bakr Abu Zayd", "url": "/biography/bakr"}
        ]
    },
    "group20": {
        "chairman": [{"name": "Shaykh Salih al-Fawzan", "url": "/biography/fawzan"}],
        "members": [
            {"name": "Shaykh Muhammad ibn hasan", "url": "/biography/muhammad-ibn-hasan"},
            {"name": "Shaykh Saad ibn Naseer", "url": "/biography/saad-ibn-naseer"},
            {"name": "Shaykh Abdul Salam ibn Abdullah", "url": "/biography/abdul-salam"}
        ]
    }
}

# Pre-normalize rules for lookup
NORMALIZED_RULES = {group: normalize_urls(rule) for group, rule in GROUP_RULES.items()}

def process_posts(root_dir):
    yaml_handler = YAML()
    yaml_handler.preserve_quotes = True
    
    updated_count = 0
    skipped_count = 0

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(('.md', '.markdown')):
                filepath = os.path.join(dirpath, filename)
                
                try:
                    # Parse post with python-frontmatter
                    post = frontmatter.load(filepath)
                    muftis_data = post.metadata.get('muftis')
                    
                    if not muftis_data:
                        skipped_count += 1
                        continue
                    
                    # Normalize post's muftis block for matching
                    normalized_post_muftis = normalize_urls(dict(muftis_data))
                    
                    # Find matching group
                    matched_group = None
                    for group_name, rule_data in NORMALIZED_RULES.items():
                        if normalized_post_muftis == rule_data:
                            matched_group = group_name
                            break
                    
                    if matched_group:
                        # Set the group flag to true without modifying anything else
                        post.metadata[matched_group] = True
                        
                        # Save file securely preserving original formatting via python-frontmatter + ruamel
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(frontmatter.dumps(post, handler=frontmatter.YAMLHandler()))
                            
                        print(f"Updated: {filepath} -> added {matched_group}: true")
                        updated_count += 1
                    else:
                        skipped_count += 1
                        
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

    print(f"\nFinished! Updated {updated_count} files. Skipped/Unmatched: {skipped_count} files.")

if __name__ == '__main__':
    # Adjust target directory as needed (e.g., '_posts/alifta')
    target_directory = '_posts/alifta'
    if os.path.exists(target_directory):
        process_posts(target_directory)
    else:
        print(f"Directory not found: {target_directory}. Please update the path variable.")