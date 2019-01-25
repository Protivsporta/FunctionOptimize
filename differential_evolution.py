import numpy
import scipy
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution

x = numpy.linspace(0,31,200)
q = numpy.sin(x/5) * numpy.exp(x/10) + 5 * (numpy.exp((-x)/2))

plt.plot(x, q)
plt.show()

def fun(x):
    
    return numpy.sin(x / 5.) * numpy.exp(x / 10.) + 5 * numpy.exp(-x / 2.)

bounds = [(1,30)]
res = differential_evolution(fun, bounds)
res.x, res.fun