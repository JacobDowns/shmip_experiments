# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 14:59:49 2017

@author: jake
"""

from time_view import *
from tr_plot import *
import numpy as np

view1 = TimeView('results_sdt1_E1/out.hdf5')
view2 = TimeView('results_sdt_E1/out.hdf5')

p = TRPlot(view1.mesh)

out_S = File('test/S_dif.pvd')
out_N = File('test/N_dif.pvd')

ff1 = FacetFunctionDouble(view1.mesh)
ff2 = FacetFunctionDouble(view2.mesh)

N_dif = Function(view1.V_cg)


for i in range(view1.num_steps):
  print i
  p.copy_tr_to_facet(view1.get_S(i), ff1)
  p.copy_tr_to_facet(view2.get_S(i), ff2)
  #out1 << ff1
  #out2 << ff2
  N_dif.vector()[:] = np.abs(view1.get_phi(i).vector().array() - view2.get_phi(i).vector().array())
  
  ff1.array()[:] = np.abs(ff2.array() - ff1.array())
  out_S << ff1
  out_N << N_dif