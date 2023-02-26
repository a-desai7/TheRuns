import PIL
from PIL import Image, ImageDraw, ImageFilter

CharDude = Image.open(r'RunsWorking\pyxelate\result (1).png')
person = Image.open('pixel.png')

reSizedPerson = person.resize((1200,550), resample=None, box=None, reducing_gap=None)

# Get the dimensions of the resized person image
width, height = reSizedPerson.size

# Calculate the crop box to remove 10% of the width from both sides
left = int(width * 0.35)
upper = 70
right = int(width * 0.6)
lower = height * .7

# Crop the resized person image
im_crop = reSizedPerson.crop((left, upper, right, lower))

# Save the cropped image to a file
im_crop.save('cropped_person.png')

# Create a copy of CharDude to place the cropped person image on
CharDude_copy = CharDude.copy()

# Calculate the position to place the cropped person image on CharDude_copy
x_offset = 120
y_offset = 10

# Paste the cropped person image onto CharDude_copy
CharDude_copy.paste(im_crop, (x_offset, y_offset))

# Save the modified image to a file
CharDude_copy.save('modified_char_dude.png')