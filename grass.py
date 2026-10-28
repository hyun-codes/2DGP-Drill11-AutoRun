from pico2d import get_canvas_width, load_image


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(get_canvas_width() / 2, 30)
