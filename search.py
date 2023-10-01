import os
import glob
import markdown_it

from dotenv import load_dotenv
import os

load_dotenv()
load_dotenv(".env.local")

folder_path = os.environ['target_path']
search_string = os.environ['find_text']

md = markdown_it.MarkdownIt()

def find_lines_with_string(file_path, search_string):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line_number, line in enumerate(lines, start=1):
            if search_string in line:
                print(f"{file_path} - Line {line_number}: {line.strip()}")

def search_in_markdown_files(folder_path, search_string):
    markdown_files = glob.glob(os.path.join(folder_path, "*.md"))
    for file_path in markdown_files:
        find_lines_with_string(file_path, search_string)

if __name__ == "__main__":
    search_in_markdown_files(folder_path, search_string)