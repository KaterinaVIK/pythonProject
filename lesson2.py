#Ответы: Вероятность, что стрелок попадет в цель ровно 85 раз = 4.81%
#Вероятность перегорания лампочек: 13.53%
#Вероятность перегорания 2 лампочек: 27.07%
#Вероятность, что орел выпадет ровно 70 раз = 6.28%
#Вероятность, что все мячи белые = 30.55%
#Вероятность, что два мяча белые = 4.52%
#Вероятность, что хотя бы один мяч белый = 99.88%

#1.
import math
from math import factorial as fct
def combinations(n, k):
    return int(fct(n) / (fct(k) * fct(n - k)))
p = 0.8
q = 1 - p

n = 100
k = 85

pnk = combinations(n, k) * p ** k * q ** (n - k)
print('Вероятность, что стрелок попадет в цель ровно 85 раз = {0:.2f}%'.format(pnk * 100))
#2.
def px(m, n=5000, p=0.0004):
    return (n * p) ** m / fct(m) * math.e ** (-n * p)
print('Вероятность перегорания лампочек: {0:.2f}%'.format(px(0) * 100))
print('Вероятность перегорания 2 лампочек: {0:.2f}%'.format(px(2) * 100))
#3.
p = 1 / 2
q = 1 - p

n = 144
k = 70

pnk = combinations(n, k) * p ** k * q ** (n - k)
print('Вероятность, что орел выпадет ровно 70 раз = {0:.2f}%'.format(pnk * 100))
#4.
def box(x, n, k):
    return combinations(k, x) * combinations (n-k, 2-x) / combinations(n, 2)

def box1(x):
    return box(x, n=10, k = 7)

def box2(x):
    return box(x, n=11, k = 9)

def boxes(x1, x2):
    return box1(x1) * box2(x2)
print('Вероятность, что все мячи белые = {0:.2f}%'.format(boxes(2, 2) * 100))
print('Вероятность, что два мяча белые = {0:.2f}%'.format(boxes(2, 0) + boxes(1, 1) + boxes(0, 2) * 100))
combs = ((0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2))
xbx = sum(boxes(*c) for c in combs)
print('Вероятность, что хотя бы один мяч белый = {0:.2f}%'.format(xbx * 100))