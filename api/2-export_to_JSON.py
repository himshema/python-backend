import json
import requests
import sys
""" Module to retrieve data from the API,
and then export the data into a .json file
"""
if __name__ == "__main__":
    employee_id = sys.argv[1]
    user_data = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    user_data = user_data.json()
    user = user_data.get("username")
    tasks = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )
    tasks = tasks.json()
    tasks_list = []
    for task in tasks:
        title = task.get("title")
        TASK_COMPLETED_STATUS = task.get("completed")        
        tasks_list.append({
            "task":title,
            "completed":TASK_COMPLETED_STATUS,
            "username":user
        })
    employee = {
        f"{employee_id}":tasks_list
    }
    print(employee)
    with open(f"{employee_id}.json", "w") as file:
        json.dump(employee, file)
        print("----------json file created!!!!!!")