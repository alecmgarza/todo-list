todo_list = []

user_action = input('Enter a command for what you would like to do: '
'(A)dd Task, (D)elete Task, or (C)omplete Task. ')

if user_action == 'A':
    todo_list.append(input("Enter your task: "))
    print(todo_list)