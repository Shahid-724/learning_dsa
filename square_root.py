# This code calculates the square root by using bisection method

def square_root(number, tolerance=1e-7, max_iterations=100):

    # If the number is zero
    if number == 0:
        root = 0
        print(f'The square root of {number} is {root}')

    # If the number is one
    if number == 1:
        root = 1
        print(f'The square root of {number} is {root}')

    # If the number is not zero or one
    else:
        low = 0
        high = max(1, number)
        root = None

        # Looping max_iterations times to find the accurate root
        for i in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid * mid

            # If the root is out of tolerance limit
            if abs(number - square_mid) < tolerance:
                root = mid
                break

            # If the root is in tolerance limit and greater than mid
            elif number > square_mid:
                low = mid

            # If the root is in tolerance limit and lesser than mid
            else:
                high = mid

        # If root is not found in max_iterations
        if root is None:
            print(f'Failed to converge within {max_iterations} iterations')
        else:
            print(f'The square root of {number} is {root}')

    return root

n = int(input('Enter a number: '))
square_root(n)