import pytesseract
from PIL import Image

# Load the image
image_path = '/Users/lilywheeler/Desktop/KKMO-WINNERS21-3.png'  # Replace with the actual path to the image file
image = Image.open(image_path)

text = pytesseract.image_to_string(image)

# Specify the file path to save the text
output_file_path = 'output1.txt'  # Replace with the desired output file path

# Save the extracted text to the file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(text)

# Print a success message
print('Text saved to:', output_file_path)