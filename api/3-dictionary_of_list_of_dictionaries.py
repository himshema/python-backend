import json
import requests
import sys
""" Retrieve data, and export into a .json file in format of list of dictionaries"""

if __name__ == "__main__":
    users = requests.get(
        f"https://jsonplaceholder.typicode.com/users"
    )
    tasks_lists = {}
    users = users.json()
    for user in users:
        user_id = user.get("id")
        user_data = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
        )
        user_data = user_data.json()
        username = user_data.get("username")
        tasks = requests.get(
            f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        )
        tasks = tasks.json()
        user_tasks = []
        for task in tasks:
            user_tasks.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })
        tasks_lists[str(user_id)] = user_tasks
    with open("todo_all_employees.json", "w") as file:
        json.dump(tasks_lists, file)