def get_cats_info(path):
    try:        
        with open(path) as fh:
            all_file = [el.strip().split(",") for el in fh.readlines()]
            result = [{"id":cat[0],"name":cat[1],"age":cat[2]} for cat in all_file]
            return result
    except Exception as err:
        print(f"Error: {err}")
        return []
        
    

path = "task_2.txt"

cats_info = get_cats_info(path)
print(cats_info)