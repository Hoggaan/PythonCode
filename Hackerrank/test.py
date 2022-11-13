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

# alaab = car(12, 22)
# car._make([22, 300])

# alaab = alaab._replace(qiimaha = 13)._asdict()
# print(alaab)

# gaari = namedtuple('gaari', [*car._fields, 'darawal'])
# gri = gaari(13, 234, 'Xassan')
# print(gri)


# from dateutil import tz, parser
# from dateutil.relativedelta import relativedelta
# from datetime import datetime

# PYCON_DATE = parser.parse("May 12, 2023 8:00 PM")
# PYCON_DATE = PYCON_DATE.replace(tzinfo = tz.gettz("America/New_York"))
# now = datetime.now(tz=tz.tzlocal())
# countdown = relativedelta(PYCON_DATE, now)
# print(countdown)

# def timeamoun(time_init: str, countdown:relativedelta): 
#     t = getattr(countdown, time_init)
#     return f"{t} {time_init}" if t != 0 else ""

# time_units = ["years", "months", "days", "hours", "minitues", "seconds"]
# output = (t for tu in time_units if (t := timeamoun(tu, countdown)))

import numpy as np

# print(np.random.uniform(-np.pi, np.pi))

total = 0.0
i = 0
while i < 10:
    total += 0.1
    i += 1
# print(total)

s = "Yaaa Kaa Waalan"
cnt = 0
for s in s:
    if s >= 'a' and s <= 'z':
        cnt += 1
# print(cnt)

# s[0] = 'b'
# print(s)
lst = [12,2,2,2,1,2,3,2,2]
# print(lst.index(3))

dc = {'Aniga':1, 'Adiga': 2, 'Ayaga':3, 'Adinka':4}
dc.pop('Adiga')
print(dc)
