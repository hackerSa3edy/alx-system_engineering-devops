#!/usr/bin/python3
"""
This script fetches data from the JSONPlaceholder API and exports all
users' to-do lists to a JSON file.
"""
import json
import requests


def users_todos():
    """Fetches all users' to-do lists from the JSONPlaceholder API and exports
    them to a JSON file.

    Parameters:
    None

    Returns:
    None

    The function works as follows:
    - It constructs two URLs: one for the users' data and one for the
    to-do lists.
    - It sends GET requests to these URLs and receives the responses.
    - It parses the JSON data from the responses.
    - It creates a dictionary with the users' IDs as the keys and the to-do
    lists as the values.
    - The to-do lists are lists of dictionaries, each containing the task
    title, completion status, and username.
    - It opens a new JSON file named 'todo_all_employees.json'.
    - It writes the dictionary to the JSON file.
    """
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    user_resp = requests.get(users_url)
    todos_resp = requests.get(todos_url)

    users_json = user_resp.json()
    todos_json = todos_resp.json()

    # all_records = {
    #     f"{user.get('id')}": [
    #         {
    #             "username": f"{user.get('username')}",
    #             "task": f"{todo.get('title')}",
    #             "completed": todo.get('completed')
    #             } for todo in todos_json
    #             if todo.get('userId') == user.get('id')
    #         ] for user in users_json
    #     }

    all_records = {}
    for user in users_json:
        user_id = user.get('id')
        username = user.get('username')
        user_todos = []
        for todo in todos_json:
            if todo.get('userId') == user_id:
                user_todos.append(
                    {
                        "username": username,
                        "task": f"{todo.get('title')}",
                        "completed": todo.get('completed')
                        }
                    )
        all_records[f"{user_id}"] = user_todos

    with open("todo_all_employees.json", 'w') as file:
        json.dump(all_records, file)


if __name__ == '__main__':
    """
    Usage:
    ------
    Run the script from the command line.

        python3 3-dictionary_of_list_of_dictionaries.py

    Example:

        python3 3-dictionary_of_list_of_dictionaries.py

    This will fetch all users' to-do lists and export them to a JSON file
    named 'todo_all_employees.json'.
    """
    users_todos()
