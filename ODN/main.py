from PIL import Image
import os
import csv

class iMAGE:

    
    def top(self,img,width, height,speed=250,bp=False):
        top=0
        x=int(width/2)
        tmp_top= img.getpixel((x, 1))
        check =False

        for y in range(height):
            for x in range(0,width,speed):
                pixel = img.getpixel((x, y))
                if bp:
                    print(f"Pixel at ({x},{y}): {pixel}")

                if pixel== tmp_top:
                    check=True
                else:
                    check=False
                    break
            if not check:
                break
            top+=1

        if top >= height:
            top=0
        return top




    def bottom(self,img,width, height,speed=250,bp=False):
        bottom=0
        x=int(width/2)
        tmp_bottom= img.getpixel((x, height-1))
        check =False

        for y in reversed(range(height)):
            for x in range(0,width,speed):
                pixel = img.getpixel((x, y))
                if bp:
                    print(f"Pixel at ({x},{y}): {pixel}")

                if pixel== tmp_bottom:
                    check=True
                else:
                    check=False
                    break
            if not check:
                break
            bottom+=1
        return bottom



    def left(self,img,width, height,speed=250,bp=False):
        tmp_left= img.getpixel((0,int(height/2)))
        left=0
        check=False
        for x in range(width):              # left to right
            for y in range(0,height,speed):
                pixel = img.getpixel((x, y))
                if bp:
                    print(f"Pixel at ({x},{y}): {pixel}")
                if tmp_left == pixel:
                    check=True
                else:
                    check=False
                    break
            if not check:
                break
            left+=1
        return left



    def right(self,img,width, height,speed=250,bp=False):
        tmp_right= img.getpixel((width-1,int(height/2)))
        check=False
        right=0
        for x in range(width - 1, -1, -1):           
            for y in range(0,height,speed):
                pixel = img.getpixel((x, y))
                if bp:
                    print(f"Pixel at ({x},{y}): {pixel}")
                if tmp_right == pixel:
                    check = True
                else:
                    check = False
                    break
            if not check:
                break
            right+=1
        return right


    def main(self,bp,speed=3):
        try:
            os.makedirs('./output', exist_ok=True)
            IMGS = os.listdir('./input')

            with open('./output/crop_data.csv', mode='w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['image', 'top', 'bottom', 'left', 'right'])  
                for image in IMGS:
                    print(image)
                    img = Image.open(os.path.join('./input', image))
                    width, height = img.size

                    c_top = self.top(img, width, height,speed,bp)
                    c_bottom = self.bottom(img, width, height,speed,bp)
                    c_left = self.left(img, width, height,speed,bp)
                    c_right = self.right(img, width, height,speed,bp)

                    print(f"img: {image} | top: {c_top} ,bottom: {c_bottom}, left: {c_left}, right:{c_right}")

                    writer.writerow([image, c_top, c_bottom, c_left, c_right])

                    if (c_left + c_right >= width) or (c_top + c_bottom >= height):
                        print(f"Skipping cropping for {image}: crop box would be empty.")
                        cropped_img = img
                    else:
                        crop_box = (c_left, c_top, width - c_right, height - c_bottom)
                        cropped_img = img.crop(crop_box)

                    cropped_img.save(f"./output/{image}")
                    print("Image cropped and saved.")
        except Exception:
            print('the speed limit crossed the size of img... \n exiting ...')



    # def main(self,):
    #     os.makedirs('./output', exist_ok=True)
    #     IMGS=os.listdir('./input')
    #     for image in IMGS:
    #         print(image)
    #         img=Image.open(os.path.join('./input', image))
    #         width, height = img.size
    #         c_top=self.top(img,width,height)
    #         c_bottom=self.bottom(img,width,height)
    #         c_left=self.left(img,width,height)
    #         c_right=self.right(img,width,height)
    #         print(f"img: {img} | top: {c_top} ,bottom: {c_bottom}, left: {c_left}, right:{c_right}")

        
    #         crop_box = (c_left, c_top, width - c_right, height - c_bottom)
    #         if (c_left + c_right >= width) or (c_top + c_bottom >= height):
    #             print(f"Skipping cropping for {image}: crop box would be empty.")
    #             cropped_img = img
    #         else:
    #             crop_box = (c_left, c_top, width - c_right, height - c_bottom)
    #             cropped_img = img.crop(crop_box)

    #         cropped_img.save(f"./output/{image}")
    #         print("Image cropped and saved.")


if __name__ == "__main__":
    main = iMAGE()
    try:
        speed = int(input(
            "Default speed: (3)\n"
            "Higher values are faster, but may reduce program quality.\n"
            "Lower values are slower but more thorough.\n"
            "Enter the speed (1-10): "
        ))

    except ValueError:
        print("Invalid input. Running in default (3)...")
        print("Background process Off \n------------------")
        speed = 3

    if speed < 1 or speed > 10:
        print("Speed out of range. Running in default (3)...")
        speed = 3

    bp = input(
        "--------------------------------------\n"
        "Do you want to see the background process?\n"
        "It will consume more power.\n"
        "Recommended: no.\n"
        "Default (no): \n"
        "(y)es - (n)o: "
    ).strip().lower()
    if bp and bp.lower().startswith('y'):
        bp = True
    else:
        bp = False

    speed = speed * 10
    main.main(bp, speed)




