from PIL import ImageDraw, Image


class GlassesImageDraw(ImageDraw.ImageDraw):
    def glasses(self, xy, fill):
        x, y, w = xy
        glass, body = fill
        draw = ImageDraw.Draw(img)
        x1 = x + (11 * w // 2) - w // 2 + 1
        y1 = y + (5 * w // 2) - (w // 4) // 2 - 1
        draw.ellipse((x, y, x + 5 * w, y + 5 * w), glass, body, 4)
        draw.ellipse((x + w + 5 * w, y, x + w + 2 * (5 * w), y + 5 * w), glass, body, 4)
        draw.rectangle([x1, y1 + 1, x1 + w - 2, y1 + w // 4], body)


img = Image.new('RGB', (240, 240), '#000000')
drw = GlassesImageDraw(img)
drw.glasses((10, 70, 20), ('#ffffff', '#999999'))
img.show()
img.save('result.png')
