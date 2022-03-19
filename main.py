import pgzrun
from random import randint
from settings import WIDTH, HEIGHT
from actors import peco, bg, menu_bg, go_bg, zombies, btn, \
    chest, key_icon, key, jello_icon, bomb_icon

game_mode = 'menu'

jellos = []
bombs = []

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
        jello_icon.draw()
        bomb_icon.draw()
        screen.draw.text(str(jello_icon.amount),
                         center=(470, 21), color='white')
        screen.draw.text(str(key_icon.amount), center=(520, 21), color='white')
        screen.draw.text(str(bomb_icon.amount),
                         center=(570, 21), color='white')
        for jello in jellos:
            jello.draw()
        for bomb in bombs:
            bomb.draw()


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


def update_enemy(zombie, jellos):
    stop = False
    for jello in jellos:
        if zombie.colliderect(jello):
            stop = True

    zombie.prev_pos = zombie.pos
    if not stop:
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
    if key == keys.SPACE and jello_icon.amount > 0:
        jello = Actor('jelo_trap')
        jello.pos = peco.pos
        jello.time = 0
        jellos.append(jello)
        jello_icon.amount -= 1
    if key == keys.LSHIFT and bomb_icon.amount > 0:
        bomb = Actor('bomb')
        bomb.pos = peco.pos
        bomb.time = 0
        bomb.set = False
        bombs.append(bomb)
        bomb_icon.amount -= 1


def on_mouse_down(pos):
    global game_mode
    if game_mode == 'menu' and btn.collidepoint(pos):
        game_mode = 'game'


def update(dt):
    global zombie, game_mode
    player_movement()
    for i in range(len(zombies)):
        zombies[i] = update_enemy(zombies[i], jellos)

    if peco.colliderect(key) and key_icon.amount == 0:
        key_icon.amount += 1
    if peco.collidelist(zombies) != -1:
        game_mode = 'game over'

    for jello in jellos:
        jello.time += dt
        if jello.time >= 4:
            jello.pos = (-100, -100)

    for bomb in bombs:
        bomb.time += dt
        if bomb.time >= 2 and not bomb.set:
            bomb.set = True
            bomb.image = 'explotion_animation1'
            for zombi in zombies:
                if bomb.colliderect(zombi):
                    zombi.x  = WIDTH + 100
        if bomb.time >= 2 and bomb.set:
            number = int(bomb.image[-1]) + 1
            if number <= 8:
                bomb.image = f'explotion_animation{number}'
            else:
                bomb.pos = (-100, -100)
pgzrun.go()
