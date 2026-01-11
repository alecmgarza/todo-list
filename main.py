list_open = True
todo_list = []

while list_open:
    def prompt_user():
        user_action = input('Enter a command for what you would like to do: '
        '(A)dd Task, (D)elete Task, (C)omplete Task, or (Q)uit. ')

        return user_action
    
    def output_list():
        for i in range(len(todo_list)):
            print(f'{i + 1}. ' + todo_list[i])

    user_action = prompt_user()

    if user_action == 'A':
        todo_list.append(input('Enter your task: '))
        output_list()
    elif user_action == 'D':
        delete_pos = int(input('Enter the position of the task you would like to delete: '))
        try: 
            todo_list.pop(delete_pos - 1)
            output_list()
        except IndexError:
            print('No task at this position.')
            output_list()
    elif user_action == 'C': 
        complete_index = int(input('Enter the number of the task you would like to mark completed: ')) - 1
    elif user_action == 'Q':
        break
    else:
        print('Invalid command entered.') 