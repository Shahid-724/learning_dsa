# This lesson focuses on properties, getters and setters
# We use getter and setter methods so that the class attributes can't be changed
# outside of a class

class Student:

    def __init__(self, name, house):
        
        if not name:
            raise ValueError('Missing Name')
        
        if house not in ['Gryffindor', 'Hufflepuff', 'Slytherin', 'Ravenclaw']:
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

# Topics that I need to watch again and practice 

# - Properties, Getters and Setters
# - Types and Classes
# - Class Methods
# - Inheritence
# - Operator Overloading