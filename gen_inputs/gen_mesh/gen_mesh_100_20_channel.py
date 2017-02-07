from dolfin import *
from mshr import *
from pylab import *
from mshr import *
""" Rectangle mesh low res. """

# Build the polygonal domain
points = []
points.append(Point(array([0.0, 0.0])))
points.append(Point(array([100e3, 0.0])))
points.append(Point(array([100e3, 20e3])))
points.append(Point(array([0.0, 20e3])))
  
# Create the mesh
domain = Polygon(points)
mesh = generate_mesh(domain, 150) 
File('mesh_channel.xml') << mesh
File('mesh_channel.pvd') << mesh


