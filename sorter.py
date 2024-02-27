import os
import shutil
from langdetect import detect
import chardet 
import tika 
from tika import parser

tika.initVM() 

folder_path = "C:/Users/Administrator/Desktop/smistalibri/file"

def detect_and_move_file(file_path):  # Renamed the function for clarity
    """Detects language of an EPUB or PDF file and moves it appropriately."""
    try:
        if file_path.endswith(".epub"):
            with open(file_path, 'rb') as f: 
                text_sample = tika.parser.from_file(file_path)['content']
        elif file_path.endswith(".pdf"):
            parsed_pdf = parser.from_file(file_path) 
            text_sample = parsed_pdf['content']
        else:
            print(f"Unsupported file type: {file_path}")
            return  # Skip unsupported files

        # Attempt language detection, prioritize langdetect
        try:
            language = detect(text_sample) 
        except Exception:  
            # Fallback to chardet for encoding hints
            rawdata = open(file_path, 'rb').read()
            result = chardet.detect(rawdata)
            language = result['encoding']  # Sometimes encoding reflects language

        print(f"Detected language: {language}")

        os.makedirs(os.path.join(folder_path, language), exist_ok=True)
        destination = os.path.join(folder_path, language, os.path.basename(file_path))
        shutil.move(file_path, destination)

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Process all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    detect_and_move_file(file_path) 
