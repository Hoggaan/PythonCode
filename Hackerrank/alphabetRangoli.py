def rangoli(n):
    alphapet = 'abcdefjhiklmnopqrstuvwxyz'
    last = ''
    for i in range(n,-n-1, -1):
        if i <= -1:
            i = abs(i)
        last = f'-{alphapet[i]}-'.center(10, last)
        print(last)

#rangoli(4)
# The idea, i am trying now is to create a variable called last which will keep the last '-h-g-f-i-j) then
# I am going to center the new variable with that center. 
size = 8 
#for i in range(-size +1, size):
#    print(i)
width = (size-1) * 4 + 1
for i in [abs(n) for n in range(-size+1, size)]:
        line = chr(ord("a") + i)
        #print(line)
        for j in range(size-i-1):
            letter = chr(ord("a") + i + j + 1)
            #print(line)
            line = letter + line + letter


s = 'abdikaf hashi'
s = ' '.join(s.capitalize() for s in s.split())
print(s)
