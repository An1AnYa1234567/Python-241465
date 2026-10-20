# Write a program to demonstrate Digital Image Filter and Color Converter Utility.
from PIL import Image, ImageFilter

# Open the input image
img = Image.open("input.jpg").convert("RGB")

print("Original Image Size:", img.size)

# 1. Grayscale conversion using RGB channels
gray = img.convert("L")
gray.save("grayscale.png")
print("Grayscale image saved.")

# 2. Black and white thresholding
threshold = 128
bw = gray.point(
    lambda pixel: 255 if pixel > threshold else 0
)
bw.save("black_white.png")
print("Black and white image saved.")

# 3. Apply a simple blur filter
blur = img.filter(ImageFilter.BLUR)
blur.save("blurred.png")
print("Blurred image saved.")

# 4. Display RGB values of the first pixel
pixels = img.load()
print("First Pixel RGB:", pixels[0, 0])

print("Image processing completed successfully.")