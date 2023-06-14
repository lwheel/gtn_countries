import pytesseract
from PIL import Image

# Load the image
image_path = 'KKMO-WINNERS21.PDF'  # Replace with the actual path to the image file
image = Image.open(image_path)

# Perform OCR using Tesseract
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)