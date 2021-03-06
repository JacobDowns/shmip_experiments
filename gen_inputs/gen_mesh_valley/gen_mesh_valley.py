from dolfin import *
from mshr import *
from valley_outline import *
from pylab import *
from mshr import *

""" Generate a valley glacier mesh for the SHMIP E experiments. """


xs, ys = valley_outline()
xs = xs[::-1]
ys = ys[::-1]
plot(xs, ys, 'ko', ms = 1)

# Build the polygonal domain
points = []

for i in range(len(xs)):
  points.append(Point(xs[i], ys[i]))
  
# Create the mesh
domain = Polygon(points)
mesh = generate_mesh(domain, 125) 
File('mesh_valley.xml') << mesh
File('mesh_valley.pvd') << mesh


