import os
import sys
import shutil
from datetime import datetime
from PIL import Image

def backup_png_files(source_directory, backup_root):
    """
    Move all PNG files to a backup directory structure
    
    :param source_directory: Source directory to move from
    :param backup_root: Root backup directory
    :return: Number of files moved
    """
    moved = 0
    
    for root, _, files in os.walk(source_directory):
        for file in files:
            if file.lower().endswith(".png"):
                png_path = os.path.join(root, file)
                
                # Create relative path from source directory
                rel_path = os.path.relpath(png_path, source_directory)
                backup_path = os.path.join(backup_root, rel_path)
                
                # Create backup directory if it doesn't exist
                backup_dir = os.path.dirname(backup_path)
                os.makedirs(backup_dir, exist_ok=True)
                
                # Move the file if it doesn't already exist in backup
                if not os.path.exists(backup_path):
                    shutil.move(png_path, backup_path)
                    print(f"📁 Moved: {rel_path}")
                    moved += 1
                else:
                    print(f"🔄 Backup exists: {rel_path}")
    
    return moved

def convert_png_to_webp(directory, quality=85, max_width=1920, backup_dir=None):
    """
    Converts all PNG images in a directory (and subdirectories) to WebP format.
    
    :param directory: Path to the image directory (e.g., "assets/images")
    :param quality: WebP quality (default 85 for good balance of quality and size)
    :param max_width: Maximum width to resize images to (default 1920px)
    :param backup_dir: Directory to move PNG files to before conversion
    """
    converted = 0
    skipped = 0
    total_savings = 0

    # Move PNG files to backup directory if specified
    if backup_dir:
        print(f"📁 Moving PNG files to backup: {backup_dir}")
        backup_subdir = os.path.join(backup_dir, os.path.basename(directory))
        moved = backup_png_files(directory, backup_subdir)
        print(f"📁 Moved {moved} PNG files to {backup_subdir}\n")
        
        # Now convert from the backup directory
        conversion_source = backup_subdir
    else:
        conversion_source = directory

    for root, _, files in os.walk(conversion_source):
        for file in files:
            if file.lower().endswith(".png"):
                png_path = os.path.join(root, file)
                
                # Determine where to place the WebP file
                if backup_dir:
                    # Calculate the relative path and place WebP in original location
                    rel_path = os.path.relpath(png_path, conversion_source)
                    webp_path = os.path.join(directory, os.path.splitext(rel_path)[0] + ".webp")
                    # Create directory structure if needed
                    os.makedirs(os.path.dirname(webp_path), exist_ok=True)
                else:
                    webp_path = os.path.join(root, os.path.splitext(file)[0] + ".webp")

                # Skip conversion if the WebP file already exists
                if os.path.exists(webp_path):
                    print(f"🔄 Skipping (already exists): {os.path.basename(webp_path)}")
                    skipped += 1
                    continue
                
                try:
                    original_size = os.path.getsize(png_path)
                    
                    # Open the PNG image and convert to WebP
                    with Image.open(png_path) as img:
                        # Resize if image is too large
                        if img.width > max_width:
                            ratio = max_width / img.width
                            new_height = int(img.height * ratio)
                            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                            print(f"📏 Resized {os.path.basename(png_path)} to {max_width}x{new_height}")
                        
                        # Convert to RGB if necessary (WebP doesn't support some PNG modes)
                        if img.mode in ('RGBA', 'LA', 'P'):
                            # Create a white background for transparent images
                            background = Image.new('RGB', img.size, (255, 255, 255))
                            if img.mode == 'P':
                                img = img.convert('RGBA')
                            background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
                            img = background
                        elif img.mode != 'RGB':
                            img = img.convert('RGB')
                        
                        # Save as WebP
                        img.save(webp_path, "WEBP", quality=quality, optimize=True)
                    
                    new_size = os.path.getsize(webp_path)
                    savings = original_size - new_size
                    total_savings += savings
                    savings_percent = (savings / original_size) * 100
                    
                    print(f"✅ Converted: {os.path.basename(png_path)} -> {os.path.basename(webp_path)}")
                    print(f"   💾 Size: {original_size/1024/1024:.2f}MB -> {new_size/1024/1024:.2f}MB ({savings_percent:.1f}% smaller)")
                    converted += 1

                except Exception as e:
                    print(f"❌ Error processing {png_path}: {e}")

    print("\n🔹 Conversion Summary 🔹")
    print(f"✔️ {converted} images converted to WebP")
    print(f"🔄 {skipped} images were already in WebP format")
    print(f"💾 Total space saved: {total_savings/1024/1024:.2f}MB")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    # Create backup directory with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = os.path.join(project_root, "png_backup", timestamp)
    
    if len(sys.argv) > 1:
        # Single directory specified
        image_directory = sys.argv[1]
        if not os.path.exists(image_directory):
            print(f"❌ Directory not found: {image_directory}")
            print("Usage: python png_to_webp.py [directory_path]")
            return
        
        print(f"🔄 Converting PNG files in: {image_directory}")
        convert_png_to_webp(image_directory, backup_dir=backup_dir)
    else:
        # Process both assets/images and static/images directories
        image_directories = [
            os.path.join(project_root, "assets", "images"),
            os.path.join(project_root, "static", "images")
        ]
        
        processed_any = False
        for image_directory in image_directories:
            if os.path.exists(image_directory):
                print(f"\n🔄 Converting PNG files in: {image_directory}")
                convert_png_to_webp(image_directory, backup_dir=backup_dir)
                processed_any = True
            else:
                print(f"⚠️  Directory not found (skipping): {image_directory}")
        
        if not processed_any:
            print("❌ No image directories found!")
            print("Usage: python png_to_webp.py [directory_path]")
            return
        
        if processed_any:
            print(f"\n📁 All PNG files moved to backup: {backup_dir}")
            print("✅ WebP files created in original locations for Hugo to use")
            print("💡 The backup folder is excluded from Hugo builds and Git")
            print("💡 You can restore PNGs from backup if needed")

# Run the conversion script
if __name__ == "__main__":
    main()