import cv2
import pytesseract

#5mb
MAX_FILE_SIZE = 5*1024*1024

def ocr_core(img):
  # Configure custom options for Tesseract
  config = ('-l eng --oem 1 --psm 3')

  pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
  # Convert the image to text
  text = pytesseract.image_to_string(img, config=config)

  text = pytesseract.image_to_string(img)
  return text

# get_grayscale will convert image to grayscale image.
def get_grayscale(img):
  return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# remove_noise will remove noise from the image
def remove_noise(img):
  return cv2.medianBlur(img, 5)

# thresholding which tell if pixel is white or black.
def thresholding(img):
  return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# img = cv2.imread('image-2.png')
img = cv2.imread('download.jpg')
# img = get_grayscale(img)
# img = thresholding(img)
# img = remove_noise(img)
text = ocr_core(img)
print("text ->", text)