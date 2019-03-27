import pygame
from pygame import Vector2

screen_res = (760, 512)
gravity = Vector2(0, .0001)
starting_fuel = 100
player_thrust = .0005
player_rotation_speed = .5
max_speed = .5
player_size = (40, 60)

kill_score = 10
bullet_speed = 2
fps = 60
background_color = (0, 0, 0)
num_players = 2

player_color = [
    (255,0,0),
    (0,255,0),
    (0,0,255)
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

starting_positions = [
    (200, 200),
    (screen_res[0] - 200, 200)
]