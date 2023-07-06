from pathlib import Path
import os


def create_file(filepath):
    with open(filepath, 'w'): pass


def add_content(filepath, content):
    with open(filepath, 'a') as file:
        file.write(content)


def replace_content(filepath, old_str, new_str):
    rep_file = Path(filepath)
    if not rep_file.exists():
        print('An error occurred')
        raise SystemExit
    else:
        with open(filepath, 'r+') as file:
            file_data = file.read()
            file_data.replace(old_str, new_str)
            file.seek()
            file.write(file_data)


def delete(filepath):
    del_file = Path(filepath)
    if not del_file.exists():
        print('An error occurred')
        exit(0)
    else:
        os.remove(filepath)


command = input().split('-')
while command != 'End':
    if command[0] == 'Create':
        filepath = f'files/{command[1]}'
        create_file(filepath)

    elif command[0] == 'Add':
        filepath = f'files/{command[1]}'
        content = command[2]
        add_content(filepath, content)
    elif command[0] == 'Replace':
        filepath = f'files/{command[1]}'
        old_content = command[2]
        new_content = command[3]
        replace_content(filepath, old_content, new_content)
    elif command[0] == 'Delete':
        filepath = f'files/{command[1]}'
        delete(filepath)

    command = input().split('-')
