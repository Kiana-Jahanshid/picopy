import cv2
import numpy as np

def convert_image_to_watercolor(input_image):
    image = cv2.imread(input_image)
    image_resized = cv2.resize(image, None, fx=1.5, fy=1.5)

    #removing impurities from image
    image_cleared = cv2.medianBlur(image_resized, 3)
    #image_cleared = cv2.medianBlur(image_cleared, 3)
    image_cleared = cv2.medianBlur(image_cleared, 3)
    image_cleared = cv2.edgePreservingFilter(image_cleared, sigma_s=5)

    #Bilateral Image filtering 
    image_filtered = cv2.bilateralFilter(image_cleared, 5, 10, 5)
    for i in range(2):
        image_filtered = cv2.bilateralFilter(image_filtered, 9, 20, 10)
    for i in range(3):
        image_filtered = cv2.bilateralFilter(image_filtered, 11, 30, 10)
    for i in range(3):
        image_filtered = cv2.bilateralFilter(image_filtered, 15, 40, 10)
    for i in range(3):
        image_filtered = cv2.bilateralFilter(image_filtered, 15, 10, 10)

    #Sharpening the image using addWeighted()
    gaussian_mask= cv2.GaussianBlur(image_filtered, (5,5), 2)
    image_sharp = cv2.addWeighted(image_filtered, 1.5, gaussian_mask, -0.5, 0)
    image_sharp = cv2.addWeighted(image_sharp, 1.4, gaussian_mask, -0.2, 10)
    cv2.imwrite("watercolor.jpg" , img=image_sharp)
    cv2.imshow('Final Image', image_sharp)
    cv2.waitKey(0)


if __name__ == "__main__":
    input_image = "c1.jpg"
    watercolor_image = convert_image_to_watercolor(input_image=input_image)
    



'''
! pip install picopy
# from package_name import filename
from picopy import picopy
picopy.convert_to_watercolor("image.jpg")

'''