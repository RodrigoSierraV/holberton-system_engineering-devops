#!/usr/bin/python3
"""
script that using https://jsonplaceholder.typicode.com/, for a given
employee ID, returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv
import csv

if __name__ == '__main__':

    id_user = argv[1]
    user = get('https://jsonplaceholder.typicode.com/users/{}'.format(
                  id_user))
    todo = get('https://jsonplaceholder.typicode.com/todos/?userId={}'.format(
                  id_user))
    with open('{}.csv'.format(id_user), 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for i in todo.json():
            writer.writerow([i['userId'], user.json()['username'],
                            i['completed'], i['title']])
