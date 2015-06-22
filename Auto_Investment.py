__author__ = 'YangWang'


class Pre_Process:
    @staticmethod
    def str2float(str):
        res = 0
        if  str == None:
            res = 0
        elif str[-1] == 'B':
            res = float(str[0:-1])*(10 ** 9)
        elif str[-1] == 'M':
            res = float(str[0:-1])*(10 ** 6)
        else:
            res = float(str[0:])
        return int(res)








# Test = Pre_Process()
# print (Pre_Process.str2float("$27.1M"))

