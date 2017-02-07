# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 10:23:56 2017

@author: jake
"""

from sqrt_steady_view import *
from pylab import *

# Load hdf5 file
view = SqrtSteadyView('results_A5/steady_A5.hdf5')


# Load Mauro's tuning data
data = loadtxt('tuning_A5.txt', delimiter=",")
xs = data[:,0]
Ns_m = data[:,1]
qs_m = data[:,4]


increments = 250
#xs = np.linspace(1, 100e3, increments)

# Compute width averaged effective pressure
N_int = view.thing()
Ns = [N_int([x, 20e3]) for x in xs]
Ns = np.array(Ns) / 20e3   

plot(xs, Ns_m, 'ro-', linewidth = 2, ms = 2)
plot(xs, Ns, 'ko-', linewidth = 2)
savefig('thing.png')

#tools.write_nc()
  
  

