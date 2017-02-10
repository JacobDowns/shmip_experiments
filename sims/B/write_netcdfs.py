# -*- coding: utf-8 -*-
"""
Write results as netcdf files
"""

from steady_view import *
from constants import *

ns = range(1,6)

for n in ns:
  # Load steady state results file
  view = SteadyView('results_hdf5/steady_B' + str(n) + '.hdf5')
  # Write results as netcdf file
  view.write_netcdf('results_netcdf/B' + str(n) + '_jdow', 'downs_B' + str(n), pcs['spd']*1000.0)