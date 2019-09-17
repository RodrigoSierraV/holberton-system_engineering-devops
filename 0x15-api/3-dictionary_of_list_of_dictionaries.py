#!/usr/bin/python3
"""
script that using https://jsonplaceholder.typicode.com/, for a given
employee ID, returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv
import csv
import json


if __name__ == '__main__':

    user = get('https://jsonplaceholder.typicode.com/users')
    todo = get('https://jsonplaceholder.typicode.com/todos')

    user_dict = {}

    for j in user.json():
        task_list = []
        for i in todo.json():
            task_dict = {}
            task_dict['task'] = i['title']
            task_dict['completed'] = i['completed']
            task_dict['username'] = j['username']
            task_list.append(task_dict)

        user_dict['{}'.format(j['id'])] = task_list
        print(user_dict.values())

    with open('todo_all_employees.json', 'w') as file:
        json.dump(user_dict, file)
