import os
import shutil
from langdetect import detect
import chardet  
import tika  
from tika import parser
tika.initVM()  
#change with source folder path
folder_path = "C:/Users/Administrator/Desktop/smistalibri/file"

def detect_and_move_epub(file_path):
    """Detects language of an EPUB file and moves it to the appropriate folder."""
    with open(file_path, 'rb') as f:  
        text_sample = tika.parser.from_file(file_path)['content']
        
    try:
        language = detect(text_sample)
    except Exception:
        language = "unknown"  # Handle cases where language detection fails
    print ("lenguage: "+language)
    # Create language folders if they don't exist
    os.makedirs(os.path.join(folder_path, language), exist_ok=True)

    # Move the file
    destination = os.path.join(folder_path, language, os.path.basename(file_path))
    shutil.move(file_path, destination)

# Process all EPUB files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".epub"):
        file_path = os.path.join(folder_path, filename)
        detect_and_move_epub(file_path)
