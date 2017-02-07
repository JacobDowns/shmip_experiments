from netCDF4 import Dataset
from pylab import *

""" Class for viewing shmip netcdf sheet model output. """

class NCView(object):
  
  def __init__(self, input_file):
    fh = Dataset(input_file, mode='r')
   
    self.times = fh.variables['time'][:]
    
    self.num_steps = len(self.times)
    
    # Nodal coordinates
    coords1 = fh.variables['coords1'][:]
    self.xs = coords1[0,:]
    self.ys = coords1[1,:]
    
    # Effective pressure
    self.N = fh.variables['N'][:]
    # Flux
    self.q = fh.variables['q'][:]
    # Sheet height
    self.h = fh.variables['h'][:]
    # Bed elevation 
    self.B = fh.variables['B'][:]
    # Ice thickness 
    self.H = fh.variables['H'][:]
    
    
  # Plot n at ith time step
  def plot_field_time(self, field, name, i):
    if i < self.num_steps:
      figure()
      tricontourf(self.xs, self.ys, field[i], 500)
      colorbar()
      savefig(name + '_' + str(i) + '.png', dpi = 600)
      
      
  # Plot unchanging field
  def plot_field_static(self, field, name):
    figure()
    tricontourf(self.xs, self.ys, field, 500)
    colorbar()
    savefig(name  + '.png', dpi = 600)
  
  
  # Plot effective pressure
  def plot_N(self, name, i):
    self.plot_field_time(self.N, name, i)
    
    
  # Plot flux
  def plot_q(self, name, i):
    self.plot_field_time(self.q, name, i)
    
  
  # Plot sheet height
  def plot_h(self, name, i):
    self.plot_field_time(self.h, name, i)
    

  # Plot bed elevation
  def plot_B(self, name):
    self.plot_field_static(self.B, name)
    
    
  # Plot ice thickness
  def plot_H(self, name):
    self.plot_field_static(self.H, name)

