import os
import re

CONTENT_DIR = "content"  # Adjust path as needed
AUTO_FIX = False  # Set to True to automatically fix errors in files

# Dictionary mapping masculine words to their correct feminine replacements
masculine_to_feminine = {
    r'\bбыл\b': 'была', r'\bсказал\b': 'сказала', r'\bдумал\b': 'думала', r'\bнаписал\b': 'написала',
    r'\bсоздал\b': 'создала', r'\bпотерял\b': 'потеряла', r'\bнашел\b': 'нашла', r'\bсделал\b': 'сделала',
    r'\bоткрыл\b': 'открыла', r'\bзакрыл\b': 'закрыла', r'\bузнал\b': 'узнала', r'\bпонял\b': 'поняла',
    r'\bпрочитал\b': 'прочитала', r'\bуверен\b': 'уверена', r'\bрад\b': 'рада', r'\bготов\b': 'готова',
    r'\bдобр\b': 'добра', r'\bсилен\b': 'сильна', r'\bумел\b': 'умела', r'\bобеспокоен\b': 'обеспокоена',
    r'\bвзволнован\b': 'взволнована', r'\bрешителен\b': 'решительна', r'\bоблегчён\b': 'облегчена',
    r'\bблагодарен\b': 'благодарна', r'\bгорд\b': 'горда', r'\bколебался\b': 'колебалась',
    r'\bуставший\b': 'уставшая', r'\bзапутался\b': 'запуталась',

    # Phrases
    r'\bбыл уверен\b': 'была уверена', r'\bбыл рад\b': 'была рада', r'\bбыл готов\b': 'была готова',
    r'\bбыл удивлен\b': 'была удивлена', r'\bбыл обеспокоен\b': 'была обеспокоена',
    r'\bбыл взволнован\b': 'была взволнована', r'\bбыл решителен\b': 'была решительна',
    r'\bбыл облегчён\b': 'была облегчена', r'\bбыл благодарен\b': 'была благодарна',
    r'\bбыл горд\b': 'была горда', r'\bбыл напуган\b': 'была напугана',
    r'\bбыл доволен\b': 'была довольна', r'\bбыл счастлив\b': 'была счастлива',
    r'\bбыл смущен\b': 'была смущена', r'\bбыл поражен\b': 'была поражена'
}

def check_and_fix_feminine_tone(file_path):
    """Checks for masculine terms and suggests or applies fixes in a given Russian translation file."""
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    found_errors = False
    for masculine, feminine in masculine_to_feminine.items():
        matches = re.findall(masculine, content)
        if matches:
            found_errors = True
            found_word = matches[0]  # Get the first matched word
            print(f"❌ {file_path}: Found '{found_word}' → Suggest '{feminine}'")

    if found_errors and AUTO_FIX:
        for masculine, feminine in masculine_to_feminine.items():
            content = re.sub(masculine, feminine, content)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"✅ Auto-fixed issues in {file_path}")

def find_and_check_ru_files(root_dir):
    """Recursively finds all .ru.md files in the content directory and checks them."""
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".ru.md"):
                file_path = os.path.join(subdir, file)
                check_and_fix_feminine_tone(file_path)

# Run the script
if __name__ == "__main__":
    find_and_check_ru_files(CONTENT_DIR)
