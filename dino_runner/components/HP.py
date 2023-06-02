from dino_runner.utils.constants import HEART

class LifeBar():
    def __init__(self):
        self.life_image = HEART 

    def draw(self, screen):
        for i in range(self.attempts):
            x = 25 + i * (self.life_image.get_width() + 10)
            y = 20  
            screen.blit(self.life_image, (x, y))

    def update(self, game):
        if game.attempts == 3:
            self.attempts = 3
        elif game.attempts == 2:
            self.attempts = 2
        elif game.attempts == 1:
            self.attempts = 1
        else:
            self.attempts = 0