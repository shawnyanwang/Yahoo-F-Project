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