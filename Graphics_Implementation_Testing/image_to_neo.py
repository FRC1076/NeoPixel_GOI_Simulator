class Image_To_Neo:

    def __init__(self,image,coordinate):
        """
        This class converts an image to neo_pixel renerable pixels

        Input: A small ascii (16*16) image

        Output: Pixels to render for NeoDisplay

        coordinate: (x,y)
        image: "*** ** * ** ** "

        """

        self.image = image
        self.coordinate = coordinate
