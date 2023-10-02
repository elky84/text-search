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
        current_heading_level = 0
        stored_lines_and_numbers = []
        found = False
        for line_number, line in enumerate(lines, start=1):
            if line.startswith("#"):
                heading_level = len(line.split()[0])
                if found and heading_level <= current_heading_level:
                    break

                current_heading_level = heading_level
                stored_lines_and_numbers = []

            if search_string in line:
                for stored_line, stored_line_number in stored_lines_and_numbers:
                    print(f"{file_path} - Line {stored_line_number}: {stored_line}")
                stored_lines_and_numbers = []
                found = True

            if found:
                print(f"{file_path} - Line {line_number}: {line.strip()}")
                if current_heading_level == 0:
                    found = False
            elif current_heading_level > 0:
                stored_lines_and_numbers.append((line.strip(), line_number))

def search_in_markdown_files(folder_path, search_string):
    markdown_files = glob.glob(os.path.join(folder_path, "*.md"))
    for file_path in markdown_files:
        find_lines_with_string(file_path, search_string)

if __name__ == "__main__":
    search_in_markdown_files(folder_path, search_string)