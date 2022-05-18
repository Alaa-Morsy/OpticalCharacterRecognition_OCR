########### Optical Character Recognition (OCR) ################
#   Name : Alaa Mohamed Morsy
#   Date: 18 May 2022
#   Version : V.1
#   Languge : Python
#   Libraries : OpenCV , Tesseract 5.0 alpha
################################################################

# import the necessary packages
from ctypes import sizeof
import numpy as np
import argparse
import cv2
from PIL import Image
import pytesseract
from colorama import Fore, Back, Style #to color the output in terminal
# identify colors
green = (0, 255, 0)
blue = (255, 0, 0)

#Get the input image as an argument -i
#Get the path of output .txt file   -t
#Get the path of output image       -o
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to input image")
ap.add_argument("-t", "--text", required=False,
	help="path of output .txt file")
ap.add_argument("-o", "--output", required=False,
	help="path of output image")
args = vars(ap.parse_args())

# load the input image from disk,
image = cv2.imread(args["input"])

#######Clarify the image for OCR##########
norm_img = np.zeros((image.shape[0], image.shape[1])) 
image_modified = cv2.normalize(image, norm_img, 0, 255, cv2.NORM_MINMAX)
image_modified = cv2.threshold(image_modified, 100, 255, cv2.THRESH_BINARY)[1]
image_modified = cv2.GaussianBlur(image_modified, (1, 1), 0)

#######Reading the image#######
# Simple image to text then split it to array
Total_string = pytesseract.image_to_string(image_modified)
print(Fore.BLUE + Total_string)    #display the detected text in blue 
print(Style.RESET_ALL)             #Reset print style
string = Total_string.split()

if len(string)==0 :
    print(Fore.RED + "SORRY : The Text Can't be Detected !!" )
    print(Style.RESET_ALL)
    exit()
# Get bounding box estimates => in form of string
#inside labels :=> char left bottom right top page
labels=pytesseract.image_to_boxes(image_modified)

output = image.copy() # have a copy of original image
h,w,c = image_modified.shape   # getting height , width , channels of image

####### Draw a rectangle surronding the word and write it above #####
j=0   #index for number of letters in a string
i=0   # index for number of strings in image
for b in labels.splitlines(): 
    b = b.split(' ')

    if b[0]!= string[i][j]:  # if the character is not from strings detected skip
        continue

    if j==0:
        left = int(b[1])       #getting the left coordinator of 1st char in a word
        bottom =h - int(b[2])  #initialize bottom
        top  = h- int(b[4])    #initialize top
       

    if bottom < (h - int(b[2])):  #getting the lowest bottom in word
        bottom =h - int(b[2])     
    
    if top > (h - int(b[4])):  #getting the highest top in word
        top =h - int(b[4]) 

    if j == len(string[i])-1 : #reaching the end of the word
        right = int(b[3])      #getting the right coordinator of last char in word
        
        #### Display on a copy of original image ####
        #have the whole word in a box
        output = cv2.rectangle(output, (left, bottom), (right, top), green, 2) 
        #writing the word above the box
        output = cv2.putText(output, string[i], (left,top), cv2.FONT_HERSHEY_SIMPLEX, 0.9, blue, 2)
        
        if i < len(string):   #if we didn't reach the end of the strings in image 
            i+=1
            j=0
           
    else:   
        j+=1  #get the next letter in string
    
        
######### Output #########
# show the output image and wait user to close it
cv2.imshow("Input", image)
# show the output image and wait user to close it
cv2.imshow("Output", output)
cv2.waitKey(0)

#write the output image to disk if asked
if (args["output"]!= None):
   print(Fore.GREEN + 'SUCCESS:The output image is added!!')
   print(Style.RESET_ALL)             #Reset print style
   cv2.imwrite(args["output"],output)
# Save the output text in .txt file if asked  
if (args["text"]!= None):
    print(Fore.GREEN + 'SUCCESS:The output text file is added!!')
    print(Style.RESET_ALL)             #Reset print style
    myText = open(args["text"],'w')
    myText.write(Total_string)
    myText.close()
