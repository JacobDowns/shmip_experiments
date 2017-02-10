# -*- coding: utf-8 -*-
"""
Write results as netcdf files
"""

from steady_view import *
from constants import *

ns = [1,2,3,4,5,6]

for n in ns:
  # Load steady state results file
  view = SteadyView('results_hdf5/steady_A' + str(n) + '.hdf5')
  # Write results as netcdf file
  view.write_netcdf('results_netcdf/A' + str(n) + '_jdow', 'downs_A' + str(n), end_time = pcs['spd']*1500.0)