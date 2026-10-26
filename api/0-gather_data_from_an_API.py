import requests
import sys

employee_id = sys.argv[1]
user = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
user_data = user.json()
emplyee_name = user_data.get("name")
tasks = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
print(emplyee_name)
tasks-number = len(tasks.json())