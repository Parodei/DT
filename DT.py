import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#Earth ellipsoid IERS (2003)
R_equator = 6378.1366; # Equatorial radius (km)
R_polar = 6356.7519; # Polar radius (km)
Inv_flat = 298.25642; # Inverse flattening

# Initial parameters of craft
V_i = 1000; #[m/s]
X_i = 0;
Y_i = 0;
Z_i = 0;
H = 100;

X_i = -(R_equator+H);
Y_i = 0;
Z_i = 0;

u = np.linspace(0,2*np.pi, 100).reshape(100, 1) # the angle of the projection in the xy-plane
v = np.linspace(0, np.pi, 100).reshape(-1, 100) # the angle from the polar axis, ie the polar angle

# Transformation formulae for a spherical coordinate system.
z_earth_inertion = R_equator*np.sin(v)*np.cos(u)
x_earth_inertion = R_equator*np.sin(v)*np.sin(u)
y_earth_inertion = R_polar *np.cos(v)

fig = plt.figure(figsize=plt.figaspect(1))  # Square figure
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(z_earth_inertion, x_earth_inertion, y_earth_inertion, color ='green')
ax.scatter(Z_i,X_i,Y_i,color = 'black')
plt.show()