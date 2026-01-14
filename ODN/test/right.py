

from PIL import Image

image = Image.open("./input/IMG_1.jpg")
width, height = image.size
tmp_right= image.getpixel((width-1,int(height/2)))
check=False
right=0
for x in range(width - 1, -1, -1):           
    for y in range(0,height,200):
        pixel = image.getpixel((x, y))
        if tmp_right == pixel:
            print(f"Pixel at ({x},{y}) = {pixel}")
            check = True
        else:
            check = False
            break
    if check:
        right+=1
    else:
        break


print(f"tmp : {tmp_right} | color : {pixel}")
print(f"height: {height} | width: {width}")
print(f'left: {right}')


