from PIL import Image

# Open your image
img = Image.open("./input/IMG_1.jpg")
width, height = img.size
tmp_left= img.getpixel((0,int(height/2)))
left=0
tmp=False
for x in range(width):              # left to right
    for y in range(0,height,200):
        pixel = img.getpixel((x, y))

        if tmp_left == pixel:
            print(f"Pixel at ({x},{y}) = {pixel}")
            tmp=True
        else:
            tmp=False
            break
    if tmp == False:
        break
    if tmp:
        print('true')
        left+=1


# if left== width:
#     left=0


print(f"tmp : {tmp_left} | color : {pixel}")
print(f"height: {height} | width: {width}")
print(f'left: {left}')
