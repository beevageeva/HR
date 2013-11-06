import numpy as np
import os
import matplotlib.pyplot as plt


f, (ax1, ax2) = plt.subplots(1, 2)
ax1.invert_yaxis()
ax2.invert_xaxis()

outdir = "testiso"
isofiles=["isocz0004.dat" , "isocz001.dat",  "isocz004.dat" , "isocz008.dat", "isocz019.dat", "isocz030.dat"]


# Create the plot

if not os.path.exists(outdir):
		os.mkdir(outdir)

for isofile in isofiles:
	#I also need initial mass column..
	dataiso = np.genfromtxt(isofile, comments="#", usecols=(9,11,0,3,4), converters={0: lambda x: round(float(x),2)})
	dataiso[:,0] = dataiso[:,0] - dataiso[:,1]
	for age in np.unique(dataiso[:,2]):
		ax1.cla();
		ax2.cla();
		ax1.set_xlabel('Mv - Mi')
		ax1.set_ylabel('Mi')
		ax2.set_xlabel('Temp')
		ax2.set_ylabel('Luminosity')
		ax1.grid(True)
		ax2.grid(True)
		#ax1.set_yscale("log")
		#ax1.set_xscale("log")
		plt.title("isocrone file=" + isofile+", age=" + "{:3.3f}".format(10**(age-9))+ "GYears" )
		data=dataiso[dataiso[:,2]==age]
		ax1.plot(data[:,0],data[:,1], "-" , markersize=1, color="#ff0000" ,  markeredgecolor='none')
		#temperature and luminosity are logaritmic 
		ax2.plot(data[:,4],data[:,3], "-" , markersize=1, color="#ff0000" ,  markeredgecolor='none')
		# Save the figure in a separate file
		filename = isofile[:-4] + "_" + str(age) + '.png'
		plt.savefig(os.path.join(outdir,filename) )






		

