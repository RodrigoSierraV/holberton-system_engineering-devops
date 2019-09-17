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

    id_user = argv[1]
    user = get('https://jsonplaceholder.typicode.com/users/{}'.format(
                  id_user))
    todo = get('https://jsonplaceholder.typicode.com/todos/?userId={}'.format(
                  id_user))
    task_list = []
    user_dict = {}

    for i in todo.json():
        task_dict = {}
        task_dict['task'] = i['title']
        task_dict['completed'] = i['completed']
        task_dict['username'] = user.json()['username']
        task_list.append(task_dict)

    user_dict['{}'.format(id_user)] = task_list

    with open('{}.json'.format(id_user), 'w') as file:
        json.dump(user_dict, file)
