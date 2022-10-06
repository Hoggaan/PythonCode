def print_formatted(number):
    # your code goes here
    v = len(str(bin(number)).lstrip("0b"))
    for a in range (1,number+1):
        print(str(a).rjust(v," "),str(oct(a)).lstrip("0o").rjust(v," "),\
                str(hex(a)).lstrip("0x").rjust(v," ").upper(),str(bin(a)).lstrip("0b").rjust(v," "))

#if __name__ == '__main__':
        #n = int(input())
        #print_formatted(n)


line = 6
curline = 5
curline -= line
print('Curline: ',curline)