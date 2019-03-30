import pygame
from pygame import Vector2

screen_res = (1000, 600)
gravity = Vector2(0, .0001)
starting_fuel = 100
player_thrust = .005
player_rotation_speed = .4
max_speed = .3
shoot_delay = 100
player_size = (40, 60)
player_lives = 3
num_players = 2

kill_score = 10
bullet_speed = 2
background_color = (0, 0, 0)
terrain_colors = [0x92BDA3,
                  0xA1BA89,
                  0xA5CC6B,
                  0x806D40,
                  0x50514F
]

fuelplatform_color = 0x649edb

player_color = [
    (128,255,114),
    (126,232,250),
    (255,240,124)
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
    },
    {
        "right":pygame.K_l,
        "left":pygame.K_j,
        "thrust":pygame.K_i,
        "shoot":pygame.K_n
    }
]

starting_positions = [
    (200, 200),
    (screen_res[0] - 200, 200),
    (screen_res[0]*.5, screen_res[1]*.5)
]

level ="""
@@@@@@      @@@@@@
@@@@         @@@@@
@@              @@
                    
                    
@@   #      #   @@
@@@@          @@@@
"""