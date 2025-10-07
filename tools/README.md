# PNG to WebP Converter

A Python script to convert PNG images to WebP format for better web performance, with automatic backup functionality.

## Overview

This script helps optimize your Hugo site by:
- **Moving** PNG files to a safe backup location
- **Converting** them to WebP format (60-80% smaller file sizes)
- **Placing** WebP files in the original locations for Hugo to use
- **Preserving** folder structure and organization

## Prerequisites

Install the required Python package:

```bash
pip install Pillow
```

## Usage

### Basic Usage (Recommended)

Convert all PNG files in both `assets/images` and `static/images`:

```bash
cd tools
python png_to_webp.py
```

### Convert Specific Directory

Convert PNG files in a specific directory:

```bash
python png_to_webp.py /path/to/directory
```

## What It Does

### Step 1: Backup
- Creates timestamped backup folder: `png_backup/YYYYMMDD_HHMMSS/`
- **Moves** (not copies) all PNG files to backup location
- Preserves original folder structure

### Step 2: Convert
- Converts PNG files from backup to WebP format
- Places WebP files in original locations
- Optimizes quality (85% default) and size
- Resizes oversized images (max 1920px width)

### Step 3: Results
- Original PNG files: **Removed** from build directories
- WebP files: **Added** to build directories
- Backup: **Safely stored** outside build process

## Example Output

```
🔄 Converting PNG files in: C:\project\assets\images

📁 Moving PNG files to backup: png_backup/20251006_143022
📁 Moved: blog/screenshot.png
📁 Moved: maps/level1.png
📁 Moved 15 PNG files to png_backup/20251006_143022/images

✅ Converted: screenshot.png -> screenshot.webp
   💾 Size: 2.45MB -> 0.87MB (64.5% smaller)
✅ Converted: level1.png -> level1.webp
   💾 Size: 1.23MB -> 0.34MB (72.4% smaller)

🔹 Conversion Summary 🔹
✔️ 15 images converted to WebP
🔄 0 images were already in WebP format
💾 Total space saved: 12.34MB
```

## File Structure

### Before Conversion
```
assets/images/
├── screenshot.png
└── level1.png
static/images/
├── logo.png
└── banner.png
```

### After Conversion
```
assets/images/
├── screenshot.webp
└── level1.webp
static/images/
├── logo.webp
└── banner.webp

png_backup/20251006_143022/images/
├── screenshot.png (from assets)
├── level1.png (from assets)
├── logo.png (from static)
└── banner.png (from static)
```

## Configuration Options

You can modify these settings in the script:

- **Quality**: Default 85% (good balance of size/quality)
- **Max Width**: Default 1920px (resizes larger images)
- **Backup Location**: `png_backup/` (excluded from Git)

## Safety Features

✅ **Automatic Backup**: All PNGs moved to safe location before conversion  
✅ **Git Ignored**: Backup folder excluded from repository  
✅ **Hugo Ignored**: Backup folder excluded from site builds  
✅ **Timestamped**: Multiple backups won't overwrite each other  
✅ **Error Handling**: Failed conversions won't break the process  

## Performance Benefits

- **60-80% smaller** image file sizes
- **Faster page loads** for your Hugo site
- **Reduced bandwidth** usage
- **Better SEO** scores due to speed improvements

## Restoring from Backup

If you need to restore original PNG files:

1. Navigate to the backup folder: `png_backup/YYYYMMDD_HHMMSS/`
2. Copy files back to their original locations
3. Delete the corresponding WebP files if desired

## Troubleshooting

### "PIL cannot be imported"
```bash
pip install Pillow
```

### "Directory not found"
- Ensure you're running from the `tools/` directory
- Check that `assets/images/` or `static/images/` exists

### "Permission denied"
- Make sure no files are currently open/locked
- Run terminal as administrator if needed

## Notes

- The script skips conversion if WebP files already exist
- Transparent PNG images get a white background in WebP
- Large images are automatically resized to improve performance
- The backup folder is automatically added to `.gitignore`

## Integration with Hugo

After conversion, update your markdown files to reference `.webp` instead of `.png`:

```markdown
<!-- Before -->
![Image](screenshot.png)

<!-- After -->
![Image](screenshot.webp)
```

Or use the optimized image shortcode for automatic format selection:

```markdown
{{< img src="screenshot.webp" alt="Description" >}}
```