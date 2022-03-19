import pgzrun
from random import randint
from settings import WIDTH, HEIGHT, TITLE, FPS
from actors import peco, bg, menu_bg, go_bg, zombies, btn, chest, key_icon, key, jello_icon

game_mode = 'menu'

def draw():
    if game_mode == 'menu' or game_mode == 'win':
        menu_bg.draw()
        btn.draw()

    if game_mode == 'game over':
        go_bg.draw()

    if game_mode == 'game':
        bg.draw()
        peco.draw()
        chest.draw()
        # for zombie in zombies:
        for zombie in zombies:
            zombie.draw()
        if key_icon.amount == 0:
            key.draw()
        key_icon.draw()
        screen.draw.text(str(key_icon.amount), center=(520, 21), color='white')
        if jello_icon.amount == 0:
            jello_icon.draw()
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

def on_key_down(key):
    if key == keys.SPACE:
        pass



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
