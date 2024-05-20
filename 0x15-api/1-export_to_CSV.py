#!/usr/bin/python3
"""Exports data in the CSV format"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    if 'username' not in user_data:
        print("User not found")
        sys.exit(1)

    username = user_data['username']

    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    filename = f"{user_id}.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([user_id, username, task['completed'], task['title']])
    
    print(f"Data exported to {filename}")
