from pico2d import *
from math import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

check = 0

while(True):
    if(check == 0):
        x = 400
        y = 90
        while(x<785):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x += 2
            delay(0.01)
        while(y<555):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y += 2
            delay(0.01)
        while(x>15):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x -= 2
            delay(0.01)
        while(y>90):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y -= 2
            delay(0.01)
        while(x<400):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x += 2
            delay(0.01)
        check += 1
    elif(check == 1):
          seta = 270
          while(seta < 630):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x = 400 + 200 * cos(radians(seta))
            y = 300 + 200 * sin(radians(seta))
            seta += 1
            delay(0.01)
          check -= 1
