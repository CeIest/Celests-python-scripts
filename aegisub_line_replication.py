# To change
resolution = 1920
n = 5

x = 0
posX = 0
posY = 0

while x < resolution:

    pos = "\pos(" + str(posX) + "," + str(posY) + ")"

    # To change. Make sure to leave "pos" at the end
    # and to add double slashes whenever python counts it as a special backslash.
    drawing = 'm 8 -44 l 7 -44 7 1008 8 1008 8 -44'
    tags = "{\\an7\c&H7C7C7C&\\1a&H62&\\blur0.6\p1" + pos + "}"

    print(tags+drawing)
    x = x + n
    posX = posX + n
    # posY = posY + n
    
# If you need to do the horizontal part, uncomment the last line & comment the one above, change the resolution and add a rotation tag with HYDRA.
