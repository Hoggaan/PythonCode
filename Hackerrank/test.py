# Counter is a container that stores elements as dictionary keys, and they counts as dictionary values.
# from collections import Counter
# numberofshoes_X = int(input())
# shoesSizeCounted = Counter(list(map(int, input().split())))
# nCustomers = int(input())
# totalEarned = []
# for customer in range(1, nCustomers+1):
#     lstShoeSizeAndPrice = list(map(int, input().split()))
#     if shoesSizeCounted[lstShoeSizeAndPrice[0]] == 0:
#         continue
#     else:
#         totalEarned.append(lstShoeSizeAndPrice[1])
#         shoesSizeCounted[lstShoeSizeAndPrice[0]] -= 1
# print(sum(totalEarned))

# from collections import Counter
# lst = [2, 3, 4, 5,5, 6, 8, 7, 6, 5, 18]
# lstcnt = Counter(lst)
# something = 5
# # if something in lstcnt:
# #     lstcnt.remove(something)
# print(lstcnt[5])

# 10
# 2 3 4 5 6 8 7 6 5 18  
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50


# ignore = ['the','a','if','in','it','of','or']
# ArtofWarCounter = Counter(ArtofWarLIST)
# for word in list(ArtofWarCounter):
#     if word in ignore:
#         del ArtofWarCounter[word]


# '''Another Hacker Rank Challange'''
# # from itertools import permutations
# # def split(s):
# #     return sorted([*s])
# # perms = list(permutations(split('Hack'.upper()), 2))
# # # for i in perms:
# # #     print(''.join(i))

# # s = 'string'
# # i = 4
# # print(hash(s), hash(i))

# '''Hacker Rank Challenge 27'''
# # def average():
# #     arraySize = int(input())
# #     setArray = set(map(float, input().split()))
# #     return sum(setArray)/len(setArray)

# # print(average())
# lst = [161,182,161,154,176,170,167,171,170,174]
# # print(float(lst))

# '''Challange 28'''
# from collections import defaultdict
# n, m = map(int, input().split())
# A = []
# for i in range(n):
#     A.append(input())
# B = []
# for i in range(m):
#     B.append(input())

# d = defaultdict(list)
# for i in range(len(A)):
#     if A[i] in B:
#         d[A[i]].append(str(i+1))

# for i in d.values():
#     print(' '.join(i))
    



# f = defaultdict()
# f['a'] = 1
# f['a'] = 2
# f['a'] = 3
# f['b'] = 1
# f['b'] = 2
# f['b'] = 3
# print(f)

'''Challanges 36'''

# from collections import OrderedDict
# ordinarydict = {}
# ordinarydict['a'] = 1
# ordinarydict['b'] = 2
# ordinarydict['c'] = 3
# ordinarydict['d'] = 4
# ordinarydict['c'] = 5
# print(ordinarydict)

# orddict = OrderedDict()
# orddict['a'] = 1
# orddict['b'] = 2
# orddict['c'] = 3
# orddict['d'] = 4
# orddict['c'] = 5
# print(orddict['b'])
# for i,m in orddict.items():
#     print(orddict['c'])

# # https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
# # Enter your code here. Read input from STDIN. Print output to STDOUT
# from collections import  OrderedDict
# n = int(input())
# orddict = OrderedDict()
# for i in range(n):
#     key, value = input().rsplit(' ', 1)
#     value = int(value)
#     try:
#         orddict[key] = orddict[key] + value
#     except KeyError:
#         orddict[key] = value

# for k, v in orddict.items():
#     print(str(k),v )
from collections import namedtuple
# point = namedtuple('point', 'x,y')
# pnt1 = point(2,3)
# pnt2 = point(3,4)
# pnt3 = point(5,3)
# dt = (pnt1.x * pnt2.x) + (pnt1.y * pnt2.y)
car = namedtuple('car', 'qiimaha, lacagta')
# premium = car(qiimaha = 1500, lacagta=2300, nuuca='premia',isticmaal=2)
# lst =  ['libaax', 'shabeel', 'bisad']

# bahal = namedtuple('bahal', *lst)

# print(premium.isticmaal)

alaab = car(12, 22)
car._make([22, 300])

print()