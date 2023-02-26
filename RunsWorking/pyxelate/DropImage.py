import PIL
from PIL import Image, ImageDraw, ImageFilter

CharDude = Image.open('result (1).png')
person = Image.open('pixel.png')

reSizedPerson = person.resize((450,253), resample=None, box=None, reducing_gap=None)

# Get the dimensions of the resized person image
width, height = reSizedPerson.size

# Calculate the crop box to remove 10% of the width from both sides
left = int(width * 0.2)
upper = 0
right = int(width * 0.9)
lower = height

# Crop the resized person image
im_crop = reSizedPerson.crop((left, upper, right, lower))

# Save the cropped image to a file
im_crop.save('cropped_person.png')

# Create a copy of CharDude to place the cropped person image on
CharDude_copy = CharDude.copy()

# Calculate the position to place the cropped person image on CharDude_copy
x_offset = 80
y_offset = 65

# Paste the cropped person image onto CharDude_copy
CharDude_copy.paste(im_crop, (x_offset, y_offset))

# Save the modified image to a file
CharDude_copy.save('modified_char_dude.png')