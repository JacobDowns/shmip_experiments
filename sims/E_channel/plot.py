# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 14:59:49 2017

@author: jake
"""

from time_view import *
from tr_plot import *
import numpy as np

view = TimeView('results_new_rk_E1/out.hdf5')
p = TRPlot(view.mesh)

out_S = File('test/S_dif.pvd')
out_N = File('test/N_dif.pvd')

ff = FacetFunctionDouble(view.mesh)


for i in range(view.num_steps):
  print i
  p.copy_tr_to_facet(view.get_S(i), ff)
  out_S << ff