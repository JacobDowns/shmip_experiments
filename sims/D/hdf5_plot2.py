# -*- coding: utf-8 -*-
"""
Plot to make sure effective pressure is periodic. 
"""

from time_view import *
from pylab import *
from matplotlib import cm
import matplotlib
matplotlib.rcParams.update({'font.size': 10})

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
  
  for i in range(0*365, 9125):
    
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
  plt1.set_title('N (Pa): (x = 10km, y = 10km)', fontsize=12)
  #plt1.set_yscale('log')
  plt2 = fig.add_subplot(3,1,2)
  plt2.set_title('N (Pa): (x = 50km, y = 10km)', fontsize=12)
  #plt2.set_yscale('log')
  plt3 = fig.add_subplot(3,1,3)
  plt3.set_title('N (Pa): (x = 90km, y = 10km)', fontsize=12)
  #plt3.set_yscale('log'  #plt4 = fig.add_subplot(4,1,4)
  #plt4.set_title('total m ' + r'$(m^3 / s)')
  
  max1 = []
  max2 = []
  max3 = []
  
  start = 0.0
  stop = 1.0
  number_of_lines= len(Ns1) / 365
  cm_subsection = linspace(start, stop, number_of_lines) 
  colors = [ cm.bwr(x) for x in cm_subsection ]
  
 
  
  Ns1 = Ns1.reshape((len(Ns1) / 365, 365))
  Ns2 = Ns2.reshape((len(Ns2) / 365, 365))
  Ns3 = Ns3.reshape((len(Ns3) / 365, 365))

  Ns1 = Ns1[:,0:100]
  Ns2 = Ns2[:,0:100]
  Ns3 = Ns3[:,0:100]
  
  s1 = Ns1.min()
  s2 = Ns2.min()
  s3 = Ns3.min()
  
  print (s1, s2, s3)
  
  
  for i in range(0, len(Ns1)):
    ns1 = Ns1[i,:]
    ns2 = Ns2[i,:]
    ns3 = Ns3[i,:]
    
    print ns1
    print len(ns1)
    #ns1 -= abs(s1) + 1e-16
    #ns2 -= abs(s2) + 1e-16
    #ns3 -= abs(s3) + 1e-16
  
    plt1.plot(ns1, color = colors[i], linewidth = 0.5)
    plt2.plot(ns2, color = colors[i], linewidth = 0.5)
    plt3.plot(ns3, color = colors[i], linewidth = 0.5)  
    #plt4.plot(ms, color = colors[i], linewidth = 0.5)
    
  tight_layout(pad=0.5, w_pad=0.5, h_pad=1.0)
  savefig('images/N_comp' + str(j) + '.png', dpi = 700)

  

  
  

