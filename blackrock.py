from PIL import Image

input_file = "imageEmbedded.png"
output_file = "outputImage.png"

input_image = Image.open(input_file)
grayscale_image = input_image.convert("L")

grayscale_pixels = grayscale_image.load()

new_image = Image.new(input_image.mode, input_image.size)
new_pixels = new_image.load()

for i in range(input_image.size[0]):
    for j in range(input_image.size[1]):
        new_pixels[i, j] = (grayscale_pixels[i, j] & 0b00000011) << 6

new_image.save(output_file)