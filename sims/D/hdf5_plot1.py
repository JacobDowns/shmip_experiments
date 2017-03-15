# -*- coding: utf-8 -*-
"""
Plot to make sure effective pressure is periodic. 
"""

from time_view import *
from pylab import *

for j in [2]:

  # Load hdf5 file
  input_file = 'results_hdf5/D' + str(j) + '.hdf5' 
  view = TimeView(input_file)
  
  ### Sampe N at points
  
  Ns1 = []
  Ns2 = []
  Ns3 = []
  ts = []
  total_ms = []
  
  for i in range(view.num_steps - 2*365, view.num_steps):
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
  
  ### Plot difference in effective pressure from one day to the next
  
  fig = figure()
  plt1 = fig.add_subplot(3,1,1)
  #plt1.set_yscale('log')
  plt2 = fig.add_subplot(3,1,2)
  #plt2.set_yscale('log')
  plt3 = fig.add_subplot(3,1,3)
  #plt3.set_yscale('log')
  max1 = []
  max2 = []
  max3 = []
  
  Ns1_0 = Ns1[0:365]
  Ns1_1 = Ns1[365:]
  
  Ns2_0 = Ns2[0:365]
  Ns2_1 = Ns2[365:]
  
  Ns3_0 = Ns3[0:365]
  Ns3_1 = Ns3[365:]
  
  plt1.plot(Ns1_0, 'r')
  plt1.plot(Ns1_1, 'g')
  plt2.plot(Ns2_0, 'r')
  plt2.plot(Ns2_1, 'g')
  plt3.plot(Ns3_0, 'g')
  plt3.plot(Ns3_1, 'g')
  
  #plt1.plot(np.abs(Ns1_0 - Ns1_1) / abs(Ns1_0), 'ko-', ms = 2)
  #plt2.plot(np.abs(Ns2_0 - Ns2_1) / abs(Ns1_0), 'ko-', ms = 2)
  #plt3.plot(np.abs(Ns3_0 - Ns3_1) / abs(Ns1_0), 'ko-', ms = 2)
  
  
  savefig('images/N_comp' + str(j) + '.png', dpi = 650)

  

  
  

