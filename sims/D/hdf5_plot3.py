# -*- coding: utf-8 -*-
"""
Plot to make sure effective pressure is periodic. 
"""

from time_view import *
from pylab import *
from matplotlib import cm
import matplotlib
matplotlib.rcParams.update({'font.size': 10})

for j in [3]:
  
  """
  # Load hdf5 file
  input_file = 'results_hdf5/D' + str(j) + '.hdf5' 
  #input_file = 'results_hdf5/out.hdf5' 
  view = TimeView(input_file)
  
  ### Sampe N at points
  
  Ns1 = []
  Ns2 = []
  Ns3 = []
  hs = []
  ts = []
  total_ms = []
  
  for i in range(0, view.num_steps):
    
    print i
    N = view.get_N(i)
    t = view.get_t(i)
  
    Ns1.append(N([5.0, 10.00]))
    Ns2.append(N([50.0, 10.00]))
    Ns3.append(N([90.0, 10.00]))
    hs.append(view.get_sheet_volume(i))
    
    
    total_ms.append(view.get_total_m(i))
    ts.append(t)
    
  ts = array(ts)
  Ns1 = array(Ns1)
  Ns2 = array(Ns2)
  Ns3 = array(Ns3)
  hs = array(hs)
  
 
  
  Ns1 = Ns1.reshape((len(Ns1) / 73, 73))
  Ns2 = Ns2.reshape((len(Ns2) / 73, 73))
  Ns3 = Ns3.reshape((len(Ns3) / 73, 73))
  hs = hs.reshape((len(hs) / 365, 365))
  
  savetxt('Ns1.txt', Ns1)
  savetxt('Ns2.txt', Ns2)
  savetxt('Ns3.txt', Ns3)
  savetxt('hs.txt', hs)
  quit()"""
  
  Ns1 = loadtxt('Ns1.txt')
  Ns2 = loadtxt('Ns2.txt')
  Ns3 = loadtxt('Ns3.txt')
  hs = loadtxt('hs.txt')
  
  
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

  

  s = 80  
  start = 0.0
  stop = 1.0
  cm_subsection = linspace(start, stop, len(Ns1) - s) 
  colors = [ cm.jet(x) for x in cm_subsection ]
  
  cs = ['r', 'g', 'b']
  
  print len(Ns1)
  
  for i in range(len(Ns1) - s):
    ns1 = Ns1[i+s,:]
    ns2 = Ns2[i+s,:]
    ns3 = Ns3[i+s,:]
    
    #ns1 -= abs(s1) + 1e-16
    #ns2 -= abs(s2) + 1e-16
    #ns3 -= abs(s3) + 1e-16
  
    plt1.plot(ns1, color = cs[i % 3], linewidth = 0.5)
    plt2.plot(ns2, color = cs[i % 3], linewidth = 0.5)
    plt3.plot(ns3, color = cs[i % 3], linewidth = 0.5)  
    #plt4.plot(ms, color = colors[i], linewidth = 0.5)
    
  tight_layout(pad=0.5, w_pad=0.5, h_pad=1.0)
  savefig('images/D3.png', dpi = 700)

  

  
  

