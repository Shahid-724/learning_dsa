# This code is used to solve tower of hanoi using recursion

def tower_of_hanoi(n, source, destination, auxillary):
    if n == 1:
        print(f'Move disk 1 from {source} to {destination}')
        return
    tower_of_hanoi(n - 1, source, auxillary, destination)
    print(f'Move disk {n} from {source} to {destination}')
    tower_of_hanoi(n - 1, auxillary, destination, source)

n = int(input('Enter the no. of disks: '))
source = 'A'
destination = 'B'
auxillary = 'C'

tower_of_hanoi(n, source, auxillary, destination)