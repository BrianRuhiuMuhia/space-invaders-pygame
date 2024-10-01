class Velocity:
    def __init__(self, image):
        self.velocity = 0
        self.image = image

    def update(self, direction, screen):
        if direction == "R" and self.image.position.x < screen.get_width() - self.image.get_width():
            self.go_right()
        elif direction == "L" and self.image.position.x > 0:
            self.go_left()
        else:
            self.stop()
        self.image.position.x += self.velocity

    def go_left(self):
        self.velocity = -10

    def go_right(self):
        self.velocity = 10

    def stop(self):
        self.velocity = 0