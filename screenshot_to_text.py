from PIL import ImageGrab
from pytesseract import pytesseract
import platform

def create_screen_shot(filename, startX, startY, endX, endY):
    image = ImageGrab.grab(bbox=(startX,startY,endX,endY))
    image.save(filename)    
    return image

def image_to_text(startX, startY, endX, endY): 
    if platform.system() == 'Windows':
        # Defining paths to tesseract.exe
        # and the image we would be using
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        # Providing the tesseract executable
        # location to pytesseract library
        pytesseract.tesseract_cmd = path_to_tesseract
    img = create_screen_shot(r"Capture.png", startX, startY, endX, endY)     
       
    # Passing the image object to image_to_string() function
    # This function will extract the text from the image
    text = pytesseract.image_to_string(img)
    
    # Displaying the extracted text
    # print(text[:-1])
    return text
