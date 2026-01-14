from PIL import Image

img = Image.open("./input/IMG_6.jpg")
width, height = img.size

for y in range(height):
    for x in range(width):
        rgb = img.getpixel((x, y))
        print(f"Pixel at ({x},{y}): {rgb}")



#  rember if check side == side len then no crop


from PIL import Image
import threading


def top(img,width, height):
    top=0
    x=int(width/2)
    tmp_top=rgb = img.getpixel((x, 1))
    for y in range(height):
        rgb = img.getpixel((x, y))
        if rgb== tmp_top:
            top+=1
        else:
            break
    return top




def bottom(img,width, height):
    bottom=0
    x=int(width/2)
    tmp_bottom=rgb = img.getpixel((x, 1))
    for y in reversed(range(height)):
            rgb = img.getpixel((x, y))
            if rgb== tmp_bottom:
                bottom+=1
            else:
                break
    return bottom



def left(img,width, height):
    y=int(height/2)
    tmp_left=rgb = img.getpixel((0,y))
    left=0
    for x in range(width):              # left to right
        color = img.getpixel((x, y))
        print(f"Pixel at ({x},{y}) = {color}")
        if tmp_left == color:
            left+=1
        else:
            break




def right(img,width, height):
    y=int(height/2)
    tmp_right=rgb = img.getpixel((0,y))
    right=0
    for x in range(width - 1, -1, -1):           
        color = img.getpixel((x, y))
        print(f"Pixel at ({x},{y}) = {color}")
        if tmp_right == color:
            right+=1
        else:
            break







def main():
    img = Image.open("./input/IMG_1.jpg")
    width, height = img.size
    # print(top(img,width,height))
    thread1 = threading.Thread(target=top, args=(img,width,height))
    thread2 = threading.Thread(target=bottom, args=(img,width,height))
    thread3 = threading.Thread(target=left, args=(img,width,height))
    thread4 = threading.Thread(target=right, args=(img,width,height))

    # starting the threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()


if __name__ == "__main__":
    main()



