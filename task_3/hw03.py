import sys
from pathlib import Path

from utility import show_directory,log_folder_name

def main():
    try:
        path = sys.argv[1]
        directory = Path(path)
        if not directory.exists():
            raise Exception("Directory does not exist. Please check the path.")
        
        log_folder_name(directory.name,space_count=0)
        show_directory(path,space_count=1)
        
    except Exception as err:
        print(f"Error: {err}")   

  

main()    