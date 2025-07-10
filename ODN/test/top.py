from PIL import Image

img = Image.open("./input/IMG_1.jpg")
width, height = img.size
top=0
x=int(width/2)
tmp_top= img.getpixel((x, 1))
check =False

for y in range(height):
    for x in range(0,width,250):
        pixel = img.getpixel((x, y))

        print(f"Pixel at ({x},{y}): {pixel}")
        if pixel== tmp_top:
            check=True
        else:
            check=False
            break
    if check == False:
        break
    if check:
        top+=1

if top >= height:
    top=0


        

print(f"height: {height} | width: {width}")
print(f"top: {tmp_top} ")
print(top)