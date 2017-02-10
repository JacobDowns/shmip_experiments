# -*- coding: utf-8 -*-
"""
Plot to make sure effective pressure is periodic. 
"""

from time_view import *
from pylab import *

for j in [1]:

  # Load hdf5 file
  input_file = 'results_hdf5/D' + str(j) + '.hdf5' 
  view = TimeView(input_file)
  
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
  
  for i in range(1, (view.num_steps) / 365):
    ns1_1 = Ns1[i*365:(i+1)*365]
    ns1_0 = Ns1[(i-1)*365:i*365]
    #dif1 = np.abs(ns1_0 - ns1_1)
    #index1 = dif1.argmax()
    #max1.append(dif1[index1] / max(abs(ns1_0[index1]), abs(ns1_1[index1])))
    max1.append(max( abs((ns1_0 - ns1_1) / ns1_0) ))
    
    ns2_1 = Ns2[i*365:(i+1)*365]
    ns2_0 = Ns2[(i-1)*365:i*365]
    #dif2 = np.abs(ns2_0 - ns2_1)
    #index2 = dif2.argmax()
    #max2.append(dif2[index2] / max(abs(ns2_0[index2]), abs(ns2_1[index2])))
    max2.append(max( abs((ns2_0 - ns2_1) / ns2_0) ))
    
    ns3_1 = Ns3[i*365:(i+1)*365]
    ns3_0 = Ns3[(i-1)*365:i*365]
    #dif3 = np.abs(ns3_0 - ns3_1)
    #index3 = dif3.argmax()
    #max3.append(dif3[index3] / max(abs(ns3_0[index2]), abs(ns3_1[index2])))
    max3.append(max( abs((ns3_0 - ns3_1) / ns3_0) ))
    
  plt1.plot(max1, 'ko-', ms = 2)
  plt2.plot(max2, 'ko-', ms = 2)
  plt3.plot(max3, 'ko-', ms = 2)
  
  
  savefig('images/N_comp' + str(j) + '.png', dpi = 650)

  

  
  

