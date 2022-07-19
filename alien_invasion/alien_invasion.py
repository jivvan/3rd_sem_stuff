import sys
from time import sleep
from settings import Settings
import pygame
from ship import Ship
from alien import Alien
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

    # Make a alien
    alien = Alien(ai_settings,screen)

    # Make a group to store bullets in
    bullets = Group()

    # start the main loop for the game.
    while True:
        gf.check_events(ai_settings,screen , ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)


run_game()
