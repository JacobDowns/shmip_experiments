# -*- coding: utf-8 -*-
"""
SHMIP D simulations. 
"""

from dolfin import *
from constants import *
from sheet_model import *
from dolfin import MPI, mpi_comm_world
import time
import numpy as np 

ns = [3]

MPI_rank = MPI.rank(mpi_comm_world())
# Input file is steady state from A1
input_file = '../../inputs/D/steady_A1.hdf5'
# Result output directories
result_dirs = ['results_D_alt' + str(n) for n in ns]

## Params

# Delta temps for each run
DTs = [-4, -2, 0, 2, 4]
spy = pcs['spy']
# Lapse rate (K / m)
lr = -0.0075 
# Degre day factor (m/K/s)
DDF = 0.01 / 86400.0 

for n in range(len(ns)):
  
  ### Setup the model
  
  model_inputs = {}
  model_inputs['input_file'] = input_file
  model_inputs['out_dir'] = result_dirs[n]
  model_inputs['constants'] = pcs

  # Create the sheet model
  model = SheetModel(model_inputs)

  # Temperature at 0m  
  def temp(t):
    return -16.0 * np.cos(2.0*pi/spy*t) - 5.0 + DTs[ns[n] - 1]

  # Melt
  m = Function(model.V_cg)
  # Array of zeros, same length as local array in m
  zs = np.zeros(len(m.vector().array()))
  # Calculate melt
  def update_m(t):    
    ms = np.maximum(zs, (model.H.vector().array()*lr + temp(t))*DDF) + 7.93e-11
    m.vector().set_local(ms)
    m.vector().apply("insert")

    
  ### Run the simulation
  
  # Seconds per day
  spd = pcs['spd']
  # Seconds per year
  spy = pcs['spy']
  # Time step
  dt = spd / 24.0
  # End time
  # Iteration count
  i = 0
  # Current years
  year = 1
  
  # Run the model for a year
  while model.t < (10.0*spy):  
    
    if MPI_rank == 0: 
      current_time = model.t / spd
      print 'Current time: ' + str(current_time)
    
    # Update melt
    update_m(model.t)
    model.set_m(m)
    
    if i % 24 == 0:
      model.checkpoint(['h', 'phi', 'N', 'm', 'q'])
      
    if i % (24*5) == 0:
      out_pfo << model.pfo
      out_h << model.h
      out_N << model.N
            
    model.step(dt)
    
    if MPI_rank == 0: 
      print
      
    i += 1
  
  model.write_steady_file()



  


 
 
