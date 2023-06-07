# install pillow library
# import pillow
# open up the image we want to resize
# print the current size of the img
# specify the size of the image you want to change
# save the new image

from PIL import Image

def resize_img(_witdh, _length):
    image = Image.open('/home/jullioap/Imágenes/Astronaut (1920x1200).jpg')
    path_to_save = 'image_resizer'
    print(f"Current size of the image : {image.size}")
    resize_img = image.resize((_witdh, _length))
    resize_img.save(f'{path_to_save}/Image_resized.png')

width = int(input('Enter Width: '))
length = int(input('Enter Lenght: '))
resize_img(width, length)