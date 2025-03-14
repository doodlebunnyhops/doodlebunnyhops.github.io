import os

def find_untranslated_pages(content_dir, ignore_dirs=None):
    if ignore_dirs is None:
        ignore_dirs = {"blog", "story"}  # Directories to ignore
    
    english_pages = set()
    russian_pages = set()
    
    for root, _, files in os.walk(content_dir):
        relative_root = os.path.relpath(root, content_dir)
        if any(relative_root.startswith(ignore) for ignore in ignore_dirs):
            continue
        
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, content_dir)
                
                if relative_path.endswith(".ru.md"):
                    russian_pages.add(relative_path[:-6])  # Remove '.ru.md'
                else:
                    english_pages.add(relative_path[:-3])  # Remove '.md'
    
    untranslated = english_pages - russian_pages
    
    print("Untranslated pages:")
    for page in sorted(untranslated):
        print(f"{page}.md")
    
    return untranslated

if __name__ == "__main__":
    content_directory = "./content"  # Adjust as needed
    untranslated_pages = find_untranslated_pages(content_directory)
