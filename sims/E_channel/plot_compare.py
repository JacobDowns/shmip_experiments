# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 14:59:49 2017

@author: jake
"""

from time_view import *
from tr_plot import *
import numpy as np

view1 = TimeView('results_parallel_E1/out.hdf5')
view2 = TimeView('results_parallel_1hr_E1/out.hdf5')
p = TRPlot(view1.mesh)

out_S1 = File('plot/S1.pvd')
out_Q1 = File('plot/Q1.pvd')
out_q1 = File('plot/q1.pvd')
out_pi1 = File('plot/pi1.pvd')
out_phi1 = File('plot/phi1.pvd')

out_S2 = File('plot/S2.pvd')
out_Q2 = File('plot/Q2.pvd')
out_q2 = File('plot/q2.pvd')
out_pi2 = File('plot/pi2.pvd')
out_phi2 = File('plot/phi2.pvd')

ff = FacetFunctionDouble(view2.mesh)


for i in range(0, view2.num_steps, 50):
  print i
  p.copy_tr_to_facet(view1.get_S(i), ff)
  out_S1 << ff
  p.copy_tr_to_facet(view1.get_Q(i), ff)
  out_Q1 << ff
  p.copy_tr_to_facet(view1.get_Pi(i), ff)
  out_pi1 << ff
  out_q1 << view1.get_q(i)
  out_phi1 << view1.get_phi(i)
  
  p.copy_tr_to_facet(view2.get_S(i), ff)
  out_S2 << ff
  p.copy_tr_to_facet(view2.get_Q(i), ff)
  out_Q2 << ff
  p.copy_tr_to_facet(view2.get_Pi(i), ff)
  out_pi2 << ff
  out_q2 << view2.get_q(i)
  out_phi2 << view2.get_phi(i)
  
