import os
import re
import argparse

def find_anchor_links_in_markdown(directory, extension):
    """
    Scans all markdown files in a given directory with the specified extension 
    and extracts links that contain anchors (#).
    
    :param directory: Path to the content directory
    :param extension: File extension to scan (e.g., .md or .ru.md)
    :return: Dictionary with filenames as keys and lists of anchor links as values
    """
    anchor_links = {}

    # Regex pattern to find Markdown links: [text](link)
    link_pattern = re.compile(r'\[.*?\]\((.*?)\)')
    # print(f"Looking for links with anchors in {extension} files...\n")  # Debugging print

    for root, _, files in os.walk(directory):
        for file in files:
            # Extract full extension for files like `.ru.md`
            filename_parts = file.split(".")
            full_extension = "." + ".".join(filename_parts[1:]) if len(filename_parts) > 1 else ""

            # print(f"Checking file: {file} (Detected extension: {full_extension})")  # Debugging print

            # Ensure full extension matches exactly
            if full_extension == extension:
                # print(f"Matched {extension} file: {file}")  # Debugging print
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Find all links in the markdown file
                links = link_pattern.findall(content)
                anchors = [link for link in links if "#" in link and not link.startswith("#")]  # Filter links with anchors
                
                if anchors:
                    anchor_links[file_path] = anchors

    return anchor_links

if __name__ == "__main__":
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Find links with anchors in Markdown files within a given directory.")
    parser.add_argument("directory", help="Path to the directory containing Markdown files (e.g., content/blog/)")
    parser.add_argument("extension", help="Markdown file extension to scan (e.g., .md or .ru.md)", choices=[".md", ".ru.md"])
    
    args = parser.parse_args()
    target_dir = args.directory
    file_extension = args.extension

    # Ensure the directory exists
    if not os.path.isdir(target_dir):
        print(f"Error: Directory '{target_dir}' not found.")
        exit(1)

    anchor_links = find_anchor_links_in_markdown(target_dir, file_extension)

    # Print results
    if anchor_links:
        print("\nLinks with Anchors Found in Markdown Files:\n")
        for file, links in anchor_links.items():
            print(f"{file}:")
            for link in links:
                print(f"  - {link}")
    else:
        print(f"No links with anchors found in {file_extension} files.")
