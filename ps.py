from PIL import Image, ImageDraw, ImageFont
import cv2
import math

def img2sketch():
    photo="ascii.png"
    k_size=7
    img=cv2.imread(photo)
    
    # Convert to Grey Image
    grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert Image
    # invert_img=cv2.bitwise_not(grey_img)
    #invert_img=255-grey_img

    # Blur image
    blur_img=cv2.GaussianBlur(grey_img, (k_size,k_size),0)

    # Invert Blurred Image
    invblur_img=cv2.bitwise_not(blur_img)
    #invblur_img=255-blur_img

    # Sketch Image
    sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)

    # Save Sketch 
    cv2.imwrite('result.png', sketch_img)

    # Display sketch
    # cv2.imshow('sketch image',sketch_img)
    # cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#Function call

def asc_img():
    chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
    charARRAY = list(chars)
    charLength = len(charARRAY)
    intervals = charLength/256

    oneCharWidth = 6
    oneCharHeight = 9

    def getChar(inputInt):
        return charARRAY[math.floor(inputInt*intervals)]
    

    im =Image.open("pineapple.png")
    fnt = ImageFont.truetype('arial.ttf', 15)

    width, height = im.size
    im = im.resize((int(0.25*width), int(0.25*height*(6/oneCharHeight))), Image.Resampling.NEAREST)
    #CHECKING AND DOING
    width, height = im.size
    pix = im.load()

    #CONVERTING INTO IMG
    outputImage = Image.new("RGB", (int(6 * width), int(9 * height)), color = (1, 1, 1))
    #USING IMAGE DRAW
    d = ImageDraw.Draw(outputImage)
    
    for i in range(height):
        
        for j in range(width):
            r, g, b = pix[j, i]
            h = int(r/3 + g/3 + b/3)
            pix[j, i] = (h, h, h)
        
            d.text((j*6, i*9), getChar(h), font = fnt, fill = (r, g, b))


    outputImage.save('ascii.png')

if __name__=="__main__":
    print('convering...')
    print('wait for program to complete...')
    asc_img()
    img2sketch()
    
