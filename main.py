import pgzrun

WIDTH = 600
HEIGHT = 500
FPS = 60
TITLE = 'my game'

peco = Actor("front")
background = Actor("new background")
enemy = Actor("zombie_side")
menu = Actor("title screen 2")
enemies = [enemy((300, 50), (15, 30)), enemy((300, 100), (15, 30))]
obstacle = Actor("chest", (150, 100), (40, 40))

def draw():
    background.draw()
    peco.draw()
    for enemy in enemies:
        screen.draw.filled_rect(enemy, (200, 0, 0))
    screen.draw.filled_rect(obstacle, (0, 200, 0))


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
    if enemy.colliderect(obstacle):
        if obstacle.top < enemy.bottom and enemy.y < obstacle.y:
            enemy.bottom = obstacle.top - 0.5
        elif obstacle.bottom < enemy.top and enemy.y > obstacle.y:
            enemy.top = obstacle.bottom + 0.5
        elif obstacle.right > enemy.left and enemy.x > obstacle.x:
            enemy.left = obstacle.right + 0.5
        elif obstacle.left < enemy.right and enemy.x < obstacle.x:
            enemy.right = obstacle.left - 0.5

    elif enemy.x - 50 < peco.x < enemy.x + 50 and \
            enemy.y - 100 < peco.y < enemy.y + 100:
        if enemy.x < peco.x:
            enemy.x += 1
        else:
            enemy.x -= 1
        if enemy.y < peco.y:
            enemy.y += 1
        else:
            enemy.y -= 1
    else:
        enemy.x -= 0.5
    return enemy


def update(dt):
    global enemies
    player_movement()
    for enemy in enemies:
        enemy = update_enemy(enemy)


pgzrun.go()
