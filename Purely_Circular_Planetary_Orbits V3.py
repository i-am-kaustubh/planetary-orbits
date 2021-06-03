#importing libraries
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#defining  variables to store position cordinates
earth_x = []
earth_y = []

moon_x = []
moon_y = []

sun_x = []
sun_y = []

#writing constant values
earth_sun_dist = 1 #in AU
moon_earth_dist =  0.00257*5 #in AU #SCALE UP THIS VALUE TO SEE VISIBLE DIFFERENCE

earth_sun_period = 365 #days
moon_earth_period = 27 #days

fig, ax = plt.subplots()

earth_path, = ax.plot(0, 0)
moon_path, = ax.plot(0, 0)
sun, = ax.plot(0, 0, 'y')

def sun_moon_orbit(d): #pass days as 'd' 
  earth_x.append(earth_sun_dist * math.sin(d*2*np.pi/earth_sun_period))
  earth_y.append(earth_sun_dist * math.cos(d*2*np.pi/earth_sun_period))
  earth_path.set_xdata(earth_x)
  earth_path.set_ydata(earth_y)
  
  moon_x.append(earth_x[d] - moon_earth_dist * math.sin(d*2*np.pi/moon_earth_period))
  moon_y.append(earth_y[d] - moon_earth_dist * math.cos(d*2*np.pi/moon_earth_period))
  moon_path.set_xdata(moon_x)
  moon_path.set_ydata(moon_y)
  
  sun_x.append(earth_sun_dist * math.sin(d*2*np.pi/5)*0.01)
  sun_y.append(earth_sun_dist * math.cos(d*2*np.pi/5)*0.01)
  sun.set_xdata(sun_x)
  sun.set_ydata(sun_y)
  
  return earth_path, moon_path, sun,

animation = FuncAnimation(fig, func=sun_moon_orbit, frames=np.arange(0, 365, 1), interval=25)

plt.xlim([-2,2])
plt.ylim([-1.5,1.5])

plt.legend(['Earth','Moon', 'Sun'], loc = 1)

plt.xticks([])
plt.yticks([])



plt.show()