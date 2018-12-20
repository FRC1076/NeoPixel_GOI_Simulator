class NeoDisplay:

    def __init__(self, num_pixels):
        pass

    def clear(self):
        pass

    def render(self, error_message="Ok"):
        """
        Return the string rendering of the NeoDisplay contents.
        They should print 
        """
        #                            1                   2                   3
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

    def set_pixels(self, pixels_to_set):
        """
        Given an array of pixels indices, turn on the pixel
        in that position.
        """
        pass
