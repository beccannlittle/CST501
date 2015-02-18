from pylab import *
from skimage import img_as_float
import math

def dual_gradient_energy(img):
	"""Return a W x H array of floats, the energy at each pixel in the passed image."""
	h = img.shape[0]
	w = img.shape[1]
	R = img[:,:,0]
	G = img[:,:,1]
	B = img[:,:,2]
	dxRed = [[[] for _ in xrange(w)] for _ in xrange(h)]
	dyRed = [[[] for _ in xrange(w)] for _ in xrange(h)]
	dxGreen = [[[] for _ in xrange(w)] for _ in xrange(h)]
	dyGreen = [[[] for _ in xrange(w)] for _ in xrange(h)]
	dxBlue = [[[] for _ in xrange(w)] for _ in xrange(h)]
	dyBlue = [[[] for _ in xrange(w)] for _ in xrange(h)]
	energy = [[[] for _ in xrange(w)] for _ in xrange(h)]
	for i in range(0, h):
		dxRed[i][0] 		= R[i][1]-R[i][w-1]
		dxRed[i][0] 		= dxRed[i][0]*dxRed[i][0]
		dxRed[i][w-1] 		= R[i][0]-R[i][w-2]
		dxRed[i][w-1] 		= dxRed[i][w-1]*dxRed[i][w-1]
		dxGreen[i][0] 		= G[i][1]-G[i][w-1]
		dxGreen[i][0] 		= dxGreen[i][0]*dxGreen[i][0]
		dxGreen[i][w-1] 	= G[i][0]-G[i][w-2]
		dxGreen[i][w-1] 	= dxGreen[i][w-1]*dxGreen[i][w-1]
		dxBlue[i][0] 		= B[i][1]-B[i][w-1]
		dxBlue[i][0] 		= dxBlue[i][0]*dxBlue[i][0]
		dxBlue[i][w-1] 		= B[i][0]-B[i][w-2]
		dxBlue[i][w-1] 		= dxBlue[i][w-1]*dxBlue[i][w-1]

		energy[i][0] 		= dxRed[i][0]+dxGreen[i][0]+dxBlue[i][0]
		energy[i][w-1] 		= dxRed[i][w-1]+dxGreen[i][w-1]+dxBlue[i][w-1]

		for j in range(1, w-1):
			dxRed[i][j] 	= R[i][j+1]-R[i][j-1]
			dxRed[i][j] 	= dxRed[i][j]*dxRed[i][j]
			dxGreen[i][j] 	= G[i][j+1]-G[i][j-1]
			dxGreen[i][j] 	= dxGreen[i][j]*dxGreen[i][j]
			dxBlue[i][j] 	= B[i][j+1]-B[i][j-1]
			dxBlue[i][j] 	= dxBlue[i][j]*dxBlue[i][j]

			energy[i][j] 	= dxRed[i][j]+dxGreen[i][j]+dxBlue[i][j]

	for i in range(0,w):
		dyRed[0][i] 		= R[1][i]-R[h-1][i]
		dyRed[0][i] 		= dyRed[0][i]*dyRed[0][i]
		dyRed[h-1][i] 		= R[0][i]-R[h-2][i]
		dyRed[h-1][i] 		= dyRed[h-1][i]*dyRed[h-1][i]
		dyGreen[0][i] 		= G[1][i]-G[h-1][i]
		dyGreen[0][i] 		= dyGreen[0][i]*dyGreen[0][i]
		dyGreen[h-1][i] 	= G[0][i]-G[h-2][i]
		dyGreen[h-1][i] 	= dyGreen[h-1][i]*dyGreen[h-1][i]
		dyBlue[0][i] 		= B[1][i]-B[h-1][i]
		dyBlue[0][i] 		= dyBlue[0][i]*dyBlue[0][i]
		dyBlue[h-1][i] 		= B[0][i]-B[h-2][i]
		dyBlue[h-1][i] 		= dyBlue[h-1][i]*dyBlue[h-1][i]

		energy[0][i] 	   += dyRed[0][i]+dyGreen[0][i]+dyBlue[0][i]
		energy[h-1][i]     += dyRed[h-1][i]+dyGreen[h-1][i]+dyBlue[h-1][i]

		for j in range(1, h-1):
			dyRed[j][i] 	= R[j+1][i]-R[j-1][i]
			dyRed[j][i] 	= dyRed[j][i]*dyRed[j][i]
			dyGreen[j][i] 	= G[j+1][i]-G[j-1][i]
			dyGreen[j][i] 	= dyGreen[j][i]*dyGreen[j][i]
			dyBlue[j][i] 	= B[j+1][i]-B[j-1][i]
			dyBlue[j][i] 	= dyBlue[j][i]*dyBlue[j][i]

			energy[j][i]   += dyRed[j][i]+dyGreen[j][i]+dyBlue[j][i]
	print("Energy is: ")
	print(energy)
	return energy

def find_seam(img,energy):
	"""Return an array of H integers, for each row of the passed image return the column of the seam (lowest energy path)."""
	h = img.shape[0]
	w = img.shape[1]
	shortestPath = [[[[] for _ in range(2)] for _ in xrange(w)] for _ in xrange(h)]
	for j in range(0,w):
		shortestPath[0][j][0] = -1
		shortestPath[0][j][1] = energy[0][j]
		for i in range(1,h):
			shortestPath[i][j][0] = -1
			shortestPath[i][j][1] = float("inf")
	for j in range(0,w):
		for i in range(0,h-1):
			if (j == 0):
				if (shortestPath[i][j][1] < shortestPath[i][j+1][1]):
					shortestPath[i+1][j][0] = j
					shortestPath[i+1][j][1] = shortestPath[i][j][1]+energy[i+1][j]
				else:
					shortestPath[i+1][j][0] = j+1
					shortestPath[i+1][j][1] = shortestPath[i][j+1][1]+energy[i+1][j]
			if (j == w-1):
				if (shortestPath[i][j-1][1] < shortestPath[i][j][1]):
					shortestPath[i+1][j][0] = j-1
					shortestPath[i+1][j][1] = shortestPath[i][j-1][1]+energy[i+1][j]
				else:
					shortestPath[i+1][j][0] = j
					shortestPath[i+1][j][1] = shortestPath[i][j][1]+energy[i+1][j]
			else:
				if (shortestPath[i][j-1][1] < shortestPath[i][j][1]):
					if (shortestPath[i][j-1][1] < shortestPath[i][j+1][1]):
						shortestPath[i+1][j][0] = j-1
						shortestPath[i+1][j][1] = shortestPath[i][j-1][1]+energy[i+1][j]
					else: 
						shortestPath[i+1][j][0] = j+1
						shortestPath[i+1][j][1] = shortestPath[i][j+1][1]+energy[i+1][j]
				else:
					if (shortestPath[i][j][1] < shortestPath[i][j+1][1]):
						shortestPath[i+1][j][0] = j
						shortestPath[i+1][j][1] = shortestPath[i][j][1]+energy[i+1][j]
					else:
						shortestPath[i+1][j][0] = j+1
						shortestPath[i+1][j][1] = shortestPath[i][j+1][1]+energy[i+1][j]
				
	optimal = (-1,float("inf"))
	for j in range(0,w):
		if (shortestPath[h-1][j][1] < optimal[1]):
			optimal = (j, shortestPath[h-1][j][1])
	seam = [[] for _ in xrange(h)]
	seam[h-1] = optimal[0]
	for i in range(h-2,-1,-1):
		seam[i] = shortestPath[i+1][seam[i+1]][0]
	print("Seam is:")
	print(seam)
	return seam

def remove_seam(img,seam):
	"""Modify passed image in-place and return a W-1 x H x 3 slice - the image minus the seam."""
	h = img.shape[0]
	w = img.shape[1]

	newImage = [[[] for _ in xrange(w-1)] for _ in xrange(h)]
	for i in range(0,h):
		currentJ = 0
		for j in range(0,w):
			if (j != seam[i]):
				newImage[i][currentJ][:] = img[i][j][:]
				currentJ = currentJ+1
	print("The image without the seam is: ")
	print(newImage)
	return newImage

def plot_seam(img,seam,energy):
	"""Plot the original image, its energy function, a visualization of the seam, and the new image with seam removed."""
	h = img.shape[0]
	w = img.shape[1]

	figure()
	gray()

	subplot(2,2,1); imshow(img); title('RGB')

	maxEnergy = 0;
	for i in range(0,h):
		for j in range(0,w):
			if (energy[i][j] > maxEnergy):
				maxEnergy = energy[i][j]
	energyImage = [[[] for _ in xrange(w)] for _ in xrange(h)]
	for i in range(0,h):
		for j in range(0,w):
			energyImage[i][j] = math.floor(energy[i][j]/maxEnergy*255)
	subplot(2,2,2); imshow(energyImage); title('energy')

	seamImage = energyImage
	for i in range(0,h):
		seamImage[i][seam[i]] = 255.0
	subplot(2,2,4); imshow(seamImage); title('seam')

	newImage = remove_seam(img,seam)
	subplot(2,2,3); imshow(newImage); title('new')

	show()

def main():
	"""Use dynamic programming to find the seam for test images and plot relevant visualizations."""
	surfing = imread("HJoceanSmall.png")
	small1 = [[[255.0,101.0,51.0],[255.0,101.0,153.0],[255.0,101.0,255.0]],
		   	  [[255.0,153.0,51.0],[255.0,153.0,153.0],[255.0,153.0,255.0]],
		   	  [[255.0,203.0,51.0],[255.0,204.0,153.0],[255.0,205.0,255.0]],
		   	  [[255.0,255.0,51.0],[255.0,255.0,153.0],[255.0,255.0,255.0]]]
	small2 = [[[97.0,82.0,107.0],[220.0,172.0,141.0],[243.0,71.0,205.0],[129.0,173.0,222.0],[225.0,40.0,209.0],[66.0,109.0,219.0]],
		   	  [[181.0,78.0,68.0],[15.0,28.0,216.0],[245.0,150.0,150.0],[177.0,100.0,167.0],[205.0,205.0,177.0],[147.0,58.0,99.0]],
		   	  [[196.0,224.0,21.0],[166.0,217.0,190.0],[128.0,120.0,162.0],[104.0,59.0,110.0],[49.0,148.0,137.0],[192.0,101.0,89.0]],
			  [[83.0,143.0,103.0],[110.0,79.0,247.0],[106.0,71.0,174.0],[92.0,240.0,205.0],[129.0,56.0,146.0],[121.0,111.0,147.0]],
			  [[82.0,157.0,137.0],[92.0,110.0,129.0],[183.0,107.0,80.0],[89.0,24.0,217.0],[207.0,69.0,32.0],[156.0,112.0,31.0]]]
	
	img1 = img_as_float(small1)
	print("For the first small data set,")
	print("The image is: ")
	print(img1)
	energy1 = dual_gradient_energy(img1)
	seam1 = find_seam(img1,energy1)
	plot_seam(img1,seam1,energy1)

	img2 = img_as_float(small2)
	print("For the second small data set,")
	print("The image is: ")
	print(img2)
	energy2 = dual_gradient_energy(img2)
	seam2 = find_seam(img2,energy2)
	plot_seam(img2,seam2,energy2)

	img3 = img_as_float(surfing)
	energy3 = dual_gradient_energy(img3)
	seam3 = find_seam(img3,energy3)
	plot_seam(img3,seam3,energy3)
	

if __name__ == '__main__':
	main()

