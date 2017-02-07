# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 10:23:56 2017

@author: jake
"""

from time_view import *
from pylab import *

for i in range(1,5)

# Load hdf5 file
view = TimeView('results_C4/out.hdf5')

### Sampe N at points

Ns1 = []
Ns2 = []
Ns3 = []
ts = []
total_ms = []

for i in range(view.num_steps):
  print i
  N = view.get_N(i)
  t = view.get_t(i)

  Ns1.append(N([10.0, 10.00]))
  Ns2.append(N([50.0, 10.00]))
  Ns3.append(N([90.0, 10.00]))
  total_ms.append(view.get_total_m(i))
  ts.append(t)
  
ts = array(ts)
Ns1 = array(Ns1)
Ns2 = array(Ns2)
Ns3 = array(Ns3)

#plot(ts, Ns1, 'k')

subplot(2,1,1)

for i in range((view.num_steps) / 48):
  ns1 = Ns1[i*48:(i+1)*48]
  ns2 = Ns2[i*48:(i+1)*48]
  ns3 = Ns3[i*48:(i+1)*48]
  plot(ns3, linewidth=0.1)
  print len(ns1)  


subplot(2,1,2)
plot(array(total_ms)[0:48])

savefig('N1.png', dpi = 650)

  

  
  

