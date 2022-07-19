import sys
from settings import Settings
import pygame
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Testing Panda")

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in
    bullets = Group()

    # start the main loop for the game.
    while True:
        gf.check_events(ai_settings, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
