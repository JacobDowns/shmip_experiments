# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 14:59:49 2017

@author: jake
"""

from time_view import *
from tr_plot import *
import numpy as np

view = TimeView('serial_continue_test/out.hdf5')
out_dir = 'plot2'
p = TRPlot(view.mesh)

out_S = File(out_dir + '/S.pvd')
out_Pi = File(out_dir + '/Pi.pvd')
out_dpw_ds = File(out_dir + '/dpw_ds.pvd')
out_dphi_ds = File(out_dir + '/dphi_ds.pvd')
out_q_c = File(out_dir + '/q_c.pvd')
out_f = File(out_dir + '/f.pvd')
out_Q = File(out_dir + '/Q.pvd')
out_q = File(out_dir + '/q.pvd')
out_phi = File(out_dir + '/phi.pvd')

ff = FacetFunctionDouble(view.mesh)


for i in range(0, view.num_steps, 1):
  print i
  p.copy_tr_to_facet(view.get_S(i), ff)
  out_S << ff
  """p.copy_tr_to_facet(view.get_dpw_ds(i), ff)
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
  out_phi << view.get_phi(i)"""
  
