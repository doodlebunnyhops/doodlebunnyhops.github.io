import os
import re
import argparse

def extract_title_length(directory, extension, only_dir, ignored_folders):
    """
    Extracts 'title' field from front matter in Markdown files and checks its length.

    :param directory: Directory to scan for Markdown files
    :param extension: File extension to filter (.md or .ru.md)
    :param only_dir: If set, only scan this directory and its subdirectories
    :param ignored_folders: List of folders to ignore
    :return: Dictionary {file_path: {"title": title, "length": length}}
    """
    title_pattern = re.compile(r'^title:\s*"(.*?)"', re.MULTILINE)  # Match title in front matter
    title_lengths = {}

    for root, _, files in os.walk(directory):
        # Normalize paths for cross-platform compatibility
        normalized_root = os.path.normpath(root)

        # If `--only-dir` is provided, ignore all other directories
        if only_dir:
            normalized_only_dir = os.path.normpath(only_dir)
            if not normalized_root.startswith(normalized_only_dir):
                continue

        # Skip ignored folders
        if ignored_folders and any(os.path.normpath(ignored) in normalized_root for ignored in ignored_folders):
            continue

        for file in files:
            # Extract full extension correctly
            filename_parts = file.split(".")
            full_extension = "." + ".".join(filename_parts[1:]) if len(filename_parts) > 1 else ""

            if full_extension == extension:
                file_path = os.path.join(root, file)

                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                title_match = title_pattern.search(content)
                if title_match:
                    title = title_match.group(1)
                    title_length = len(title)
                    title_lengths[file_path] = {"title": title, "length": title_length}

    return title_lengths


def validate_titles(directory, extension, only_dir, ignored_folders):
    """
    Checks if title length in Markdown files is within the recommended range (50-60 chars).

    :param directory: Directory to scan for Markdown files
    :param extension: File extension to filter (.md or .ru.md)
    :param only_dir: If set, only scan this directory and its subdirectories
    :param ignored_folders: List of folders to ignore
    """
    print(f"\n🔍 Evaluating 'title' length in {extension} files...\n")

    title_data = extract_title_length(directory, extension, only_dir, ignored_folders)
    too_short = []
    too_long = []

    for file, data in title_data.items():
        title, length = data["title"], data["length"]
        if length < 50:
            too_short.append((file, title, length, 50 - length))
        elif length > 60:
            too_long.append((file, title, length, length - 60))

    # Display results
    for file, title, length, diff in too_short:
        print(f"📂 File: {file}")
        print(f"   🏷️ Title: \"{title}\"")
        print(f"   🔢 Length: {length} characters")
        print(f"   ⚠️ Too short! Needs at least {diff} more characters.\n")

    for file, title, length, diff in too_long:
        print(f"📂 File: {file}")
        print(f"   🏷️ Title: \"{title}\"")
        print(f"   🔢 Length: {length} characters")
        print(f"   ⚠️ Too long! Reduce by {diff} characters.\n")

    if not too_short and not too_long:
        print("✅ All titles are within the correct length range (50-60 characters)!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check 'title' length in Markdown front matter.")
    parser.add_argument("directory", help="Path to the content directory")
    parser.add_argument("extension", help="Markdown file extension to scan (.md or .ru.md)", choices=[".md", ".ru.md"])
    parser.add_argument("--only-dir", help="Scan only this directory and its subdirectories")
    parser.add_argument("--ignore", nargs="*", default=[], help="List of folders to ignore (space-separated)")

    args = parser.parse_args()

    target_dir = os.path.normpath(args.directory)
    file_extension = args.extension
    only_directory = os.path.normpath(args.only_dir) if args.only_dir else None
    ignored_folders = [os.path.normpath(folder) for folder in args.ignore]

    if not os.path.isdir(target_dir):
        print(f"❌ Error: Directory '{target_dir}' not found.")
        exit(1)

    validate_titles(target_dir, file_extension, only_directory, ignored_folders)
