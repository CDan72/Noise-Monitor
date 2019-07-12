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

datestring = datetime.strftime(datetime.now(), '%Y/%m/%d')
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
asdf = datetime.now().minute + 1
while datetime.now().minute < asdf:
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

plt.savefig("graph.png")

print (" ")
print ("End of day")

wait.sleep(5)

import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.ehlo()

username='noisemonitor123@gmail.com'
password='NoiseMonitor123'
s.login(username,password)

sendto=['noisemonitor@googlegroups.com']

msg = MIMEMultipart()
msg["From"] = username
msg["To"] = sendto[0]
msg["Date"] = formatdate(localtime=True)
msg["Subject"] = f"Graph for {datestring}"

f = "/home/pi/Documents/Noise-Monitor/graph.png"
with open(f, "rb") as fil:
    part = MIMEApplication(
        fil.read(),
        Name=basename(f)
    )
# After the file is closed
part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
msg.attach(part)

s.sendmail(username, sendto, msg.as_string())

rslt=s.quit()

