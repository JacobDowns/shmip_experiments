# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 10:23:56 2017

@author: jake
"""

from sqrt_steady_view import *
from pylab import *

# Load hdf5 file
view1 = SqrtSteadyView('results_B1/steady_B1.hdf5')
view2 = SqrtSteadyView('results_B2/steady_B2.hdf5')

xs = np.linspace(1, 100e3, 250)

q_int1 = view1.width_integrate_q()
qs1 = [q_int1([x, 20e3]) for x in xs]
qs1 = np.array(qs1)

q_int2 = view2.width_integrate_q()
qs2 = [q_int2([x, 20e3]) for x in xs]
qs2 = np.array(qs2)

plot(xs, qs1, 'ro-', ms = 2)
plot(xs, qs2, 'ko-', ms = 2)

print qs1[0]
print qs2[0]

File('q1.pvd') << q_int1
File('q2.pvd') << q_int2

savefig('out.png')

