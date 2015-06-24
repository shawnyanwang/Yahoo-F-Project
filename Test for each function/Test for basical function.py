__author__ = 'YangWang'

b = ['','', 'a', '', 'C', '']
i = 0
while i < len(b):
    if b[i] == '':
        b.remove(b[i])
        i -= 1
    i += 1

b.sort()
print (b)

import numpy as np

p = np.convolve([1, 2, 3]+[3 for j in range(5)], [1, 1,1,1])
print(p)
print([10, 2, 3, 4, 5]+[1, 1])
win = [1 for i in range(10)]
print(win)


l = [15, 18, 2, 36, 12, 78, 5, 6, 9]
