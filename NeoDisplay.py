class NeoDisplay:
    def __init__(self, num_pixels, width=16, height=16):
        self.pixels = []
        self.rows = []
        self.width = width
        self.height = height

    def clear(self):
        print(chr(27) + '[2J', end='')

    def coord_to_serpentine(self, coord_list):

        new_coord_list = []

        for i in range(len(coord_list)):
            current_coord = coord_list[i]
            #Check if even or odd
            #if even go down
            #if odd go up
            #new_coord = (current_coord - 1) * (self.height / 2)
            #new_coord_list.append(new_coord)

        return new_coord_list

    def render(self, error_message="Ok"):
        """
        Return the string rendering of the NeoDisplay contents.
        They should print 
        """
        self.clear()
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

            for i in range(self.height):  #16 lines
                rendered_line = '| ' + ' '.join(out[i]) + ' |'
                rendered_lines.append(rendered_line)

            top = ['--'] * self.width

            #Put everything into a readable format
            banner = ''.join(top) + '---'
            display_elements = [banner] + rendered_lines + [banner]

            #test the serpentine function
            x = []
            x = self.coord_to_serpentine([1, 2, 3, 4, 5, 6])
            print(x)

            return '\n'.join(display_elements)

    def partition(self, lst, n):
        division = len(lst) / n
        return [
            lst[round(division * i):round(division * (i + 1))]
            for i in range(n)
        ]

    def set_pixels(self, pixels_to_set):
        """
        Given an array of pixels indices, turn on the pixel
        in that position.
        """

        self.pixels = pixels_to_set

        #Regenerate Row list
        pixels_to_rows = [' '] * (self.width * self.height)

        #Draw Pixels
        for cpv in self.pixels:
            pixels_to_rows[cpv] = 'x'

        self.rows = pixels_to_rows

        return 0
