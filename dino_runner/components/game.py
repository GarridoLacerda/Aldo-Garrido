import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE, TEXT_POSITION
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.clouds import Clouds


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = 0
        self.death_count = 0

        self.clouds = {
            'cloud1': Clouds((SCREEN_WIDTH + 300), 200),
            'cloud2': Clouds((SCREEN_WIDTH + 600), 240),
            'cloud3': Clouds((SCREEN_WIDTH + 900), 180),
            'cloud4': Clouds((SCREEN_WIDTH + 1200), 50)
        }
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()    

    def reset_game(self):
        self.game_speed = 20
        self.score = 0
        self.death_count = 0
        self.execute()

    def run(self):
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self)
        for cloud in self.clouds.values():
            cloud.update()
        self.clouds.update()

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 5
            for cloud in self.clouds.values():
                cloud.clouds_speed += 0.25

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        for cloud in self.clouds.values():
            cloud.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                self.draw_text(
                f"{self.player.type.capitalize()} enabled for {time_to_show} seconds",
                18,
                (255, 0, 0),
                TEXT_POSITION
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def draw_text(self, text, size, color, position):
        font = pygame.font.Font(FONT_STYLE, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = position
        self.screen.blit(text_surface, text_rect)

    def draw_score(self):
        score_text = f"Score: {self.score}"
        self.draw_text(score_text, 22, (0, 0, 0), (1000, 50))

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.draw_text("Press any key to start", 22, (0, 0, 0), (half_screen_width, half_screen_height))
        elif self.death_count >= 1 and self.death_count < 4:
            self.screen.blit(ICON, (half_screen_width - 35, half_screen_height - 140))
            text_list = [
                ("Press any key to restart", (half_screen_width, half_screen_height)),
                (f"Score: {self.score}", (1000, 50)),
                (f"Deaths: {self.death_count}", (100, 50))
            ]
            for text, position in text_list:
                self.draw_text(text, 22, (0, 0, 0), position)
        elif self.death_count >= 3:
            self.reset_game()


        pygame.display.update()
        self.handle_events_on_menu()


        