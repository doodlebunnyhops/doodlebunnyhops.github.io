import os
import re

# Define the root directory where your content is stored
CONTENT_DIR = "content"

# Define common masculine past-tense verbs that should be in feminine form
masculine_patterns = [
    r'\bбыл\b', r'\bсказал\b', r'\bдумал\b', r'\bнаписал\b', r'\bсоздал\b', 
    r'\bпотерял\b', r'\bнашел\b', r'\bсделал\b', r'\bоткрыл\b', r'\bзакрыл\b', 
    r'\bузнал\b', r'\bпонял\b', r'\bпрочитал\b', 
    r'\bуверен\b', r'\bрад\b', r'\bготов\b', r'\bдобр\b', r'\bсилен\b', r'\bумел\b', 

    # Phrases with "был" (past tense "was" in masculine)
    r'\bбыл уверен\b', r'\bбыл рад\b', r'\bбыл готов\b', r'\bбыл удивлен\b', 
    r'\bбыл обеспокоен\b', r'\bбыл взволнован\b', r'\bбыл решителен\b', 
    r'\bбыл облегчён\b', r'\bбыл благодарен\b', r'\bбыл горд\b', 

    # Additional verbs found in markdown files
    r'\bзнал\b', r'\bвидел\b', r'\bпонимал\b', r'\bстал\b', r'\bиспользовал\b',
    r'\bначал\b', r'\bразобрался\b', r'\bспросил\b', r'\bответил\b', r'\bнажал\b', 
    r'\bсмог\b', r'\bхотел\b', r'\bпробовал\b', r'\bрешил\b',

    # Adjectives and states found in markdown files
    r'\bобеспокоен\b', r'\bвзволнован\b', r'\bрешителен\b', r'\bоблегчён\b', 
    r'\bблагодарен\b', r'\bгорд\b', r'\bколебался\b', r'\bуставший\b', r'\bзапутался\b',
    
    # Common phrases with gendered verbs
    r'\bбыл заинтересован\b', r'\bбыл уверен в себе\b', r'\bбыл напуган\b', 
    r'\bбыл доволен\b', r'\bбыл счастлив\b', r'\bбыл смущен\b', r'\bбыл поражен\b'
]

def check_feminine_tone(file_path):
    """Checks for masculine verb usage in a given Russian translation file."""
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    errors = []
    for pattern in masculine_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            errors.append(f"❌ {file_path}: Found masculine terms -> {', '.join(set(matches))}")

    if errors:
        for error in errors:
            print(error)
    else:
        print(f"✅ {file_path}: No masculine forms detected.")

def find_and_check_ru_files(root_dir):
    """Recursively finds all .ru.md files in the content directory and checks them."""
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".ru.md"):
                file_path = os.path.join(subdir, file)
                check_feminine_tone(file_path)

# Run the script
if __name__ == "__main__":
    find_and_check_ru_files(CONTENT_DIR)
