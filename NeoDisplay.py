import numpy as np


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
        #for debuging
        self.pixels = [71, 73, 85, 91, 99, 109, 113, 127, 127]

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
           
           
            pixels=self.pixels
            
            rows = []
            #self.pixels = [71, 73, 85, 91, 99, 109, 113, 127, 127]


            #print(len(pixels))
            
            i = 0
            while(i < 256):
                rows.append(' ')
                i+=1
            
            current_row_value=0
            current_pixel_value=0


            #Draw line  
            while(current_pixel_value < len(pixels)):
                    while(current_row_value < len(rows)):
                        if(current_row_value == pixels[current_pixel_value]):
                            rows[current_row_value] = 'x'
                            
                        current_row_value+=1
                    current_row_value=0
                    current_pixel_value+=1    
            
            #Convert array into mulitple arras
            
            out = self.partition(rows,16)
            
            i=0
            rendered_lines = []
            while(i<16):#16 lines
                rendered_line = '| ' + ' '.join(out[i]) + ' |'
                
                rendered_lines.append(rendered_line)
                rendered_lines.append("\n")
                i+=1
            #rendered_out = out #do stuff

            return rendered_lines
                 
                        

            
    def partition(self,lst, n):
        division = len(lst) / n
        return [lst[round(division * i):round(division * (i + 1))] for i in range(n)]
        
            
    def set_pixels(self, pixels_to_set):
        """
        Given an array of pixels indices, turn on the pixel
        in that position.
        """
        self.pixels = pixels_to_set


