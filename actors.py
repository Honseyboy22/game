from pgzero.builtins import Actor
from random import randint

peco = Actor("front")
bg = Actor("background")
menu_bg = Actor('menu_screen')
go_bg = Actor('game_over')
btn = Actor('start_btn', (300, 300))
zombies = []
for i in range(5):
    zombie = Actor('zombie_front', (randint(300, 650), randint(50, 450)))
    zombies.append(zombie)

chest = Actor("chest", (150, 100), (40, 40))
bomb_icon = Actor('bomb', (550, 20))
bomb_icon.amount = 3
jello_icon = Actor('jelo_trap', (440, 10))
jello_icon.amount = 2
key = Actor('key', (500, 450))
key_icon = Actor('key', (500, 20))
key_icon.amount = 0
