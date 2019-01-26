import math

width = 8
height = 8


def coord_to_serpentine(coord_list):

    for i in range(len(coord_list)):
        current_coord = coord_list[i]

        column = (current_coord % width) + 1
        row = (int(current_coord / height)) + 1

        serpentine_value = ((column - 1) * height)
        if ((column % 2) == 0):  #column is even
            #if (width == 8):
            serpentine_value += (height - row)

        else:  #column is odd
            serpentine_value += row - 1
        return serpentine_value


def serpentine_to_coord(coord_list):

    for i in range(len(coord_list)):
        current_coord = coord_list[i]

        column = (int(current_coord / height)) + 1

        if ((column % 2) == 0):
            row = (height - (current_coord % width))
            x = ((row - 1) * width) + column
        else:
            row = (current_coord % height)
            print("hi")
            x = (((row - 0) * width) + column - 1)
        print(row)

        return x


print(serpentine_to_coord([28]))
#final result should be 27
