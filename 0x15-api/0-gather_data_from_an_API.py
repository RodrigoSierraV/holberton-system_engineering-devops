#!/usr/bin/python3
"""
script that using https://jsonplaceholder.typicode.com/, for a given
employee ID, returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv


if __name__ == '__main__':

    id_user = argv[1]
    user = get('https://jsonplaceholder.typicode.com/users/{}'.format(
                  id_user))
    todo = get('https://jsonplaceholder.typicode.com/todos/?userId={}'.format(
                  id_user))
    completed = [i['title'] for i in todo.json() if i['completed']]
    print('Employee {} is done with tasks({}/{}):'.format(
                  user.json()['name'], len(completed), len(todo.json())))
    print('\n'.join('\t {}'.format(j) for j in completed))
