import numpy as np
import os
import matplotlib.pyplot as plt
from math import fabs


f, (ax1, ax2) = plt.subplots(1, 2)
ax1.invert_yaxis()
ax2.invert_yaxis()
ax1.set_xlabel('Mv - Mi')
ax1.set_ylabel('Mi')
ax2.set_xlabel('Mv - Mi')
ax2.set_ylabel('Mi')
ax1.grid(True)
ax2.grid(True)
ax1.set_title("all mi")
ax2.set_title("Mi>=0.7")	

outdir = "testisomi"
isofiles=["isocz0004.dat" , "isocz001.dat",  "isocz004.dat" , "isocz008.dat", "isocz019.dat", "isocz030.dat"]


# Create the plot

if not os.path.exists(outdir):
	os.mkdir(outdir)

def floatRgb(mag, cmin, cmax):
	"""
	Return a tuple of floats between 0 and 1 for the red, green and
	blue amplitudes.
	"""
	try:
		# normalize to [0,1]
		x = float(mag-cmin)/float(cmax-cmin)
	except:
		# cmax = cmin
		x = 0.5
	blue = min((max((4*(0.75-x), 0.)), 1.))
	red  = min((max((4*(x-0.25), 0.)), 1.))
	green= min((max((4*fabs(x-0.5)-1., 0.)), 1.))
	return "#%02x%02x%02x" % (red*255, green*255, blue*255)

for isofile in isofiles:
	#I also need initial mass column..
	dataiso = np.genfromtxt(isofile, comments="#", usecols=(9,11,0,1), converters={0: lambda x: round(float(x),2)})
	dataiso[:,0] = dataiso[:,0] - dataiso[:,1]
	for age in np.unique(dataiso[:,2]):
		#because of dataiso in for condition I need to define other variable
		data=dataiso[dataiso[:,2]==age]
		data2=data[data[:,3]>0.7]
		colorstring = floatRgb(age, 7.8, 10.25)
		ax1.plot(data[:,0],data[:,1], "-" , markersize=1, color=colorstring ,  markeredgecolor='none')
		ax2.plot(data2[:,0],data2[:,1], "-" , markersize=1, color=colorstring ,  markeredgecolor='none')
		# Save the figure in a separate file
plt.savefig("allisomi.png" )






		

