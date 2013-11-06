import numpy as np
import os
import matplotlib.pyplot as plt
from math import fabs


plt.gca().invert_yaxis()

outdir = "testisoz"
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
		# normalize to [0,1] and increase difference for small values
		x = float(mag-cmin)/float(cmax-cmin) * float(cmax) / float(mag)
	except:
		# cmax = cmin
		x = 0.5
	blue = min((max((4*(0.75-x), 0.)), 1.))
	red  = min((max((4*(x-0.25), 0.)), 1.))
	green= min((max((4*fabs(x-0.5)-1., 0.)), 1.))
	return "#%02x%02x%02x" % (red*255, green*255, blue*255)

for age in np.arange(7.8,10.3,0.05):
	#I also need initial mass column..
	plt.cla();
	plt.xlabel('Mv - Mi')
	plt.ylabel('Mi')
	plt.grid(True)
	plt.title("age=" + str(age) )
	for isofile in isofiles:
		z=int(isofile[5:-4].lstrip("0"))
		dataiso = np.genfromtxt(isofile, comments="#", usecols=(9,11,0,1), converters={0: lambda x: round(float(x),2)})
		dataiso[:,0] = dataiso[:,0] - dataiso[:,1]
		#because of float precision I must define it in an interval???
		delta = 0.01
		dataiso=dataiso[(age - delta) < dataiso[:,2]]
		dataiso=dataiso[dataiso[:,2] <  (age + delta)]
		colorstring = floatRgb(z, 4, 300)
		plt.plot(dataiso[:,0],dataiso[:,1], "-" , markersize=1, color=colorstring ,  markeredgecolor='none', label="z=" + isofile[5:-4])
		plt.legend()
		# Save the figure in a separate file
	filename =  str(age)  + '.png'
	plt.savefig(os.path.join(outdir,filename) )






		

