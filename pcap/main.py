from sys import path
path.append(".\\modules")
# path.append("C:\\Users\\ttpha\\source\\repos\\practice\\pcap\\modules")
print(path)
from module import prodl, suml
# from module import prod1, sum1

x=0
zeroes = [0  for i in range(5)]

from itertools import repeat
zeroes = list(repeat(0,5))


x = 1
ones = [1 for i in range(5)]

ones = [1] * 4

x=2
twos = [x for i in range(5)]

print(suml(zeroes))
print(suml(ones))
#print(sum1(ones))
print(prodl(ones))




