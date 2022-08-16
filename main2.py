# 1.
from math import factorial as fct
def combinations(n, k):
    return int(fct(n) / (fct(k) * fct(n - k)))
k13k4 = combinations(13, 4)
k52k4 = combinations(52, 4)
k4 = k13k4 / k52k4
print('Вероятность, что с первого раза извлечем все 4 карты крести = {0:.2f}%'.format(k4 * 100))
k4t1 = combinations(4, 1)
k4t2 = combinations(4, 2)
k4t3 = combinations(4, 3)
k4t4 = combinations(4, 4)
k48t3 = combinations(48, 3)
k48t2 = combinations(48, 2)
k48t1 = combinations(48, 1)
k48t0 = combinations(48, 0)
tyz1 = k4t1 * k48t3 / k52k4
tyz2 = k4t2 * k48t2 / k52k4
tyz3 = k4t3 * k48t1 / k52k4
tyz4 = k4t4 * k48t0 / k52k4
tyz = tyz1 + tyz2 + tyz3 + tyz4
print('Вероятность, что с первого раза окажется из 4 карт 1 туз = {0:.0f}%'.format(tyz * 100))
# 2.
s10c3 = combinations(10, 3)
try3 = 1 / s10c3
print('Количество комбинаций: ', s10c3)
print('Вероятность, что с первого раза угадает код = {0:.0f}%'.format(try3 * 100))
# 3.
d1 = 9 / 15
d2 = 8 / 14
d3 = 7 / 13
result = d1 * d2 * d3
print('Вероятность того, что все извлеченные детали окрашены = {0:.0f}%'.format(result * 100))
# 4.
ticket2 = combinations(100, 2)
ticket1 = 1 / ticket2
print('Вероятность того, что 2 приобретенных билета окажутся выигрышными = {0:.2f}%'.format(ticket1 * 100))
# Ответы: 1. Вероятность, что с первого раза извлечем все 4 карты крести = 0.26%
# 2. Вероятность, что с первого раза окажется из 4 карт 1 туз = 28%
# 3. Количество комбинаций:  120
# 4. Вероятность, что с первого раза угадает код = 1%
# 5. Вероятность того, что все извлеченные детали окрашены = 18%
# 6. Вероятность того, что 2 приобретенных билета окажутся выигрышными = 0.02%
