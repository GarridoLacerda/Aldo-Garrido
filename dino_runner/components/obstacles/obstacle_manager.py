import pygame
import random

from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import LARGE_CACTUS, BIRD, SMALL_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle_type = random.choice([Cactus, Bird])
            if obstacle_type == Cactus:
                is_large = random.choice([False, True])
                if is_large:
                    image = LARGE_CACTUS[random.randint(0, 2)]
                else:
                    image = SMALL_CACTUS[random.randint(0, 2)]
                self.obstacles.append(Cactus(image, is_large))
            else:
                image = BIRD
                self.obstacles.append(Bird(image))
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
                else:
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
