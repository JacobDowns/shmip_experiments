# -*- coding: utf-8 -*-
"""
Write results as netcdf files
"""

from time_view import *

ns = [1]

for n in ns:
  # Load steady state results file
  view = TimeView('results_C' + str(n) + '/out.hdf5')
  # Write results as netcdf file
  view.write_netcdf('results_netcdf/C' + str(n) + '_jdow', 'downs_C' + str(n))