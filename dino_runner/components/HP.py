from dino_runner.utils.constants import LIFE_BAR

class LifeBar():
    def __init__(self):
        self.life_images = LIFE_BAR
        self.current_life_index = 0

    def draw(self, screen):
        current_life_image = self.life_images[self.current_life_index]
        screen.blit(current_life_image, (25, 20)) 

    def update(self, game):
        if game.attempts == 3:
            self.current_life_index = 0
        elif game.attempts == 2:
            self.current_life_index = 1
        elif game.attempts == 1:
            self.current_life_index = 2
        else:
            self.current_life_index = 2
