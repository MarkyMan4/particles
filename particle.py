import random

colors = [
    (50, 168, 82),
    (72, 128, 212),
    (242, 55, 27),
    (242, 235, 27),
    (214, 9, 173),
    (255, 126, 33)
]

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = random.random() * 20
        self.x_vel = (random.random() * 0.3) * (1 if random.random() > 0.5 else -1)
        self.y_vel = (random.random() * 0.3) * (1 if random.random() > 0.5 else -1)
        self.color = random.choice(colors)

    def update(self):
        self.x += self.x_vel
        self.y += self.y_vel

        if self.radius >= 0.2:
            self.radius -= 0.03
