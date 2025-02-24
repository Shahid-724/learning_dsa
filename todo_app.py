# The code for todo list app
user_input = ''
data = []

def show_menu():
    print('Menu:')
    print('1. Add an item')
    print('2. Mark as done')
    print('3. View Items')
    print('4. Exit')

while user_input != '4':

    show_menu()
    user_input = input('Enter your choice: ')

    if user_input == '1':
        item = input('What is to be done? ')
        data.append(item)
        print(f'Added {item} to the list')

    elif user_input == '2':
        item = input('What is to be marked as done? ')
        if item in data:
            data.remove(item)
            print(f'{item} is removed from the list')
        else:
            print(f'{item} not in list')

    elif user_input == '3':
        print('The items in the todo list are:')
        for i in data:
            print(i)

    elif user_input == '4':
        print('Goodbye!')

    else:
        print('Please enter 1, 2, 3 or 4')

# Notes
# A lot of features can be added to this code
# Work on it