from PIL import Image
img = Image.open("./input/IMG_6.jpg")
width, height = img.size
bottom=0
x=int(width/2)
tmp_bottom= img.getpixel((x, height-1))
check =False

for y in reversed(range(height)):
    for x in range(0,width,250):
        pixel = img.getpixel((x, y))
        print(f"Pixel at ({x},{y}): {pixel}")

        if pixel== tmp_bottom:
            check=True
        else:
            check=False
            break
    if check == False:
        break
    if check:
        bottom+=1

# if bottom >= height:
#     bottom=0

print(f"height: {height} | width: {width}")
print(f"bottom: {tmp_bottom} ")
print(bottom)