from pygame import K_RIGHT, K_LEFT, K_UP, K_RCTRL, K_a, K_d, K_w, K_SPACE

screen_res = (1920, 1080)
gravity = 9.8
starting_fuel = 100
fps = 60
background_color = (255, 255, 255)
num_players = 2

keymaps = [{
        "right":K_RIGHT,
        "left":K_LEFT,
        "thrust":K_UP,
        "shoot":K_RCTRL
    },
    {
        "right":K_d,
        "left":K_a,
        "thrust":K_w,
        "shoot":K_SPACE
    }
]