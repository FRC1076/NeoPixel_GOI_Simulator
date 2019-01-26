def cart_to_neo(location):
    x, y = location
    #check if even
    panel_offset = 255
    if y > 7:
        panel_offset = 0
        y = (y - 8)
    if (x % 2 == 0):
        #x is even
        val = (x * 8) + (7 - y)
    else:
        #x is odd
        val = (x * 8) + y

    return val + panel_offset

x = cart_to_neo((4,5))
print(x)
