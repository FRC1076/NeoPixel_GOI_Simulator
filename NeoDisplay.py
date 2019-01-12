class NeoDisplay:
    def __init__(self, num_pixels):
        self.pixels = []

    def clear(self):
        pass

    def render(self, error_message="Ok"):
        """
        Return the string rendering of the NeoDisplay contents.
        They should print 
        """

        if (error_message == "No Data" or self.pixels == []):
            #                        1                   2                   3
            #        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
            return '+---------------------------------------------------------------+\n' + \
                '|                                                               |\n' + \
                '|                                                               |\n' + \
                '|                                                               |\n' + \
                '|                                                               |\n' + \
                '|                                                               |\n' + \
                '|                                                               |\n' + \
                '|                                                               |\n' + \
                '|                         No Data                               |\n' + \
                '|                                                               |\n' + \
                '|                                                               |\n' + \
                '|                                                               |\n' + \
                '|                                                               |\n' + \
                '|                                                               |\n' + \
                '|                                                               |\n' + \
                '|                                                               |\n' + \
                '|                                                               |\n' + \
                '+---------------------------------------------------------------+\n' + \
                ' Status: '+error_message
        else:
            pixels = self.pixels
            print(pixels)

            #line0 = [0, 2]

            #line_values = []

            #for positions in line0:
            #    line_values.append(values[positions])
            #rendered_line = '| ' + ' '.join(line_values) + ' |'
            #return (rendered_line)
            return 0

    def set_pixels(self, pixels_to_set):
        """
        Given an array of pixels indices, turn on the pixel
        in that position.
        """
        self.pixels = pixels_to_set
