from pathlib import Path

current_dir = Path(__file__).parent
def total_salary(path:str)->int:
    try:
        with open(current_dir / path,"r", encoding="utf-8") as fh:
            all_salaries = [int(el.strip().split(',')[1]) for el in fh.readlines()]
            total = sum(all_salaries)
            average = int(total/len( all_salaries))

        return (total,average)
    except Exception as err:
        print(f"Error: {err}")
        return (0,0)


path="task_1.txt"

total,average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")