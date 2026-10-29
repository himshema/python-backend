import csv
import requests
import sys
if __name__ == "__main__":
    employee_id = sys.argv[1]
    user = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        )
    user_data = user.json()
    NAME = user_data.get("username")
    tasks = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )
    tasks = tasks.json()
    NUMBER_OF_TASKS = len(tasks)
    completed_tasks = [task for task in tasks if task.get("completed")]
    DONE_TASKS = len(completed_tasks)
    for task_titles in completed_tasks:
        task_title = task_titles.get("title")
    
    with open(f"{employee_id}.csv", "w", newline="") as file:
        writer = csv.writer(
            file,
            quoting=csv.QUOTE_ALL
        )
        for task in tasks:
            writer.writerow([
                employee_id,
                NAME,
                task.get("completed"),
                task.get("title")
            ])
            
