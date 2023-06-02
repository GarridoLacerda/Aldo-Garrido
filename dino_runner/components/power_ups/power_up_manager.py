import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.multi_score import MultiScore


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200, 300)
            power_up_type = random.choice([Shield, Hammer, MultiScore])
            if  power_up_type == Shield:
                self.power_ups.append(Shield())

            elif power_up_type == Hammer:
                self.power_ups.append(Hammer())
            else:
                self.power_ups.append(MultiScore())

    def update(self, game):
        self.generate_power_up(game.score)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)

                if isinstance(power_up, Hammer):
                    game.player.hammer = True
                    game.player.shield = False
                    game.player.multi_score = False
                elif isinstance(power_up, Shield):
                    game.player.shield = True
                    game.player.hammer = False
                    game.player.multi_score = False
                elif isinstance(power_up, MultiScore):
                    game.player.multi_score = True
                    game.player.hammer = False
                    game.player.shield = False

                else:
                    game.player.hammer = False
                    game.player.shield = False
                    game.player.multi_score = False

                game.player.type = power_up.type


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)