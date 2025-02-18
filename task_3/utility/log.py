from colorama import Fore

space='\t'

def log_folder_name(folder_name,space_count):    
    
    print(f"{Fore.BLUE} {space_count * space + folder_name+'/'} {Fore.RESET} ")

def log_file_name(file_name,space_count):
    print(f"{Fore.GREEN} {space_count * space + file_name} {Fore.RESET} ")