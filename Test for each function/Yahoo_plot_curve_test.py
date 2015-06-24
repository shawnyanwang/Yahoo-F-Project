__author__ = 'YangWang'


from Auto_Investment import PreProcess
print(27**5)
#PreProcess.get_all_symbol()

A = PreProcess.Curve(365*5, 'YGE')
A.moving_average(10)
A.derivative(1)
A.plot_curve()