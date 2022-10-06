names = ['Ayaamaha','maalmaha','hawraaraha', 'Halbeegyada']
nums = [23, 22, 54, 43]

# # combined = []
# # for i,name in enumerate(names):
# #     combined.append((name, nums[i]))
# #print(combined)

# combined_zip = zip(names, nums)
# print(type(combined_zip))
# print(*combined_zip)

# from code import compile_command
# from itertools import combinations
# comb = combinations(names, 3)
# print(*comb)

# for i in zip(names, nums):
#     print(i)

# """ 08 Modules Document"""
# from itertools import permutations
# perm = permutations('abc')
# perms = ["".join(x) for x in perm]
# print(perms)

# # Python Counter Methods
# from collections import Counter
# counter = Counter({'Dog': 2, 'Cat': 1, 'Horse': 1})
# countCat = counter['Cat']   # Getting things from counter object
# # print(counter['Aniga']) # Returns zero when tried to get Non exisisting value

# counter['Horse'] = 3 # Setting an element into counter


# del counter['Dog']
# #print(counter)

"""Tutorial Module Day2"""
#import turtorialModule2 as pf

# #print("Prime factors of 1719:", tuple(pf.prime_factors(1719)))
# def hayaay(x='halhaleel'):
#     print(x)
# def main():
#     x = input('Wa ii kan: ')
#     hayaay(x)
# if __name__=='__main__':
#     main()

'''Tutorial Module Day 3'''
# from sys import stdout, stderr
# import sys

# stdout.write('This is same as print.\n')
# stderr.write('This is wee bit different.\n')
# print('We can import modules from these directories: \n', sys.path)

'''OS module'''
import os
# Change the active directory to the directory called 'Pybook'
os.chdir(os.path.expanduser("~\OneDrive\Desktop\Kaggle\PythonCode\Pybook\\"))
print('Working DirectoryL ' , os.getcwd())