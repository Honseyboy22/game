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
<<<<<<< HEAD


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
=======
    zombie.draw()
>>>>>>> 6a7923254f8dad46d263facd1671b8696bd3440e


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

    if enemy.colliderect(chest):
        zombie.pos = zombie.prev_pos

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
