# OpticalCharacterRecognition_OCR
An Optical character recognition is a character detector with extracts text from an image

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
