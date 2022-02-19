import pgzrun
from random import randint


WIDTH = 600
HEIGHT = 500
FPS = 60
TITLE = 'Pecos quest'

peco = Actor("front")
background = Actor("background")
menu_background = Actor('menu_screen')
btn = Actor('start_btn', (300, 300))
jellotrap = Actor("jelo_trap")
zombie = Actor('zombie_front', (200, 300))
chest = Actor("chest", (150, 100), (40, 40))

game_mode = 'menu'

def draw():
    if game_mode == 'menu':
        menu_background.draw()
        btn.draw()

    if game_mode == 'game':
        background.draw()
        peco.draw()
        jellotrap.draw()
        chest.draw()
        # for zombie in zombies:
        zombie.draw()


def player_movement():
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


def update_enemy(enemy):
    if enemy.colliderect(chest):
        if chest.top < zombie.bottom and zombie.y < chest.y:
            zombie.bottom = chest.top - 0.5
        elif chest.bottom < zombie.top and zombie.y > chest.y:
            zombie.top = chest.bottom + 0.5
        elif chest.right > zombie.left and zombie.x > chest.x:
            zombie.left = chest.right + 0.5
        elif chest.left < zombie.right and zombie.x < chest.x:
            zombie.right = chest.left - 0.5

    elif zombie.x - 50 < peco.x < zombie.x + 50 and \
            zombie.y - 100 < peco.y < zombie.y + 100:
        if zombie.x < peco.x:
            zombie.x += 1
            zombie.image = 'zombie_right'
        else:
            zombie.x -= 1
            zombie.image = 'zombie_left'
        if zombie.y < peco.y:
            zombie.y += 1
            zombie.image = 'zombie_front'
        else:
            zombie.y -= 1
            zombie.image = 'zombie_back'
    else:
        zombie.x -= 0.5
        zombie.image = 'zombie_left'
        if zombie.x < -10:
            zombie.x = WIDTH + 5
            zombie.y = randint(10, HEIGHT - 10)

    return zombie

def on_mouse_down(pos):
    global game_mode
    if game_mode == 'menu' and btn.collidepoint(pos):
        game_mode = 'game'

def update(dt):
    global zombie
    player_movement()
    zombie = update_enemy(zombie)
    # for zombie in zombies:
    #     zombies = update_enemy(zombie)


pgzrun.go()
