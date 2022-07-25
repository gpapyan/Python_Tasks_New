# The coordinates (x;y) of the point and the radius of the circle (r) are entered. Determine whether a given point
# belongs to a circle if its center is at the origin.


def inside(crcl_x, crcl_y, rads, x, y):

    if ((x - crcl_x) * (x - crcl_x) +
            (y - crcl_y) * (y - crcl_y) <= rads * rads):
        return True
    else:
        return False


x = 2
y = 2

crcl_x = 2
crcl_y = 8

rads = 6

if inside(crcl_x, crcl_y, rads, x, y):
    print("inside")
else:
    print("outside")
