#!/usr/bin/python3
"""
This script fetches data from the JSONPlaceholder API and exports a user's
to-do list to a JSON file.
"""
import json
import requests
import sys


def export_to_JSON(user_id):
    """Fetches a user's to-do list from the JSONPlaceholder API and exports it
    to a JSON file.

    Parameters:
    user_id (int): The ID of the user.

    Returns:
    None

    The function works as follows:
    - It constructs two URLs: one for the user's data and one for the user's
    to-do list.
    - It sends GET requests to these URLs and receives the responses.
    - It parses the JSON data from the responses.
    - It creates a dictionary with the user's ID as the key and the to-do list
    as the value.
    - The to-do list is a list of dictionaries, each containing the task
    title, completion status, and username.
    - It opens a new JSON file named after the user's ID.
    - It writes the dictionary to the JSON file.
    """
    user_data = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    user_todos = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'

    user_data_resp = requests.get(user_data)
    user_todos_resp = requests.get(user_todos)

    user_json = user_data_resp.json()
    todos_json = user_todos_resp.json()

    EMPLOYEE_ID = user_json.get('id')
    EMPLOYEE_USERNAME = user_json.get('username')

    all_records = {
        f"{EMPLOYEE_ID}": [
            {
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": EMPLOYEE_USERNAME
            } for todo in todos_json
        ]
    }

    with open(f"{EMPLOYEE_ID}.json", 'w') as file:
        json.dump(all_records, file)


if __name__ == '__main__':
    """
    Usage:
    ------
    Run the script from the command line and pass the user_id as an argument.

        python3 2-export_to_JSON.py <user_id>

    Example:

        python3 2-export_to_JSON.py 1

    This will fetch the to-do list of the user with ID 1 and export it to a
    JSON file named '1.json'.
    """
    user_id: int = int(sys.argv[1])
    export_to_JSON(user_id)
