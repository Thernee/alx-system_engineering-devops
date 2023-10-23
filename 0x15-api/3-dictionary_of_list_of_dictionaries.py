#!/usr/bin/python3
"""Return info about employee's TODO list progress"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(f"{url}/users").json()

    todo_data = {}
    for user in users:
        user_id = user["id"]
        username = user["username"]
        todos = requests.get(f"{url}/todos", params={"userId": user_id}).json()
        todo_list = [{
            "task": todo["title"],
            "completed": todo["completed"],
            "username": username
        } for todo in todos]

        todo_data[user_id] = todo_list

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(todo_data, jsonfile)
