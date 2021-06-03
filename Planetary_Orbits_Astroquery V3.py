# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 12:20:05 2021

@author: Kaustubh
"""

#!pip install astropy
#!pip install astroquery

#importing libraries
#import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#from astropy.time import Time
from astroquery.jplhorizons import Horizons
import matplotlib.animation as animation
import matplotlib as mpl 
mpl.rcParams['animation.ffmpeg_path'] = r'C:\\Users\\Kaustubh\\Downloads\\ffmpeg-4.4-full_build\\bin\\ffmpeg.exe'

#defining  variables to store position cordinates
earth_x = []
earth_y = []

moon_x = []
moon_y = []

fig, ax = plt.subplots()

earth_path, = ax.plot(0, 0)
moon_path, = ax.plot(0,0)

time_dur = {'start' : '2021-01-01', 'stop' : '2021-12-31', 'step' : '1d'}
earth = Horizons(id=3, location="@sun", epochs=time_dur, id_type='id').vectors()
moon = Horizons(id=301, location="@sun", epochs=time_dur, id_type='id').vectors()

def sun_moon_orbit(d): #pass days as 'd'
  
  earth_x.append(earth['x'][d]) #x-co ordinate of earth's position
  earth_y.append(earth['y'][d]) #y-co ordinate of earth's position
  earth_path.set_xdata(earth_x)
  earth_path.set_ydata(earth_y)
  
  
  moon_x.append(moon['x'][d]) #x-co ordinate of moon's position
  moon_y.append(moon['y'][d]) #y-co ordinate of moon's position
  moon_path.set_xdata(moon_x)
  moon_path.set_ydata(moon_y)
  
  
  x_fov = [earth['x'][d] - 0.01 , earth['x'][d] + 0.01]
  y_fov = [earth['y'][d] - 0.01, earth['y'][d] + 0.01]
  
  plt.xlim([earth['x'][d] - 0.1 , earth['x'][d] + 0.1])
  plt.ylim([earth['y'][d] - 0.1, earth['y'][d] + 0.1])
  
  return earth_path, moon_path, x_fov, y_fov

animation1 = FuncAnimation(fig, func=sun_moon_orbit, frames=np.arange(1, 365, 1), interval=20)

#plt.xlim([-2,2])
#plt.ylim([-1.5,1.5])

#plt.xlim(x_fov)
#plt.ylim(y_fov)
plt.legend(['Earth','Moon'], loc = 1)

plt.xticks([])
plt.yticks([])

plt.show()


#Writer = animation.writers['ffmpeg']
#writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

#animation1.save('lines.mp4', writer=writer)
