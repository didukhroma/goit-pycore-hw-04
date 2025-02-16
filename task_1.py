def total_salary(path:str)->int:
    try:
        with open(path) as (fh):
            all_file = [int(el.strip().split(',')[1]) for el in fh.readlines()]
            total = sum(all_file)
            average = int(total/len( all_file))

        return (total,average)
    except Exception as err:
        print(f"Error: {err}")
        return (0,0)


path="task_1.txt"

total,average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")