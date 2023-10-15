# LAB 7 Documentation
Here is how you run the plugin known as pillow which is the module/plug in i used for my lab 7

First, let's create a Virtual ENV called scripts. You can call it whatever you want.

```bash
virtualenv ~/venv/pillow
source ~/venv/scripts/bin/activate
pip install pillow
```
Now you have to have an image that you want to use to convert or do operations with like an jpg file.
First, download any image and save it in your project folder for easy access and thus allowing for no need of adding file path

Now, in Python, run the following code:

The Following code  will resize the old image size to the new dimensions according to new width using pillow and load it

```python
from PIL import Image,ImageFilter
img = Image.open('IMG_1270.jpg')
widthToChange = 300
HeightToChange = 100
resizeImg = img.resize((widthToChange,HeightToChange))
resizeImg.save("IMG_1270.jpg")
img.load()
```

The Following code  will apply a greyscale filter the resized image file with the new dimensions and load it


```python
greyscaleImg = img.convert("L")
greyscaleImg.save("IMG_1270.jpg")
```

Finally, we can use the Image module to create a thumnail for our image. It is using the greyed out reformatted image not the original image file. 

```python
thumnailSize = (100,100)
thumnailimg = img.copy()
thumnailimg.thumbnail(thumnailSize)

thumnailimg.save("thumnail_img.jpg")
```

make sure  to deactivate your virtualenv when you're done.

```bash
deactivate
```
