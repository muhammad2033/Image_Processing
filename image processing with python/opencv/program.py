import cv2

# Load the grayscale image
img_gray = cv2.imread('maazkhan.jpg', cv2.IMREAD_GRAYSCALE)

# Convert the grayscale image to color using cv2.cvtColor()
img_color = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)

# Display the color image
cv2.imshow('Color Image', img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
