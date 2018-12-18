class NeoDisplay:

    def __init__(self, num_pixels):
        pass

    def clear(self):
        pass

    def render(self):
        """
        Return the string rendering of the NeoDisplay contents.
        They should print 
        """
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
               '+---------------------------------------------------------------+\n'

    def set_pixels(self, pixels_to_set):
        """
        Given an array of pixels indices, turn on the pixel
        in that position.
        """
        pass
