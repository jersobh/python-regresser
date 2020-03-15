from PIL import Image, ImageChops

class Compare:

    def __init__(self, version):
        self.version = version
        self.i1 = Image.open('./screenshots/baseline/screenshot.png')
        self.i2 = Image.open(f'./screenshots/{self.version}/screenshot.png')
        self.black_or_b()

    def black_or_b(self):
        point_table = ([0] + ([255] * 255))

        diff = ImageChops.difference(self.i1, self.i2)
        diff = diff.convert('L')
        diff = diff.point(point_table)
        new = diff.convert('RGB')
        new.paste(self.i2, mask=diff)
        new.save(f'./screenshots/{self.version}/alpha_diff.png')

