import numpy
import scipy
import matplotlib.pyplot as plt
from scipy.optimize import minimize

x = numpy.linspace(0,31,200)
f = numpy.sin(x/5) * numpy.exp(x/10) + 5 * (numpy.exp((-x)/2))

plt.plot(x, f)
plt.show()

h = (list(map(int, numpy.sin(x/5) * numpy.exp(x/10) + 5 * (numpy.exp((-x)/2)))))


plt.plot(x, h)
plt.show()

def fun(x):
    
    d = numpy.sin(x / 5.) * numpy.exp(x / 10.) + 5 * numpy.exp(-x / 2.)
    return d.astype(int)

res1 = minimize(fun, 30, method='BFGS')

print res1

from scipy.optimize import differential_evolution

bounds = [(1,30)]
res = differential_evolution(fun, bounds)
res.x, res.fun