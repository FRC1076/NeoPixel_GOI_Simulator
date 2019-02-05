class Pixel:
    def __init__(self, pixel_loc, color):
        self.pixel_loc = pixel_loc
        self.color = color


class NeoDisplay:
    def __init__(self, num_pixels, width=16, height=16):
        self.pixels = []
        self.rows = []
        self.width = width
        self.height = height
        self.pixelcollist = []

        self.pixels_to_rows = [' '] * (self.width * self.height)


    def coord_to_serpentine(self, coord_list):

        new_coord_list = []

        for i in range(len(coord_list)):
            current_coord = coord_list[i]

            column = (current_coord % self.width) + 1
            row = (int(current_coord / self.height)) + 1

            serpentine_value = ((column - 1) * self.height)
            if ((column % 2) == 0):  #column is even
                #if (width == 8):
                serpentine_value += (self.height - row)

            else:  #column is odd
                serpentine_value += row - 1
            new_coord_list.append(serpentine_value)

        return new_coord_list

    def serpentine_to_coord(self, coord_list):
        new_coord_list = []
        for i in range(len(coord_list)):
            current_coord = coord_list[i]

            column = (int(current_coord / self.height)) + 1

            if ((column % 2) == 0):
                row = (self.height - (current_coord % self.width))
                x = ((row - 1) * self.width) + column
            else:
                row = (current_coord % self.height)

                x = (((row - 0) * self.width) + column - 1)
            new_coord_list.append(x)
        return new_coord_list

    def clear(self, clear_screen=False):
        #x = oneCoord
        #y = twoCoord]
        pixels_to_rows = [' '] * (self.width * self.height)

        if (clear_screen is not False):

            oneCoord, twoCoord = (0,1)

            pixels_to_remove = []  #[56,57,58,59]

            for x in range(oneCoord, twoCoord):
                pixels_to_remove.append(x)
            for cpv in pixels_to_remove:
                pixels_to_rows[cpv] = ' '
        else:
            print(chr(27) + '[2J', end='')

    def render(self, error_message="Ok"):
        """
        Return the string rendering of the NeoDisplay contents.
        They should print 
        """
        #self.clear()
        if (error_message == "No Data"):
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

            #Convert array into mulitple arrays

            out = self.partition(self.rows, self.height)

            rendered_lines = []

            for i in range(self.height):  
                rendered_line = '| ' + ' '.join(out[i]) + ' |'
                rendered_lines.append(rendered_line)

            top = ['--'] * self.width

            #Put everything into a readable format
            banner = ''.join(top) + '---'
            display_elements = [banner] + rendered_lines + [banner]


            return '\n'.join(display_elements)

    def partition(self, lst, n):
        division = len(lst) / n
        return [
            lst[round(division * i):round(division * (i + 1))]
            for i in range(n)
        ]

    def set_pixels(self, pixels_to_set=[], colors=[], pixel_type='*'):
        """
        Given an array of pixels indices, turn on the pixel
        in that position.

        To clear a pixel, set pixel_type to ' '
        To Set a pixel, give list of pixels and their colors

        To change the pixel reperesentation, change pixel_type to something else

        """


        self.pixels = self.serpentine_to_coord(pixels_to_set)
        i = 0
        for cpv in self.pixels:
            
            if(colors != []):
                self.pixels_to_rows[cpv] = colors[i] + pixel_type + '\u001b[0m'
            else:
                self.pixels_to_rows[cpv] = pixel_type
            i += 1

        self.rows = self.pixels_to_rows

        return 0
