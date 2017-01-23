# -*- coding: utf-8 -*-
"""
SHMIP C simulations. 
"""

from dolfin import *
from constants import *
from sheet_model import *
from dolfin import MPI, mpi_comm_world
import time
import numpy as np 

ns = [3]

MPI_rank = MPI.rank(mpi_comm_world())
input_file = '../../inputs/C/steady_B5.hdf5'
result_dirs = ['results_C' + str(n) for n in ns]
ras = [0.25, 0.5, 1.0, 2.0]


for n in range(len(ns)):
  
  ### Setup the model
  
  model_inputs = {}
  model_inputs['input_file'] = input_file
  model_inputs['out_dir'] = result_dirs[n]
  model_inputs['constants'] = pcs
 
  # Create the sheet model
  model = SheetModel(model_inputs)
  model.newton_params['newton_solver']['maximum_iterations'] = 25
  
   # Set conductivity
  k = interpolate(Constant(1e-2), model.V_cg)
  model.set_k(k)
   
  # Melt
  m = Function(model.V_cg)
  # Array of zeros, same length as local array in m
  zs = np.zeros(len(m.vector().array()))
  # Uniform basal melt 
  runoff_basal = 7.93e-11
  # Relative amplitude 
  ra = ras[ns[n] - 1]
  # Seconds per day
  spd = pcs['spd']
  # Moulin input
  moulin_in = Function(model.V_cg)
  moulin_in.vector().set_local(model.m.vector().array() - runoff_basal)
  moulin_in.vector().apply("insert") 
  
  # Calculate melt
  def update_m(t):
    runoff = np.maximum(zs, moulin_in.vector().array()*(1.0 - ra*np.sin(2.0*np.pi*t/spd)))
    m.vector().set_local(runoff + 7.93e-11)
    m.vector().apply("insert")

  ### Run the simulation

  # End time
  T = 100.0 * spd
  # Time step
  dt = 5.0 * 60.0
  # Iteration count
  i = 0
  # Day
  day = 1
  
  # Time the run  
  start_time = time.time()
  
  # Put output for each year in a separate folder
  while day <= 100:
    
    pvd_dir = result_dirs[n] + '/day' + str(year) + '/'
    out_pfo = File(pvd_dir + 'pfo.pvd')
    out_h = File(pvd_dir + 'h.pvd')
    out_N = File(pvd_dir + 'N.pvd')
    
    # Run the model for a year
    while model.t < day * spd:  
      if MPI_rank == 0: 
        current_time = model.t / spd
        print 'Current time: ' + str(current_time)
        
      # Update melt
      update_m(model.t)
      model.set_m(m)
      
      model.step(dt)
      
      if i % 20 == 0:
        out_pfo << model.pfo
        out_h << model.h
        out_N << model.N
        
      if i % 20 == 0:
        model.checkpoint(['h', 'phi', 'N', 'm', 'q'])
      
      if MPI_rank == 0: 
        print
        
      i += 1
    
    end_time = time.time()
    np.savetxt(result_dirs[n] + '/Time_day' + str(day), np.array([start_time, end_time, end_time - start_time]))
    
    model.write_steady_file(result_dirs[n] + '/day' + str(day))
    year += 1
  

  model.write_steady_file(result_dirs[n] + '/steady_C' + str(ns[n]))

  end_time = time.time()
  np.savetxt(result_dirs[n] + '/Time_C' + str(ns[n]), np.array([start_time, end_time, end_time - start_time]))
  


 
 
