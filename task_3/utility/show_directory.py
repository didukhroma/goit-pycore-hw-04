from pathlib import Path
from utility import log_folder_name,log_file_name

def show_directory(folder_path,space_count):
      
    space_count += 1

    for path in Path(folder_path).iterdir():
        if path.name == ".venv" or path.name == ".git" or path.name == "__pycache__": continue

        if path.is_dir():
            log_folder_name(path.name,space_count)
            show_directory(path,space_count)
        elif path.is_file():
            log_file_name(path.name,space_count)
       