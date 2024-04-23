#!/usr/bin/python3
'''
This script fetches data from the JSONPlaceholder API to track the progress
of a user's to-do list.
'''
import requests
import sys


def todo_list_progress(user_id):
    '''
    todo_list_progress(user_id: int) -> None:
    Fetches and prints the progress of a user's to-do list from the
    JSONPlaceholder API.

    Parameters:
    user_id (int): The ID of the user.

    Returns:
    None
    '''
    user_data = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    user_todos = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'

    user_data_resp = requests.get(user_data)
    user_todos_resp = requests.get(user_todos)

    user_json = user_data_resp.json()
    todos_json = user_todos_resp.json()

    done_tasks = [todo for todo in todos_json if todo.get('completed') is True]
    EMPLOYEE_NAME = user_json.get('name')
    TOTAL_NUMBER_OF_TASKS = len(todos_json)
    NUMBER_OF_DONE_TASKS = len(done_tasks)

    print(
        f"Employee {EMPLOYEE_NAME} is done with "
        f"tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):"
        )

    for todo in done_tasks:
        print(f'\t {todo.get("title")}')


if __name__ == '__main__':
    user_id: int = int(sys.argv[1])
    todo_list_progress(user_id)
