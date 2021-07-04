''' OCR -Optical Character Recognition or optical character reader
is the electronic or mechanical conversion of images of typed,
handwritten or printed text into machine-encoded text,
whether from a scanned document, a photo of a document, a scene-photo
or from subtitle text superimposed on an image.'''

""" The first step of ocr is using a scanner to process the physical form of
a document """

"""Once all pages are copied , OCR software converts the document into a
two- color, or black and white version"""


""" The scanned -in image or bitmap is analysed for light and dark areas ,
where dark areas are identified as characters that need to be recognised
and light areas are identified as background """

# Pattern recoginition or feature recoginition
# PyTesseract
#pip3 install PyTesseract

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recText(filename):
    text=pytesseract.image_to_string(Image.open(filename))
    return text
info=recText('Test.png')
print(info)
file=open("result.text","w")
file.write(info)
file.close()
print("written Successfull")
