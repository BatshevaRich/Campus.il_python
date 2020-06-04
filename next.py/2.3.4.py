class Pixel:
    """
_x - x coordinate
_y - y coordinate
_red - a value between 0 and 255
_green - a value between 0 and 255
_blue - a value between 0 and 255
"""

    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg = (self._red + self._green + self._blue) / 3
        self._red = avg
        self._green = avg
        self._blue = avg

    def print_pixel_info(self):
        if self._red > 50 and (self._green == self._blue == 0):
            print('X: {}, Y: {}, Color: ({}, {}, {}) {}'.format(
                self._x, self._y, self._red, self._green, self._blue, 'Red'))
        elif self._green > 50 and (self._red == self._blue == 0):
            print('X: {}, Y: {}, Color: ({}, {}, {}) {}'.format(
                self._x, self._y, self._red, self._green, self._blue, 'Green'))
        elif self._blue > 50 and (self._red == self._green == 0):
            print('X: {}, Y: {}, Color: ({}, {}, {}) {}'.format(
                self._x, self._y, self._red, self._green, self._blue, 'Blue'))
        else:
            print('X: {}, Y: {}, Color: ({}, {}, {})'.format(
                self._x, self._y, self._red, self._green, self._blue))


def main():
    pix = Pixel(5, 6, 250)
    pix.print_pixel_info()
    pix.set_grayscale()
    pix.print_pixel_info()

main()