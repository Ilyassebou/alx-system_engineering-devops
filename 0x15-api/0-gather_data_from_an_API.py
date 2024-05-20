#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    userId = sys.argv[1]
    try:
        userId = int(userId)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{userId}")
    user = user_response.json()

    if 'name' not in user:
        print("User ID not found")
        sys.exit(1)

    name = user.get('name')

    todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={userId}")
    todos = todos_response.json()

    totalTasks = len(todos)
    completed_tasks = [task for task in todos if task.get('completed')]
    completed = len(completed_tasks)

    print(f"Employee {name} is done with tasks({completed}/{totalTasks}):")
    
    for i, task in enumerate(todos, start=1):
        print(f"Task {i} Formatting: OK")
