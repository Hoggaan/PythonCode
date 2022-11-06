import random
nums = random.uniform(0,1)
# print(nums)
num = random.randint(3,5)
# print(num)
num = random.random() # Real Number between 0 and 1
# print(num)
num1 = random.randrange(3)
num2 = random.randrange(3, 9)
num3 = random.randrange(3, 27, 3)
# print(num1, num2, num3)
# print(num3)

a = random.uniform(1, 10)
# print(a)

a = [random.randint(0,9) for i in range(random.randint(0,9))]
# print(a)
a = [5, 8, 3, 1, 6, 3, 2, 3, 5]
random.shuffle(a)
# print(a)
b = random.choice(a)
#print(b)

a_s = random.sample(a,3)
#print(a_s)

import string

s = random.choice(string.ascii_letters)
# print(s)

sr = random.SystemRandom()
# print(sr.random())
# print(sr.randint(3, 9))
# print(sr.randrange(2,12,3))

