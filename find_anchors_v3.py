import os
import re

def find_anchors_in_markdown(directory):
    """
    Recursively scans all .ru.md files in the given directory and subdirectories.
    Finds and lists markdown links using anchors: 
    - [text](#anchor)
    - [text](/some/path/#anchor)
    """
    # Regex for both standard and path-based anchors
    anchor_pattern = re.compile(r'\[(.*?)\]\(([^)]+#([^)\s]+))\)')  
    results = {}

    for root, _, files in os.walk(directory):  # Recursively walk through directories
        for file in files:
            if file.endswith(".ru.md"):  # Only process Russian markdown files
                file_path = os.path.join(root, file)

                with open(file_path, "r", encoding="utf-8") as md_file:
                    content = md_file.readlines()

                for line_number, line in enumerate(content, 1):
                    matches = anchor_pattern.findall(line)
                    if matches:
                        if file_path not in results:
                            results[file_path] = []
                        for match in matches:
                            results[file_path].append(
                                (line_number, match[0], match[1], match[2])  
                                # (line number, link text, full path, anchor name)
                            )

    return results

def display_results(results):
    """
    Prints out the found anchors in a structured way.
    """
    if not results:
        print("❌ No anchored links found in .ru.md files.")
        return
    
    print("\n✅ **Anchored Links Found in .ru.md Files:**\n")
    for file, links in results.items():
        print(f"📂 **File:** {file}")
        for line_num, text, path, anchor in links:
            print(f"   - 📌 Line {line_num}: `[ {text} ]({path})` (Anchor: `#{anchor}`)")
        print("\n" + "-" * 50)

# Example usage:
directory_to_scan = "content"  # Change this to your directory path
results = find_anchors_in_markdown(directory_to_scan)
display_results(results)
