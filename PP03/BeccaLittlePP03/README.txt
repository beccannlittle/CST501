README

For any image, simply create a new variable and
set it equal to imread("FILENAME.png") and use
img_as_float on that variable.

From there, create variables for energy (using 
dual_gradient_energy) and seam (using find_seam)
and pass them into plot_seam. Example:


variable = imread("FILENAME.png")
img = img_as_float(variable)
energy = dual_gradient_energy(img)
seam = find_seam(img,energy)
plot_seam(img,seam,energy)


You can copy and paste the above into the main() 
function of my program, change the FILENAME, and 
the four plots should output.

The four plots are the original image, the energy
plot, the energy plot with seam displayed as a 
white line, and the final image with the seam
removed. 

I have also inserted print statements into the code.
I do not suggest you uncomment them for large images,
but for small test images such as the ones I provided
in main(), these print statements should give some 
insight into the inner workings of the code. Simply 
search for print and uncomment all lines. 