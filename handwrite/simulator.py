# coding: utf-8
from PIL import Image, ImageFont

from handright import Template, handwrite

file = open("input.txt", "r")
text = ""
while file:
    line = file.readline()
    text = text + line + "\n"
    if line == "":
        break
file.close()

template = Template(
    background=Image.new(mode="1", size=(2480, 3508), color=1),
    font=ImageFont.truetype("hand1.ttf", size=100),
)
images = handwrite(text, template)
for i, im in enumerate(images):
    assert isinstance(im, Image.Image)
    # im.show()
    im.save("output/{}.jpg".format(i))
