# The main focus of this lesson is 
# - To make code more abstract, we do not need to know the implementation details of everything
# - Differences between list and tuples, list are mutable(changable) and tuples are not

def main():
    student = get_student()
    print(f'{student[0]} from {student[1]}')

def get_student():
    name = input('Name: ')
    house = input('House: ')
    return (name, house)

if __name__ == '__main__':
    main()