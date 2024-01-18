import numpy as np
from scipy.signal import convolve2d
from PIL import Image


# Load the image as a grayscale array
image = np.array(Image.open("D:\python\image processing with python\pillow\image\maazkhan.jpg").convert("L"))

# Define the 3x3 smoothing filter
filter = np.ones((4, 4)) /16

# Apply the filter to the image using convolve2d
filtered_image = convolve2d(image, filter, mode="same")

# Save the filtered image
Image.fromarray(filtered_image.astype(np.uint8)).save("filtered_example.jpg")



# Load the image as a grayscale array
image = np.array(Image.open("D:\python\image processing with python\pillow\image\samcurran.jpg").convert("L"))

# Define the 3x3 smoothing filter
filter = np.ones((4, 4)) /10

# Apply the filter to the image using convolve2d
filtered_image = convolve2d(image, filter, mode="same")

# Save the filtered image
Image.fromarray(filtered_image.astype(np.uint8)).save("filtered_example2.jpg")




