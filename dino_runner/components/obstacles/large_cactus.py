from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_OBSTACLE_Y_POS


class LargeCactus(Obstacle):
    def __init__(self, image):
        super().__init__(image)
        self.rect.y = LARGE_OBSTACLE_Y_POS