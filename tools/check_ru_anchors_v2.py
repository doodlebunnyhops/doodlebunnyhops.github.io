import os
import re
import unicodedata

def extract_headings(file_path):
    """Extracts markdown headings from a file as potential anchors."""
    headings = set()
    heading_pattern = re.compile(r'^(#+)\s+(.+)', re.MULTILINE)
    
    extracted_headings = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for match in heading_pattern.finditer(f.read()):
                heading_text = match.group(2).strip()
                # Normalize and replace spaces with dashes, keeping Cyrillic characters intact
                anchor = unicodedata.normalize('NFKC', heading_text)
                anchor = re.sub(r'\s+', '-', anchor)  # Replace spaces with dashes
                anchor = re.sub(r'[^\wа-яА-ЯёЁ\-]', '', anchor, flags=re.UNICODE)  # Preserve Cyrillic characters
                extracted_headings.add(anchor.lower())
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

    print("-----------------------------------------")
    print(f"File path: {file_path}")
    print(f"Extracted headings: {extracted_headings}")
    print("-----------------------------------------")
    
    return extracted_headings

def resolve_target_path(content_dir, source_file, target_link):
    """Resolves the full path of a linked file based on its relative position and ensures only the correct language file is checked."""
    source_dir = os.path.dirname(source_file)

    # Only process Russian files
    # if not source_file.endswith(".ru.md"):
    #     return None
    
    is_russian = source_file.endswith(".ru.md")

    print("-----------------------------------------")
    print(f"Target link: {target_link}")
    print(f"Source file: {source_file}")
    print(f"Is Russian: {is_russian}")
    
    # Handle absolute links (assuming /content root)
    if target_link.startswith("/"):
        target_path = os.path.normpath(os.path.join(content_dir, target_link.lstrip("/")))
    else:
        target_path = os.path.normpath(os.path.join(source_dir, target_link))

    print(f"Target path: ./{target_path}.ru.md")
    # Only check for the correct language version
    if is_russian:
        if os.path.exists("./" + target_path + ".ru.md"):
            full_path = "./" + target_path + ".ru.md"
            print(f"Full path: {full_path}")
            print("-----------------------------------------")
            return full_path
        
            
    print(f"Full Path: {None}")
    print("-----------------------------------------")
    
    return None

def check_anchors_in_ru_files(content_dir):
    """Scans .ru.md files for links with anchors and verifies their validity, ensuring correct language matching."""
    anchor_pattern = re.compile(r'\[.*?\]\((.*?)#(.*?)\)')
    issues = []
    
    for root, _, files in os.walk(content_dir):
        for file in files:
            if file.endswith(".ru.md"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    matches = anchor_pattern.findall(content)
                    
                    for link, anchor in matches:
                        if link:
                            target_path = resolve_target_path(content_dir, file_path, link)
                            
                            if target_path == None:
                                issues.append(f"Broken link in {file_path}: \n\tLink:\t{link} \n\tAnchor:\t{anchor} \n\tTarget Path:\t{target_path}")
                            elif os.path.exists(target_path) == False:
                                issues.append(f"Broken link in {file_path}: \n\tLink:\t{link} \n\tAnchor:\t{anchor} \n\tTarget Path:\t{target_path}")
                            else:
                                print(f"Link: {link}#{anchor}")
                                print(f"Target path: {target_path}")
                                print(f"Extracting headings from {target_path}")
                                headings = extract_headings(target_path)
                                if anchor.lower() not in headings:
                                    issues.append(
                                        f"Invalid anchor in {file_path}: {link}#{anchor}\n"
                                        f"    → Target file: {target_path}\n"
                                        f"    → Expected anchors: {', '.join(headings) if headings else 'No headings found'}\n"
                                    )
    
    if issues:
        print("Anchor issues found:")
        for issue in issues:
            print(issue)
    else:
        print("No anchor issues found.")
    
    return issues

if __name__ == "__main__":
    content_directory = "./content"  # Adjust as needed
    check_anchors_in_ru_files(content_directory)
