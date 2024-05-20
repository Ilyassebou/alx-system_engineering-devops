#!/usr/bin/python3
"""
Check student .CSV output of user information
"""

import csv
import requests
import sys

USERS_URL = "https://jsonplaceholder.typicode.com/users?id="
TODOS_URL = "https://jsonplaceholder.typicode.com/todos"


def user_info(user_id):
    """Check CSV formatting"""

    # Fetch all TODO items
    todos_response = requests.get(TODOS_URL).json()

    try:
        # Read the content of the CSV file
        with open(f"{user_id}.csv", 'r') as f:
            output = f.read().strip()

        count = 0
        flag = 0

        for task in todos_response:
            if task['userId'] == user_id:
                user_response = requests.get(USERS_URL + str(task['userId'])).json()
                if not user_response:
                    print(f"User with ID {task['userId']} not found")
                    return

                username = user_response[0]['username']
                line = (
                    f'"{task["userId"]}","{username}","{task["completed"]}","{task["title"]}"'
                )
                count += 1

                if line not in output:
                    print(f"Task {count} Formatting: Incorrect")
                    flag = 1

        if flag == 0:
            print("Formatting: OK")

    except FileNotFoundError:
        print("CSV file not found")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./main_2.py <employee_id>")
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    user_info(user_id)
