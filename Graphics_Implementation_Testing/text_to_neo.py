
from PIL import Image, ImageFont, ImageDraw
import numpy as np

class Text_To_Neo:

    def __init__(self):
        """
        This class converts an text to neo_pixel renerable pixels

        Input: Text

        Output: Pixels to render for NeoDisplay

        coordinate: (x,y)
        image: "*** ** * ** ** "

        """
        

        
        
    
    def Text_To_Pixels(self,text):
        myfont = ImageFont.truetype('Roboto-Black.ttf', 12)
        size = myfont.getsize(text)
        img = Image.new("1",size,"black")
        draw = ImageDraw.Draw(img)
        draw.text((0, 0), text, "white", font=myfont)
        pixels = np.array(img, dtype=np.uint8)
        chars = np.array([' ','*'], dtype="U1")[pixels]
        strings = chars.view('U' + str(chars.shape[1])).flatten()
        x = "\n".join(strings)
        return x

    def Pixels_To_Neo(self,coordinate):
        """
        This should take the output of Text_To_Pixels() and 
        a coordinate on the lights plane and output a list of 
        coordinates for the NeoDisplay to render


        """








if __name__ == "__main__":
    d = Text_To_Neo()
    print(d.convert("python"))