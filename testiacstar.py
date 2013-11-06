import numpy as np
import os,sys
import matplotlib.pyplot as plt



datafile = sys.argv[1]
mydatafile = sys.argv[2]

print "datafile " + datafile

f, (ax1, ax2) = plt.subplots(1, 2, sharex=True)
ax1.invert_yaxis()
ax2.invert_yaxis()
data = np.genfromtxt(datafile, comments="#", usecols=(16, 18))
data[:,0] = data[:,0] - data[:,1]
ax1.set_xlabel('Mv - Mi')
ax1.set_ylabel('Mi')
ax1.grid(True)
ax1.set_title(datafile)
ax1.plot(data[:,0],data[:,1], "ko" , markersize=1)

ax2.set_xlabel('Mv - Mi')
ax2.set_ylabel('Mi')
ax2.grid(True)
ax2.set_title(mydatafile)
mydata = np.genfromtxt(mydatafile, comments="#")
ax2.plot(mydata[:,0],mydata[:,1], "ko", markersize=1)

#plt.show()
plt.savefig(datafile+".png" )






		

