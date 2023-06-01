import random

from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    def __init__(self, images):
        super().__init__(images[0])
        self.images = images
        self.image_index = 0
        self.animation_speed = 5
        self.animation_counter = 0
        self.rect.y = random.randrange(200, 330, 10)
        self.direction = 1 
        self.speed = 5

    def update(self, game_speed, obstacles):
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
            self.animation_counter = 0

        self.rect.y += self.speed * self.direction
        if self.rect.top <= 190:
            self.direction = 1
        elif self.rect.bottom >= 315:
            self.direction = -1

        super().update(game_speed, obstacles)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
