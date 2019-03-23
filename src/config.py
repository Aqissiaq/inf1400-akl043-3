import pygame
from pygame import Vector2

screen_res = (1920, 1080)
gravity = Vector2(0, .0001)
starting_fuel = 100
player_thrust = .005
player_rotation_speed = .5
max_speed = .9

bullet_speed = 3
fps = 60
background_color = (0, 0, 0)
num_players = 1

playerColor = [
    (0,0,0),
    (0,0,0)
]

keymaps = [{
        "right":pygame.K_RIGHT,
        "left":pygame.K_LEFT,
        "thrust":pygame.K_UP,
        "shoot":pygame.K_RCTRL
    },
    {
        "right":pygame.K_d,
        "left":pygame.K_a,
        "thrust":pygame.K_w,
        "shoot":pygame.K_SPACE
    }
]