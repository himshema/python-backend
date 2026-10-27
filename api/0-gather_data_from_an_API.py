import requests
import sys

employee_id = sys.argv[1]
user = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
user_data = user.json()
EMPLOYEE_NAME = user_data.get("name")
tasks = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
tasks = tasks.json()
TOTAL_NUMBER_OF_TASKS = len(tasks)
completed_tasks = [task for task in tasks if task.get("completed")]
NUMBER_OF_DONE_TASKS = len(completed_tasks)
print(f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS})")
for task_titles in completed_tasks:
    task_title = task_titles.get("title")
    print(f"\t{task_title}")

