#!/usr/bin/python3
"""Return info about employee's TODO list progress"""

import requests
from sys import argv

if __name__ == "__main__":
    baseUrl = 'https://jsonplaceholder.typicode.com/users'
    fullUrl = f"{baseUrl}/{argv[1]}"

    user = requests.get(fullUrl).json()
    name = user.get('name')

    todosUrl = f"{fullUrl}/todos"
    todos = requests.get(todosUrl).json()

    completed = [todo.get('title') for todo in todos if todo.get('completed') is True]
    print(f"Employee {name} is done with tasks({len(completed)}/{len(todos)}):")
    [print(f"\t {task}") for task in completed]
