from wand.image import Image

class Compare:

    def __init__(self, version):
        self.version = version
        self.highlight()

    def highlight(self):
        with Image(filename=f'./screenshots/baseline/screenshot.png') as base:
            with Image(filename=f'./screenshots/{self.version}/screenshot.png') as img:
                base.fuzz = base.quantum_range * 0.20
                result_image, result_metric = base.compare(img)
                location, diff = base.similarity(img)
                print(f'Similarity (percentage): {diff}', self.version)
                with result_image:
                    result_image.save(filename=f'./screenshots/{self.version}/highlight_diff.png')

        return diff
