# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 14:59:49 2017

@author: jake
"""

from time_view import *
from tr_plot import *
import numpy as np

view = TimeView('results_1/out.hdf5')
p = TRPlot(view.mesh)

out_S = File('plot/S.pvd')
out_Pi = File('plot/Pi.pvd')
out_dpw_ds = File('plot/dpw_ds.pvd')
out_dphi_ds = File('plot/dphi_ds.pvd')
out_q_c = File('plot/q_c.pvd')
out_f = File('plot/f.pvd')
out_Q = File('plot/Q.pvd')
out_q = File('plot/q.pvd')
out_phi = File('plot/phi.pvd')

ff = FacetFunctionDouble(view.mesh)


for i in range(view.num_steps):
  print i
  p.copy_tr_to_facet(view.get_S(i), ff)
  out_S << ff
  p.copy_tr_to_facet(view.get_dpw_ds(i), ff)
  out_dpw_ds << ff
  #p.copy_tr_to_facet(view.get_dphi_ds(i), ff)
  #out_dphi_ds << ff
  p.copy_tr_to_facet(view.get_q_c(i), ff)
  out_q_c << ff
  p.copy_tr_to_facet(view.get_Pi(i), ff)
  out_Pi << ff
  p.copy_tr_to_facet(view.get_f(i), ff)
  out_f << ff
  p.copy_tr_to_facet(view.get_Q(i), ff)
  out_Q << ff
  
  out_q << view.get_q(i)
  out_phi << view.get_phi(i)
  
