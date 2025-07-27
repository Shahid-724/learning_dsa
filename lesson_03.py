# This lesson is on classes and objects
# We can create our own data types using oop
# Classes allow you to invent your own data types and give them a name
# In this case we can create a data type called student that stores student details
# Classes are blueprints for objects

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError('Missing Name')
        if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
            raise ValueError('Invalid House')
        self.name = name 
        self.house = house

    def __str__(self):
        return f'{self.name} from {self.house}'

def main():
    student = get_student()
    print(student)

def get_student():
    name = input('Name: ')
    house = input('House: ')
    return Student(name, house)

if __name__ == '__main__':
    main()