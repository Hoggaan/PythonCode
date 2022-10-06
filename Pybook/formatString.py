def print_formatted(number):
    # your code goes here
        for number in range(1,number+1):
            print("{:>3}{:>3}{:>3}{:>3}".format( number, oct(number)[2:],hex(number)[2:],bin(number)[2:]))

print_formatted(2)
