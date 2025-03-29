#NOT READY TO USE

import os
from PIL import Image

def convert_png_to_webp(directory, quality=80):
    """
    Converts all PNG images in a directory (and subdirectories) to WebP format.
    
    :param directory: Path to the image directory (e.g., "assets/images")
    :param quality: WebP quality (default 80 for a balance of quality and size)
    """
    converted = 0
    skipped = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".png"):
                png_path = os.path.join(root, file)
                webp_path = os.path.join(root, os.path.splitext(file)[0] + ".webp")

                # Skip conversion if the WebP file already exists
                if os.path.exists(webp_path):
                    print(f"🔄 Skipping (already exists): {webp_path}")
                    skipped += 1
                    continue
                
                try:
                    # Open the PNG image and convert to WebP
                    with Image.open(png_path) as img:
                        img.save(webp_path, "WEBP", quality=quality)
                    
                    print(f"✅ Converted: {png_path} -> {webp_path}")
                    converted += 1

                except Exception as e:
                    print(f"❌ Error processing {png_path}: {e}")

    print("\n🔹 Conversion Summary 🔹")
    print(f"✔️ {converted} images converted to WebP")
    print(f"🔄 {skipped} images were already in WebP format")

# Run the conversion script
if __name__ == "__main__":
    image_directory = "compress"  # Change if needed
    convert_png_to_webp(image_directory)