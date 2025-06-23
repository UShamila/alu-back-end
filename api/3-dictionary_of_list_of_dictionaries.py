#!/usr/bin/python3
"""
Python script that exports all users' TODO lists to a JSON file
"""
import json
import requests


def get_all_users():
    """
    Get the list of all users
    """
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    return response.json()


def get_all_todos():
    """
    Get the list of all todos
    """
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    return response.json()


def export_all_todos_to_json(users, todos):
    """
    Export all users' TODO lists to a JSON file
    """
    data = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        # Filter todos belonging to current user
        user_todos = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            }
            for todo in todos if todo.get("userId") == user_id
        ]
        data[user_id] = user_todos

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)


def main():
    users = get_all_users()
    todos = get_all_todos()
    export_all_todos_to_json(users, todos)


if __name__ == "__main__":
    main()
