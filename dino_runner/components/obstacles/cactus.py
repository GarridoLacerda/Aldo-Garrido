from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import OBSTACLE_Y_POS, LARGE_OBSTACLE_Y_POS


class Cactus(Obstacle):
    def __init__(self, image, is_large=False):
        super().__init__(image)
        self.rect.y = LARGE_OBSTACLE_Y_POS if is_large else OBSTACLE_Y_POS
        self.is_large = is_large
