import math


def coord_to_serpentine(coord_list):

    for i in range(len(coord_list)):
        current_coord = coord_list[i]

        column = (current_coord % 8) + 1
        row = (int(current_coord / 8)) + 1

        # print(row)
        #print(column)
        x = ((column - 1) * 8)
        if ((column % 2) == 0):  #column is even

            print("even")
            x += ((8 - row) + 1) - 1
        else:  #column is odd
            x += row - 1
        #Check if even or odd
        #if even go down
        #if odd go up
        print(x)


coord_to_serpentine([34])
#final result should be 20
