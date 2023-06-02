from dino_runner.utils.constants import SCORE_CAKE, SCORE_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class MultiScore(PowerUp):
    def __init__(self):
        self.image = SCORE_CAKE
        self.type = SCORE_TYPE
        super().__init__(self.image, self.type)