from PIL import Image

im = Image.open(input('path to your image:    '))
pix = im.load()
file = open(input('path to your file with text:  '), 'r')
data = file.read()


def text_to_bin(data):
    bin_array = []
    for char in data:
        d_char = int.from_bytes(char.encode('ascii'), 'big')
        bin_array += format(d_char, '08b')
    return bin_array


def steganographus(x, y):
    width, height = im.width, im.height
    bits = list(format(pix[x, y][-1], '08b'))
    z = -3

    for idx, number in enumerate(text_to_bin(data)):
        bits[z] = str(number)
        if z == -1 or idx == len(text_to_bin(data)) - 1:
            tuple_v = list(pix[x, y])
            tuple_v[-1] = int(''.join(bits), 2)
            pix[x, y] = tuple(tuple_v)
            z = -3
            x += 1
            if x == width:
                y += 1
                x = 0
            if y == height:
                break
            try:
                bits = list(format(pix[x, y][-1], '08b'))
            except IndexError:
                pass
        else:
            z += 1
    im.save(input('enter a new filename with extension:  '))
    print('completed')


if __name__ == '__main__':
    steganographus(0, 0)
