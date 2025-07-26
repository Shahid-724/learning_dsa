# This lesson focuses on dictionary
# The same problem can be solved by using a dictionary
# You don't need to remember the indices and instead call the keys to access values
# Lists, tuples and strings are also actually dictionaries, but we can't have custom keys
# Dictionaries are mutable

def main():
    student = get_student()
    print(f'{student['name']} from {student['house']}')

def get_student():
    student = dict()
    student['name'] = input('Name: ')
    student['house'] = input('House: ')
    return student

if __name__ == '__main__':
    main()