

class Center:
    def __init__(self, center_px, cv_image):
        self.px = center_px
        self.value = cv_image[center_px[1], center_px[0]]

    def __eq__(self, other):
        return self.value == other.value and self.px == other.px

    def __str__(self):
        return '(value: %d, px [%d, %d])' % (self.value, self.px[0], self.px[1])


class CenterList(list[Center]):

    def centers_px(self, abs_threshold):
        return [c.px for c in self if c.value >= abs_threshold]

