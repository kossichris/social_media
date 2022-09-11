# Importing the libraries
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter
from PIL import ImageFont


def flyer_creator():
    # Open an Image
    img = Image.open('flyer.png')

    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)

    # Custom font style and font size
    my_font = ImageFont.truetype('Ubuntu-Light.ttf', 200)

    # Add Text to an image
    title = input("Enter title of your post: ")
    I1.text((1000, 70), title.title(), font=my_font,
            align='center',)

    # Resize the code image
    code_img = Image.open('code.png')
    basewidth = 3200
    wpercent = (basewidth/float(code_img.size[0]))
    hsize = int((float(code_img.size[1])*float(wpercent)))
    new_code_img = code_img.resize((basewidth, hsize), Image.ANTIALIAS)

    img.paste(new_code_img,  (400, 500))
    # Display edited image
    img.show()

    # Save the edited image
    img.save("/Users/christiankossi/Documents/new_flyer.png")
