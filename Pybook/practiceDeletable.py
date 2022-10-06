""" n, m = 7, 21

center = n // 2
text = ''
for i in range(n):
    if i < center:
        sign = '.|.' * (i + 1)
        print(sign.center(m, '-'))
    if i == center:
        sign = 'welcome'
        print(sign.center(m, '-'))
    if i > center:
        sign = '.|.' * (n-i)
        print(sign.center(m, '-'))
 """

from asyncio.proactor_events import _ProactorBaseWritePipeTransport


def print_formated(number):
    for n in range(number):
        print(f'{n}     {bin(n)[2:]}     {oct(n)[2:]}      {hex(n)[2:]}')



