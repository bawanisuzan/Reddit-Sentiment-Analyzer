import nltk 
import os

download_dir = "nltk_data"
if not os.path.exists(download_dir):
    print("Model not found. Downloading model...")
    nltk.download('vader_lexicon', download_dir=download_dir)
    print("Model downloaded successfully...")
else:
    print(f"Model already exits in the directory: {download_dir}")
