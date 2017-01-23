# -*- coding: utf-8 -*-
"""
Write results as netcdf files
"""

from steady_view import *

ns = [1,2,3,4,5]

for n in ns:
  # Load steady state results file
  view = SteadyView('results_E' + str(n) + '/steady_E' + str(n) + '.hdf5')
  # Write results as netcdf file
  view.write_netcdf('results_netcdf/E' + str(n), 'Jacob Z Downs, E' + str(n))