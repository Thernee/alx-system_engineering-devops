#!/usr/bin/python3
"""Return info about employee's TODO list progress"""

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

    with open(f"{user_id}.csv", 'w') as csv_file:
        for todo in todos:
            csv_file.write(f'"{user_id}","{name}","{todo.get("completed")}",'
                           f'"{todo.get("title")}"\n')
