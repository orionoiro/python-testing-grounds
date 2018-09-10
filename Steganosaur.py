from PIL import Image

im = Image.open(input('path to your image:    '))
pix = im.load()                                         # loading of pixels coordinates
file = open(input('path to your file with text:  '), 'r')
data = file.read()
width, height = im.width, im.height
x, y = 0, 0
bin_array = []
bits = list(format(pix[x, y][-1], '08b'))               # (list of strings)    bits of blue value in rgb pixel
z = -3                                                  # I'm using z as the beginning of last bits

for char in data:                                       # transforming text to binary data
    d_char = int.from_bytes(char.encode('ascii'), 'big')
    bin_array += format(d_char, '08b')

for idx, number in enumerate(bin_array):                # writing data into last bits of pixel blue value
    bits[z] = str(number)
    if z == -1 or idx == len(bin_array) - 1:
        tuple_v = list(pix[x, y])
        tuple_v[-1] = int(''.join(bits), 2)
        pix[x, y] = tuple(tuple_v)
        z = -3
        x += 1
        if x == width:
            y += 1
            x = 0
        if y == height:
            print('there are no more pixels left')
        try:
            bits = list(format(pix[x, y][-1], '08b'))
        except IndexError:
            pass
    else:
        z += 1
im.save(input('enter a filename with extension:  '))
print('completed')
