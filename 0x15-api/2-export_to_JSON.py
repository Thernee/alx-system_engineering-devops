#!/usr/bin/python3
"""Return info about employee's TODO list progress"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    baseUrl = 'https://jsonplaceholder.typicode.com/users'
    fullUrl = f"{baseUrl}/{argv[1]}"

    user = requests.get(fullUrl).json()
    name = user.get('username')

    user_id = argv[1]
    todosUrl = f"{fullUrl}/todos"
    todos = requests.get(todosUrl).json()

    with open(f"{user_id}.json", 'w') as json_file:
        todo_list = [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": name
        } for todo in todos]

        data = {user_id: todo_list}
        json.dump(data, json_file)
