#!/usr/bin/python3
"""
This script fetches data from the JSONPlaceholder API and exports a user's
to-do list to a CSV file.
"""
import csv
import requests
import sys


def export_to_CSV(user_id):
    """Fetches a user's to-do list from the JSONPlaceholder API and exports
    it to a CSV file.

    Parameters:
    user_id (int): The ID of the user.

    Returns:
    None

    The function works as follows:
    - It constructs two URLs: one for the user's data and one for the user's
    to-do list.
    - It sends GET requests to these URLs and receives the responses.
    - It parses the JSON data from the responses.
    - It opens a new CSV file named after the user's ID.
    - It writes the headers to the CSV file.
    - It iterates over the to-do list and writes each to-do as a row in the
    CSV file.
    """
    user_data = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    user_todos = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'

    user_data_resp = requests.get(user_data)
    user_todos_resp = requests.get(user_todos)

    user_json = user_data_resp.json()
    EMPLOYEE_USERNAME = user_json.get('username')
    EMPLOYEE_ID = user_json.get('id')

    todos_json = user_todos_resp.json()

    with open(f'{EMPLOYEE_ID}.csv', 'w') as file:
        CSV_HEADERS = [
            "USER_ID",
            "USERNAME",
            "TASK_COMPLETED_STATUS",
            "TASK_TITLE"
            ]

        csv_writer = csv.DictWriter(
            file,
            fieldnames=CSV_HEADERS,
            quotechar='"',
            quoting=1
            )

        for todo in todos_json:
            csv_writer.writerow(
                {
                    "USER_ID": f"{EMPLOYEE_ID}",
                    "USERNAME": f"{EMPLOYEE_USERNAME}",
                    "TASK_COMPLETED_STATUS": f"{todo.get('completed')}",
                    "TASK_TITLE": f"{todo.get('title')}"
                    }
                )


if __name__ == '__main__':
    """
    Usage:
    ------
    Run the script from the command line and pass the user_id as an argument.

        python3 1-export_to_CSV.py <user_id>

    Example:

        python3 1-export_to_CSV.py 1

    This will fetch the to-do list of the user with ID 1 and export it to a
    CSV file named '1.csv'.
    """
    user_id: int = int(sys.argv[1])
    export_to_CSV(user_id)
