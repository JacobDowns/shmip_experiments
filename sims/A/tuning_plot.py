# -*- coding: utf-8 -*-
"""
File for plotting width averaged effective pressure in A5 for tuning. 
"""

from sqrt_steady_view import *
from pylab import *

# Load Mauro's tuning data
data = loadtxt('tuning_A5.txt', delimiter=",")
xs = data[:,0]
Ns_m = data[:,1]
qs_m = data[:,4]

# Load my results
view = SqrtSteadyView('results_hdf5/steady_A5.hdf5')

# Compute width averaged effective pressure
N_int = view.width_integrate_N()
Ns_j = [N_int([x, 20e3]) for x in xs]
Ns_j = np.array(Ns_j) / 20e3   

# Compare
plot(xs, Ns_m, 'ro-', linewidth = 2, ms = 2, label = 'channel')
plot(xs, Ns_j, 'go-', linewidth = 2, ms = 2, label = 'sheet')
legend()
savefig('tune.png')
  
  

