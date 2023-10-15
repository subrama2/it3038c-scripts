#make sure to pip install Pillow before running this module
from PIL import Image, ImageFilter

# image File
img = Image.open("IMG_1270.jpg")

widthToChange = 300
HeightToChange = 100

resizeImg = img.resize((widthToChange,HeightToChange))
# this will resize the old image size to the new dimensions according to new width using pillow
resizeImg.save("IMG_1270.jpg")


# Applying fiter to reformatted pic
greyscaleImg = img.convert("L")
greyscaleImg.save("IMG_1270.jpg")


# creating a thumnail

thumnailSize = (100,100)
thumnailimg = img.copy()
thumnailimg.thumbnail(thumnailSize)

thumnailimg.save("thumnail_img.jpg")

