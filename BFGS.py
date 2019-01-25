import numpy
import scipy
import matplotlib.pyplot as plt
from scipy.optimize import minimize

x = numpy.linspace(0,31,200)
q = numpy.sin(x/5) * numpy.exp(x/10) + 5 * (numpy.exp((-x)/2))

plt.plot(x, q)
plt.show()

def fun(x):
    
    return numpy.sin(x / 5.) * numpy.exp(x / 10.) + 5 * numpy.exp(-x / 2.)

res1 = minimize(fun, 25)

res2 = minimize(fun, 2, method='BFGS')

print res2

res3 = minimize(fun, 30, method='BFGS')

print res3