import os
import re
import argparse

def extract_links_with_anchors(directory, extension):
    """ Extracts all links with anchors (#) from Markdown files in the given directory. """
    anchor_links = {}
    link_pattern = re.compile(r'\[.*?\]\((.*?)\)')  # Match [text](link)

    for root, _, files in os.walk(directory):
        for file in files:
            filename_parts = file.split(".")
            full_extension = "." + ".".join(filename_parts[1:]) if len(filename_parts) > 1 else ""

            if full_extension == extension:
                file_path = os.path.join(root, file).replace("\\", "/")  # Normalize path
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                links = link_pattern.findall(content)
                anchors = [link for link in links if "#" in link and not link.startswith("#")]

                if anchors:
                    anchor_links[file_path] = anchors

    return anchor_links


def resolve_markdown_file(link_path, extension):
    """ Resolves the corresponding markdown file from an absolute or relative path. """
    
    content_root = "content"  # Define the base content directory

    if link_path.startswith("/"):
        link_path = link_path.lstrip("/")
        if link_path.endswith("/"):
            link_path = link_path.rstrip("/")
        md_file_path = os.path.join(content_root, link_path + extension)  # Search in content root
    else:
        if link_path.endswith("/"):
            link_path = link_path.rstrip("/")
        md_file_path = os.path.abspath(os.path.join(content_root, link_path))

    resolved_path = md_file_path.replace("\\", "/")  # Normalize path
    print(f"Resolving markdown file: {link_path} -> {resolved_path}")  # Debugging print
    return resolved_path if os.path.exists(resolved_path) else None


# def extract_headers(file_path):
#     """ Extracts all headers (### Header) from a specific Markdown file. """
#     headers = []
#     header_pattern = re.compile(r'^(#{1,6})\s+(.+)', re.MULTILINE)  # Match # Header

#     if os.path.exists(file_path):
#         with open(file_path, "r", encoding="utf-8") as f:
#             content = f.read()

#         # Convert headers to anchor format (supports English & Russian)
#         found_headers = header_pattern.findall(content)
#         headers = [
#             f"#{re.sub(r'[^a-zA-Zа-яА-Я0-9-_ ]', '', title).strip().replace(' ', '-').lower()}"
#             for _, title in found_headers
#         ]

#     return headers

def extract_headers(file_path):
    """ Extracts all headers (### Header) from a specific Markdown file. """
    headers = []
    header_pattern = re.compile(r'^(#{1,6})\s+(.+)', re.MULTILINE)  # Match # Header

    if not os.path.isfile(file_path):  # ✅ Prevent trying to open directories
        print(f"⚠️ Skipping non-file: {file_path}")  # Debugging print
        return headers  # Return empty list so it doesn’t break validation

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Convert headers to anchor format (supports English & Russian)
        found_headers = header_pattern.findall(content)

        #this one adds -- if spaces at end
        # headers = [
        #     f"#{re.sub(r'[^a-zA-Zа-яА-Я0-9-_ ]', '', title).replace(' ', '-').lower()}"
        #     for _, title in found_headers
        # ]
        headers = [
            f"#{re.sub(r'[^a-zA-Zа-яА-Я0-9-_ ]', '', title).rstrip().replace(' ', '-').lower()}"
            for _, title in found_headers
        ]
    except PermissionError:
        print(f"❌ Permission denied: {file_path}")  # Prevent crash and log error
        return headers

    return headers


def validate_anchors(directory, extension):
    """ Checks if anchors in Markdown links exist in the corresponding files. """
    print(f"\n🔍 Validating anchor links in {extension} files...\n")

    # Step 1: Extract links only from files in the provided directory
    links_with_anchors = extract_links_with_anchors(directory, extension)

    missing_anchors = {}

    # Step 2: Validate each link against its target file & anchor
    for file, links in links_with_anchors.items():
        print(f"\n🔗 Checking links in {file}:\n")
        for link in links:
            file_path, anchor = link.split("#", 1) if "#" in link else (link, None)
            resolved_file = resolve_markdown_file(file_path, extension)  # Handle absolute & relative paths

            if resolved_file:
                headers_in_file = extract_headers(resolved_file)  # Extract only for the target file

                formatted_anchor = f"#{anchor.lower().replace(' ', '-')}"
                print(f"  🔍 Checking if {formatted_anchor} exists in {resolved_file}...")  # Debugging print

                if formatted_anchor not in headers_in_file:
                    print(f"  ❌ MISSING: {formatted_anchor} in {resolved_file}")
                    if file not in missing_anchors:
                        missing_anchors[file] = []
                    missing_anchors[file].append((link, resolved_file, headers_in_file))
                else:
                    print(f"  ✅ FOUND: {formatted_anchor} in {resolved_file}")

    # Step 3: Print results in a structured format
    print("\n📝 Results:\n")
    if missing_anchors:
        print("❌ Missing Anchors Found:\n")
        for file, missing in missing_anchors.items():
            print(f"📂 File: {file}")
            for link, expected_file, found_headers in missing:
                print(f"   🔗 Link: {link}")
                print(f"   📄 Expected in: {expected_file}")
                print(f"   📝 Found anchors in this file:")
                for header in found_headers:
                    print(f"     {header}")
            print("")  # Blank line for readability
    else:
        print("✅ All anchor links are valid!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check if Markdown anchor links exist in corresponding files.")
    parser.add_argument("directory", help="Path to the content directory (only checks links in this dir)")
    parser.add_argument("extension", help="Markdown file extension to scan (.md or .ru.md)", choices=[".md", ".ru.md"])

    args = parser.parse_args()
    target_dir = args.directory
    file_extension = args.extension

    if not os.path.isdir(target_dir):
        print(f"❌ Error: Directory '{target_dir}' not found.")
        exit(1)

    validate_anchors(target_dir, file_extension)
