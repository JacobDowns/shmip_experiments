# -*- coding: utf-8 -*-
"""
SHMIP E simulations. 
"""

from dolfin import *
from constants import *
from channel_model_back import *
from dolfin import MPI, mpi_comm_world
import time
import numpy as np 

ns = [1]

MPI_rank = MPI.rank(mpi_comm_world())
# Input files 
input_files = ['../../inputs/E_channel/inputs_E' + str(n) + '.hdf5' for n in ns]

# Result output directories
result_dirs = ['results_E' + str(n) for n in ns]

# Subdomain containing only a single outlet point at terminus
def outlet_boundary(x, on_boundary):
  cond1 = abs(x[0]) < 5.0
  cond2 = abs(x[1]) < 5.0
  return cond1 and cond2


for n in range(len(ns)):
  
  ### Setup the model  
  model_inputs = {}
  model_inputs['input_file'] = input_files[n]
  model_inputs['out_dir'] = result_dirs[n] 
  model_inputs['constants'] = pcs
  #model_inputs['use_pi'] = False
  # Point boundary condition at the outlet
  model_inputs['point_bc'] = outlet_boundary
  # Create the sheet model
  model = ChannelModel(model_inputs)


  


 
 
