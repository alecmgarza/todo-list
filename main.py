from pathlib import Path
import json

def prompt_user():
    user_action = input('Enter a command for what you would like to do: '
    '(A)dd Task, (D)elete Task, (C)omplete Task, or (Q)uit. ')

    return user_action

def output_list(todo_list):
    for i in range(len(todo_list)):
        print(f'{i + 1}. ' + todo_list[i])

def mark_complete(todo_list, i):
    todo_list[i] = '\u0336' + '\u0336'.join(todo_list[i])

def load_file(list_file):
    with open(list_file, 'r') as f:
        todo_list = json.load(f)
        return todo_list

def save_file(list_file, todo_list):
    with open(list_file, 'w') as f:
        json.dump(todo_list, f)

def main():
    list_open = True
    todo_list = []
    list_file = Path('.todo_list.json')

    if list_file.exists():
        todo_list = load_file(list_file)

    while list_open:
        user_action = prompt_user()

        if user_action == 'A':
            todo_list.append(input('Enter your task: '))
            save_file(list_file, todo_list)
            output_list(todo_list)
        elif user_action == 'D':
            try: 
                delete_pos = int(input('Enter the position of the task you would like to delete: '))
                todo_list.pop(delete_pos - 1)
                save_file(list_file, todo_list)
                output_list(todo_list)
            except IndexError:
                print('No task at this position.')
                output_list(todo_list)
            except ValueError:
                print('Please enter a number for the task position.')
        elif user_action == 'C': 
            try:
                complete_pos = int(input('Enter the position of the task you would like to mark completed: '))
                mark_complete(todo_list, complete_pos - 1)
                save_file(list_file, todo_list)
                output_list(todo_list)
            except IndexError:
                print('No task at this position.')
                output_list(todo_list)
            except ValueError:
                print('Please enter a number for the task position.')
                output_list(todo_list)
        elif user_action == 'Q':
            save_file(list_file, todo_list)
            break
        else:
            print('Invalid command entered.')

main()