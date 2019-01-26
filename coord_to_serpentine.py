import math


def coord_to_serpentine(coord_list):

    for i in range(len(coord_list)):
        current_coord = coord_list[i]

        column = (current_coord % 8) + 1
        row = (int(current_coord / 8)) + 1

        serpentine_value = ((column - 1) * 8)
        if ((column % 2) == 0):  #column is even
            serpentine_value += ((8 - row) + 1) - 1
        else:  #column is odd
            serpentine_value += row - 1
        return serpentine_value


print(coord_to_serpentine([10, 9]))
#final result should be 20
