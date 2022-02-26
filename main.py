import pgzrun
from random import randint


WIDTH = 600
HEIGHT = 500
FPS = 60
TITLE = 'Pecos quest'

peco = Actor("front")
background = Actor("background")
menu_background = Actor('menu_screen')
game_over_screen = Actor('game_over')
btn = Actor('start_btn', (300, 300))
jellotrap = Actor("jelo_trap")
zombies = []
for i in range(8):
    zombie = Actor('zombie_front', (randint(300, 650), randint(50, 450)))
    zombies.append(zombie)

chest = Actor("chest", (150, 100), (40, 40))
key = Actor('key', (500, 450))
key_icon = Actor('key', (500, 20))
key_icon.amount = 0
game_mode = 'menu'


def draw():
    if game_mode == 'menu' or game_mode == 'win':
        menu_background.draw()
        btn.draw()

    if game_mode == 'game over':
        game_over_screen.draw()

    if game_mode == 'game':
        background.draw()
        peco.draw()
        jellotrap.draw()
        chest.draw()
        # for zombie in zombies:
        for zombie in zombies:
            zombie.draw()
        if key_icon.amount == 0:
            key.draw()
        key_icon.draw()
        screen.draw.text(str(key_icon.amount), center=(520, 21), color='white')


def player_movement():
    global game_mode
    peco.prev_pos = peco.pos
    if keyboard.left and peco.x > 20:
        peco.x -= 3
        peco.image = 'left'
    if keyboard.right and peco.x < 580:
        peco.x += 3
        peco.image = "right"
    if keyboard.up:
        peco.y -= 3
        peco.image = "back"
    if keyboard.down:
        peco.y += 3
        peco.image = "front"
    if peco.colliderect(chest):
        peco.pos = peco.prev_pos
        if key_icon.amount != 0:
            game_mode = 'win'


def update_enemy(zombie):
    zombie.prev_pos = zombie.pos

    if zombie.x - 100 < peco.x < zombie.x + 100 and \
            zombie.y - 150 < peco.y < zombie.y + 150:
        if zombie.x < peco.x:
            zombie.x += 0.5
            zombie.image = 'zombie_right'
        else:
            zombie.x -= 0.5
            zombie.image = 'zombie_left'
        if zombie.y < peco.y:
            zombie.y += 0.5
            zombie.image = 'zombie_front'
        else:
            zombie.y -= 0.5
            zombie.image = 'zombie_back'
    else:
        zombie.x -= 0.5
        zombie.image = 'zombie_left'
        if zombie.x < -10:
            zombie.x = WIDTH + 5
            zombie.y = randint(10, HEIGHT - 10)

    if zombie.colliderect(chest):
        zombie.pos = zombie.prev_pos

    return zombie


def on_mouse_down(pos):
    global game_mode
    if game_mode == 'menu' and btn.collidepoint(pos):
        game_mode = 'game'


def update(dt):
    global zombie, game_mode
    player_movement()
    for i in range(len(zombies)):
        zombies[i] = update_enemy(zombies[i])

    if peco.colliderect(key) and key_icon.amount == 0:
        key_icon.amount += 1
    if peco.collidelist(zombies) != -1:
        game_mode = 'game over'


pgzrun.go()
