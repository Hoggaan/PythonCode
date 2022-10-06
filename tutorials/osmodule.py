import os

'''From modules pdf i am following'''
# chdir - change current working directory
# print(os.getcwd())
# os.chdir(os.path.expanduser(os.getcwd()))
# print(os.getcwd())

# Absolute path from relative one
#print(os.path.abspath('../balo/merge.py')) # It is giving the absolute path of what you give
#print(os.path.basename('tutorials/sysmodule.py'))
#print(os.path.dirname('tutorials/sysmodule.py'))
#print(os.getcwd())

# Proberly set a path for a subdirectory of current working directory. 
# print(os.path.join(os.getcwd(), 'some','path'))
# print(os.path.join(os.getcwd(), 'Hello', 'World'))

'''Digging deep into os module'''
'''Goal: Get comfortable with all the functionalities from this module
Looking for examples from the internet. '''
# Anylitics Vidya : https://www.analyticsvidhya.com/blog/2021/05/30-useful-methods-from-python-os-module/
# Javapoint : https://www.javatpoint.com/python-os-module
# Digital Ocean : https://www.digitalocean.com/community/tutorials/python-os-module

#           -----------
# Anylitics Vidya
#1. print(os.name) # nt
#2. os.Error - Environment error class for I/O and OSError. returns any system related error.
# path = 'balo.txt'
# try:
#     with open('balo', 'r') as f:
#         balo = f.read()
# except os.error:
#     print('File does not exist!')

'''Day 2'''
# 3 - OS.ctermid() 
# 4 - os.environ
# 5 - os.getenv(key)
#os.getenv()


