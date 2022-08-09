import time
from button import Button
from settings import Settings
from game_stats import GameStats
import pygame
from sfx import SFX
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from scoreboard import Scoreboard


def run_game():
    # initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the play button
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    sfx = SFX()

    # Make a ship, a group of bullets, and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    # capping fps
    time_1 = time.perf_counter()
    unprocessed = 0
    frame_cap = (1.0/1000)

    # start the main loop for the game.
    while True:
        can_render = False
        time_2 = time.perf_counter()
        passed = time_2 - time_1
        unprocessed += passed
        time_1 = time_2
        while(unprocessed >= frame_cap):
            unprocessed -= frame_cap
            can_render = True

        if can_render:
            gf.check_events(ai_settings, stats, sb, sfx, screen, ship,
                            aliens, bullets, play_button)
            if stats.game_active:
                ship.update()
                gf.update_bullets(ai_settings, screen, stats,
                                  sb, sfx, ship, aliens, bullets)
                gf.update_aliens(ai_settings, stats, sb, sfx, screen,
                                 ship, aliens, bullets)
            gf.update_screen(ai_settings, stats, sb, screen, ship,
                             aliens, bullets, play_button)


run_game()
