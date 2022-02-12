import pgzrun

WIDTH = 600
HEIGHT = 500
FPS = 60
TITLE = 'my game'

peco = Actor("front")
background = Actor("background")

def draw():
    background.draw()
    peco.draw()

def update(dt):
    if keyboard.left and peco.x > 20:
        peco.x -= 5
        peco.image  = 'left'
    elif keyboard.right and peco.x < 580:
        peco.x += 5
        peco.image = "right"
    elif keyboard.up:
        peco.y -= 5
        peco.image = "back"
    elif keyboard.down:
        peco.y += 5
        peco.image = "front"
pgzrun.go()
