# -*- coding: utf-8 -*-
"""
Loads an hdf5 results file. Writes a netcdf file. 
"""

from dolfin import *
from constants import *
from netCDF4 import Dataset
import numpy as np

class TimeView(object):
  
  def __init__(self, input_file):

    # Load a results file
    self.input_file = HDF5File(mpi_comm_world(), input_file, 'r') 

    # Load the mesh
    self.mesh = Mesh()
    self.input_file.read(self.mesh, "mesh", False)  
    self.V_cg = FunctionSpace(self.mesh, "CG", 1)
    self.V_tr = FunctionSpace(self.mesh, FiniteElement("Discontinuous Lagrange Trace", "triangle", 0))
    
    
    # Get the number of time steps
    self.num_steps = 0
    try:
      self.num_steps = self.input_file.attributes("h")['count']
    except:
      raise Exception("Not a results file.")
      sys.exit(1)
    
    # Bed
    self.B = Function(self.V_cg)
    self.input_file.read(self.B, "B")
    
    # Thickness    
    self.H = Function(self.V_cg)
    self.input_file.read(self.H, "H")
    
    # Sliding speed
    self.u_b = Function(self.V_cg)
    self.input_file.read(self.u_b, "u_b_0")
    
    # Sliding speed
    self.h = Function(self.V_cg)
    # Potential
    self.phi = Function(self.V_cg)
    # Effective pressure
    self.N = Function(self.V_cg)
    # Flux
    self.q = Function(self.V_cg)
    # Melt rate
    self.m = Function(self.V_cg)
    # Pressure as a fraction of overburden
    self.pfo = Function(self.V_cg)
    # Channel cross sectional area
    self.S = Function(self.V_tr)
    # Xi
    self.Pi = Function(self.V_tr)
    # Derivative of pressure along edges
    self.dpw_ds = Function(self.V_tr)
    # Derivative of phi along edges
    self.dphi_ds = Function(self.V_tr)
    # f
    self.f = Function(self.V_tr)
    # q_c
    self.q_c = Function(self.V_tr)
    # Channel flux
    self.Q = Function(self.V_tr)
    
    # Potential at 0 pressure
    phi_m = project(pcs['rho_w'] * pcs['g'] * self.B, self.V_cg)
    # Ice overburden pressure
    p_i = project(pcs['rho_i'] * pcs['g'] * self.H, self.V_cg)
    # Potential at overburden pressure
    self.phi0 = project(phi_m + p_i, self.V_cg)
    
    # Vertex coordinates
    self.coords = self.V_cg.tabulate_dof_coordinates().reshape(self.V_cg.dim(), 2)
    self.coords_x = self.coords[:,0]
    self.coords_y = self.coords[:,1]
    
  
  # Get Pi at the ith time step
  def get_Pi(self, i):
    if i < self.num_steps:
      self.input_file.read(self.Pi, "Pi/vector_" + str(i))
      return self.Pi
      
  
  # Get Q at the ith time step
  def get_Q(self, i):
    if i < self.num_steps:
      self.input_file.read(self.Q, "Q/vector_" + str(i))
      return self.Q
      
      
  # Get dpw_ds at the ith time step
  def get_dpw_ds(self, i):
    if i < self.num_steps:
      self.input_file.read(self.dpw_ds, "dpw_ds/vector_" + str(i))
      return self.dpw_ds

      
  # Get dpw_ds at the ith time step
  def get_dphi_ds(self, i):
    if i < self.num_steps:
      self.input_file.read(self.dphi_ds, "dphi_ds/vector_" + str(i))
      return self.dphi_ds
      
      
  # Get f at the ith time step
  def get_f(self, i):
    if i < self.num_steps:
      self.input_file.read(self.f, "f/vector_" + str(i))
      return self.f

      
  # Get q_c at the ith time step
  def get_q_c(self, i):
    if i < self.num_steps:
      self.input_file.read(self.q_c, "q_c/vector_" + str(i))
      return self.q_c

    
  # Get ith time step
  def get_t(self, i):
    if i < self.num_steps:
      attr = self.input_file.attributes("h/vector_" + str(i))
      return attr['timestamp']


  # Get phi at the ith time step
  def get_phi(self, i):
    if i < self.num_steps:
      self.input_file.read(self.phi, "phi/vector_" + str(i))
      return self.phi

      
  # Get pfo at the ith time step
  def get_pfo(self, i):
    if i < self.num_steps:
      self.input_file.read(self.pfo, "pfo/vector_" + str(i))
      return self.pfo
      
      
  # Get N at the ith time step
  def get_N(self, i):
    if i < self.num_steps:
      self.input_file.read(self.N, "N/vector_" + str(i))
      return self.N
        
  
  # Get h at the ith time step
  def get_h(self, i):
    if i < self.num_steps:
      self.input_file.read(self.h, "h/vector_" + str(i))
      return self.h
      
      
  # Get S at the ith time step
  def get_S(self, i):
    if i < self.num_steps:
      self.input_file.read(self.S, "S/vector_" + str(i))
      return self.S
        
  
  # Get m at the ith time step
  def get_m(self, i):
    if i < self.num_steps:
      self.input_file.read(self.m, "m/vector_" + str(i))
      return self.m
      
  
  # Get q at the ith time step
  def get_q(self, i):
    if i < self.num_steps:
      self.input_file.read(self.q, "q/vector_" + str(i))
      return self.q
        
        
  # Get the total melt input at the ith time step
  def get_total_m(self, i):
    if i < self.num_steps:
      self.get_m(i)
      return assemble(self.m * dx(self.mesh))
        
        
  # Compute the volume of water in the sheet at the ith time
  def get_sheet_volume(self, i):
    if i < self.num_steps:
      self.get_h(i)
      return assemble(self.h * dx(self.mesh))
      
      
  # Compute spatially averaged pfo at ith time step
  def get_avg_pfo(self, i):
    if i < self.num_steps:
      self.get_pfo(i)
      return assemble(self.pfo * dx(self.mesh)) / assemble(1.0 * dx(self.mesh))
    
    
  
  # Write a netcdf file with the results
  def write_netcdf(self, out_file, title, steps = None):
    if steps is None:
      steps = self.num_steps   

    root = Dataset(out_file + '.nc', 'w')
    
    ## Dimensions
    
    # Time
    root.createDimension('time', None)
    # Spatial dimension of model 
    root.createDimension('dim', 2)
    # Number of nodes in mesh
    root.createDimension('index1', self.V_cg.dim())
    
    
    ## Variables
    
    # Time
    times = root.createVariable('time', 'f8', ('time',))
    times.units = 's'
    times.long_name = 'time'
    
    start_index = self.num_steps - steps
    
    for i in range(steps):
      index = start_index + i
      times[i] = self.get_t(index)
      
    print self.get_t(0)
    quit()
  
    # Node coordinates
    coords1 = root.createVariable('coords1', 'f8', ('dim', 'index1'))
    coords1.units = 'm'
    coords1.long_name = 'node coordinates'
    coords1[:] = self.coords.T
    
    # Bed
    B = root.createVariable('B', 'f8', ('index1',))
    B.units = 'm'
    B.long_name = 'bed elevation'
    B[:] = self.B.vector()[:]    
    
    # Ice thickness
    H = root.createVariable('H', 'f8', ('index1',))
    H.units = 'm'
    H.long_name = 'ice thickness'
    H[:] = self.H.vector()[:]
    
    # Effective pressure
    N = root.createVariable('N', 'f8', ('time', 'index1',))
    N.units = 'Pa'
    N.long_name = 'effective pressure'
    
    # Sheet thickness
    h = root.createVariable('h', 'f8', ('time', 'index1',))
    h.units = 'm'
    h.long_name = 'water sheet thickness'
    
    # Water sheet discharge
    q = root.createVariable('q', 'f8', ('time', 'index1',))
    q.units = 'm^2/s'
    q.long_name = 'water sheet discharge'
    
    
    ## Write time dependent variables
    
    for i in range(steps):
      index = start_index + i
      
      # Get time dependent variables at ith time step
      self.get_N(index)
      self.get_h(index)
      self.get_q(index)

      # Write data to netcdf
      N[i,:] = self.N.vector().array()
      h[i,:] = self.h.vector().array()
      q[i,:] = self.q.vector().array()
    
    ## Global attributes
    root.title = title
    root.meshtype = 'unstructured'
    root.institution = 'Jacob Z Downs, UM'
    root.source = 'https://github.com/JacobDowns/SheetModel/tree/shmip'
    root.references = 'Schoof et al. 2012, DOI: 10.1017/jfm.2012.165'
    
    root.close() 
    