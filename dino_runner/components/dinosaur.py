import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import (
    RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD,
    JUMPING_SHIELD, RUNNING_SHIELD, JUMPING_HAMMER, DUCKING_HAMMER,
    RUNNING_HAMMER, HAMMER_TYPE, SCORE_TYPE, RUNNING_SCORE, JUMPING_SCORE,
    DUCKING_SCORE
)

X_POS = 80
Y_POS = 310
Y_POS_DUCK = 340
JUMP_VEL = 8.5

DUCK_IMG = { 
    DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, 
            HAMMER_TYPE: DUCKING_HAMMER, SCORE_TYPE: DUCKING_SCORE
}
JUMP_IMG = { 
    DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD,
             HAMMER_TYPE: JUMPING_HAMMER, SCORE_TYPE: JUMPING_SCORE 
}
RUN_IMG = { 
    DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, 
           HAMMER_TYPE: RUNNING_HAMMER, SCORE_TYPE:RUNNING_SCORE 
}


class Dinosaur(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.jump_vel = JUMP_VEL
        self.dino_jump = False
        self.dino_duck = False
        self.dino_run = True
        self.setup_state()

    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.hammer = False
        self.a = self.type
        self.multi_score = False
        self.show_text = False
        self.power_up_time = 0

    def update(self, user_input):
        if user_input[pygame.K_UP]:
            self.dino_jump = True
            self.dino_run = False
        elif user_input[pygame.K_DOWN]:
            self.dino_duck = True
            self.dino_run = False
        elif not self.dino_jump:
            self.dino_run = True

        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

        if self.step_index >= 9:
            self.step_index = 0

    def run(self):
        if not self.has_power_up:
            self.image = RUN_IMG[DEFAULT_TYPE][self.step_index // 5]
        else:
            self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1

    def jump(self):
        if not self.has_power_up:
            self.image = JUMP_IMG[DEFAULT_TYPE]
        else:
            self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def duck(self):
        if not self.has_power_up:
            self.image = DUCK_IMG[DEFAULT_TYPE][self.step_index // 5]
        else:
            self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect.y = Y_POS_DUCK   
        self.step_index += 1

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))