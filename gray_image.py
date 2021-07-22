from simpleimage import SimpleImage
img = SimpleImage('C:\\Users\\Nithin\\My_GitHub\\Gray-image-converter\\flower.png')
img.show()
pixel=image.get_pixel(x,y)
average=(pixel.red + pixel.blue + pixel.green)//3

def gray_scale(x):
    average=(x.red + x.blue + x.green)//3
    x.red=average
    x.blue=average



for pixel in img:
    if pixel.red>average*1.6:
        pixel.red=255
        pixel.blue=0
        pixel.green=0
    else:
        gray_scale(pixel)

img.show()

