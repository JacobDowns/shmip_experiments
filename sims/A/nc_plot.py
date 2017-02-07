# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 13:26:08 2017

@author: jake
"""

from nc_view import *

for i in range(1,7):
  input_file = 'results_netcdf/A' + str(i) + '_jdow.nc'
  view = NCView(input_file)
  view.plot_N('images/A' + str(i) + '_N', 0)
  view.plot_h('images/A' + str(i) + '_h', 0)
  view.plot_q('images/A' + str(i) + '_q', 0)
  
  
  

