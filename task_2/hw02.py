from pathlib import Path 
current_dir = Path(__file__).parent

def get_cats_info(path):
    try:
           
        with open(current_dir / path,"r", encoding="utf-8") as file_path:
            result = [{"id":cat[0],"name":cat[1],"age":cat[2]} for cat in [el.strip().split(",") for el in file_path.readlines()]]
            
            return result
    except Exception as err:
        print(f"Error: {err}")
        return []
        
    

path = "task_2.txt"

cats_info = get_cats_info(path)
print(cats_info)