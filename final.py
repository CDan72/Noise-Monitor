#!/usr/bin/python3
import time as wait
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd 
import png

num = 66
fs = 44100
plotx = []
ploty = []

datestring = datetime.strftime(datetime.now(), '%Y%m%d')
timestring = wait.strftime('%H:%M:%S')

print (datestring)
print (timestring)
print (" ")
def point(seconds):
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    mx = np.max(myrecording)
    return mx

print ("Start of day")
print (" ")
  
while datetime.now().hour < 18:
    # Get sound level
    a = point(10)
    # Compute x as time as fractions of an hour
    n = datetime.now ()
    h = n.hour
    m = n.minute
    s = n.second
    t = h + m / 60.0 + s / 3600.0
    plotx.append (t)
    ploty.append (a)
    print (t, a)
    
plt.plot (plotx, ploty)
plt.xlabel ('time')
plt.ylabel ('max points')
plt.ylim (0, 1)
plt.grid(True)

plt.savefig("Data-For-" + datestring + ".png")

print (" ")
print ("End of day")

wait.sleep(3)
