# OpticalCharacterRecognition_OCR
An Optical character recognition is a character detector which extracts text from an image

- Date: 18 May 2022 Version : V.1
- Languge : Python -> I used python3.10.4
- Libraries : OpenCV , Tesseract 5.0 alpha
- Allowed input image extension : jpeg, png, gif, bmp, tiff
- Allowed outputs: 
   => image with text detected in box 
   => text file with the detected text
 
# Pre-requests:
to install OpenCV library 
```
pip install opencv-python
```
Note : Python-tesseract is an optical character recognition (OCR) tool for python. That is, it will recognize and “read” the text embedded in images.
to install Python-tesseract
```
pip install pytesseract
```
If you don't have tesseract executable in your PATH, include the following:
```
pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
```
# Usage
1. Open your ``` cmd```
2.  Be in the file directory using cd command if in Windows
   Example
```
> cd g:/Self_Dev/TSF_Intern/ObjectDetector_OCR/FamiliarWOpenCV/TSF_Task1
```
2. Make sure you have python exeutable in your PATH
3. Run the program 
```
> python .\TSF_Task1.py -i <PATH of input image>
#Example
> python .\TSF_Task1.py -i .\image1.jpg 
# Have an output in .txt file
> python .\TSF_Task1.py -i .\image1.jpg  -t .\all.txt
# Have an output in image file
> python .\TSF_Task1.py -i .\image1.jpg  -o .\out_image.jpg
```
# Note: You can use -h/ --help
```
> python .\TSF_Task1.py -h 
usage: TSF_Task1.py [-h] -i INPUT [-t TEXT] [-o OUTPUT]

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        path to input image
  -t TEXT, --text TEXT  path of output .txt file
  -o OUTPUT, --output OUTPUT
                        path of output image
```
