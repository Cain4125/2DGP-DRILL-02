from pico2d import *
import math

open_canvas()
# fill here
grass = load_image('grass.png')
character = load_image('character.png')

def move(x=400,y=90):
    while x < 785:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x,y)
        update_canvas()
        x = x + 2
        delay(0.001)
    while y<560:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x,y)
        update_canvas()
        y = y + 2
        delay(0.001)
    while x > 15:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x,y)
        update_canvas()
        x = x - 2
        delay(0.001)
    while y>90:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x,y)
        update_canvas()
        y = y - 2
        delay(0.001)
    while x < 400:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x,y)
        update_canvas()
        x = x + 2
        delay(0.001) #(800,310)
    start_x, start_y = x, y
    r = 230
    cx = start_x
    cy = start_y + r
    for a in range(270, -90, -1):
        rad = math.radians(a)
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x,y)
        update_canvas()
        delay(0.001)


while True:
    move()
delay(2)



close_canvas()
