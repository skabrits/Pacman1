from functools import partial
from tkinter import *
from random import randint
import math
import cocos
from cocos import layer
import pampy as pm

import numpy as np
from numpy import *
import random
from time import sleep
from cocos import actions
from pyglet.window import key
from math import ceil
from math import floor
from array_to_graph import convert_mas_to_graf, convert, level, answ
from itertools import product as pdct

import xlrd
difficulty = 1

workbook = xlrd.open_workbook('Pacman_config.xlsx')
worksheet = workbook.sheet_by_index(0)
speeds = dict()
conditions = ["nm", "nd","ft","fd"]
levels = list(worksheet.col_values(0, start_rowx=2, end_rowx=6))
for i in pdct(levels, conditions):
    cval = worksheet.cell(levels.index(i[0])+2, conditions.index(i[1])+1).value
    if cval == "-":
        speeds[i] = 0
    else:
        speeds[i] = float(cval)

coef = 14.95
left_offset = 98
down_offset = 21
Pack_c = 1 + 7 * np.complex(0,1)

score = 0
dots = [] #little yellow circles
privedenia = [] #sprites

def intellect(self, Packman):
    pass

def mistake_square(comp):
    return math.sqrt(sum([i ** 2 for i in [comp.real, comp.imag]]) / 2)

def round_forward(x, direction):
    if direction > 0:
        return ceil(x + 0.05)
    elif direction < 0:
        return floor(x - 0.05)
    else:
        return round(x)

keyboard = key.KeyStateHandler()

j = complex(0,1)
# graf = {
#
#     1 + 7 * j: [2 + 7 * j, 1 + 8 * j], 2 + 7 * j: [1 + 7 * j, 3 + 7 * j], 3 + 7 * j: [2 + 7 * j, 4 + 6 * j], 6 + 7 * j: [7 + 7 * j, 6 + 6 * j, 6 + 8 * j], 7 + 7 * j: [6 + 7 * j, 8 + 7 * j], 8 + 7 * j: [7 + 7 * j, 9 + 7 * j], 9 + 7 * j: [8 + 7 * j, 10 + 7 * j, 9 + 6 * j], 10 + 7 * j: [9 + 7 * j, 11 + 7 * j], 11 + 7 * j: [10 + 7 * j, 12 + 7 * j], 12 + 7 * j: [11 + 7 * j, 13 + 7 * j, 12 + 8 * j], 13 + 7 * j: [12 + 7 * j, 14 + 7 * j], 14 + 7 * j: [13 + 7 * j, 15 + 7 * j], 15 + 7 * j: [14 + 7 * j, 16 + 7 * j, 15 + 8 * j], 16 + 7 * j: [15 + 7 * j, 17 + 7 * j], 17 + 7 * j: [16 + 7 * j, 18 + 7 * j], 18 + 7 * j: [17 + 7 * j, 19 + 7 * j, 18 + 6 * j], 19 + 7 * j: [18 + 7 * j, 20 + 7 * j], 20 + 7 * j: [19 + 7 * j, 21 + 7 * j], 21 + 7 * j: [20 + 7 * j, 21 + 6 * j, 21 + 8 * j], 24 + 7 * j: [25 + 7 * j, 24 + 6 * j], 25 + 7 * j: [24 + 7 * j, 26 + 7 * j], 26 + 7 * j: [25 + 7 * j, 26 + 8 * j],
#     3 + 6 * j: [3 + 5 * j, 3 + 7 * j], 6 + 6 * j: [6 + 5 * j, 6 + 7 * j], 9 + 6 * j: [9 + 5 * j, 9 + 7 * j], 18 + 6 * j: [18 + 5 * j, 18 + 7 * j], 21 + 6 * j: [21 + 5 * j, 21 + 7 * j], 24 + 6 * j: [24 + 5 * j, 24 + 7 * j],
#     3 + 5 * j: [3 + 4 * j, 3 + 6 * j], 6 + 5 * j: [6 + 4 * j, 6 + 6 * j], 9 + 5 * j: [9 + 4 * j, 9 + 6 * j], 18 + 5 * j: [18 + 4 * j, 18 + 6 * j], 21 + 5 * j: [21 + 4 * j, 21 + 6 * j], 24 + 5 * j: [24 + 4 * j, 24 + 6 * j],
#     1 + 4 * j: [2 + 4 * j, 1 + 3 * j], 2 + 4 * j: [1 + 4 * j, 3 + 4 * j], 3 + 4 * j: [2 + 4 * j, 4 + 4 * j, 3 + 5 * j], 4 + 4 * j: [3 + 4 * j, 5 + 4 * j], 5 + 4 * j: [4 + 4 * j, 6 + 4 * j], 6 + 4 * j: [5 + 4 * j, 7 + 4 * j, 6 + 5 * j], 9 + 4 * j: [8 + 4 * j, 10 + 4 * j, 9 + 5 * j], 10 + 4 * j: [9 + 4 * j, 11 + 4 * j], 11 + 4 * j: [10 + 4 * j, 12 + 4 * j], 12 + 4 * j: [11 + 4 * j, 12 + 3 * j], 15 + 4 * j: [14 + 4 * j, 16 + 4 * j, 15 + 3 * j], 16 + 4 * j: [15 + 4 * j, 17 + 4 * j], 17 + 4 * j: [16 + 4 * j, 18 + 4 * j], 18 + 4 * j: [17 + 4 * j, 19 + 4 * j, 18 + 5 * j], 21 + 4 * j: [20 + 4 * j, 22 + 4 * j, 21 + 5 * j], 22 + 4 * j: [21 + 4 * j, 23 + 4 * j], 23 + 4 * j: [22 + 4 * j, 24 + 4 * j], 24 + 4 * j: [23 + 4 * j, 25 + 4 * j, 24 + 5 * j], 25 + 4 * j: [24 + 4 * j, 26 + 4 * j], 26 + 4 * j: [25 + 4 * j, 26 + 3 * j],
#     1 + 3 * j: [1 + 2 * j, 1 + 4 * j], 12 + 3 * j: [12 + 2 * j, 12 + 4 * j], 15 + 3 * j: [15 + 2 * j, 15 + 4 * j], 26 + 3 * j: [26 + 2 * j, 26 + 4 * j],
#     1 + 2 * j: [1 + j, 1 + 3 * j], 12 + 2 * j: [12 + j, 12 + 3 * j], 15 + 2 * j: [15 + j, 15 + 3 * j], 26 + 2 * j: [26 + j, 26 + 3 * j],
#     1 + j: [2 + j, 1 + 2 * j], 2 + j: [1 + j, 3 + j], 3 + j: [2 + j, 4 + j], 4 + j: [3 + j, 5 + j], 5 + j: [4 + j, 6 + j], 6 + j: [5 + j, 7 + j], 7 + j: [6 + j, 8 + j], 8 + j: [7 + j, 9 + j], 9 + j: [8 + j, 10 + j], 10 + j: [9 + j, 11 + j], 11 + j: [10 + j, 12 + j], 12 + j: [11 + j, 13 + j, 12 + 2 * j], 13 + j: [12 + j, 14 + j], 14 + j: [13 + j, 15 + j], 15 + j: [14 + j, 16 + j, 15 + 2 * j], 16 + j: [15 + j, 17 + j], 17 + j: [16 + j, 18 + j], 18 + j: [17 + j, 19 + j], 19 + j: [18 + j, 20 + j], 20 + j: [19 + j, 21 + j], 21 + j: [20 + j, 22 + j], 22 + j: [21 + j, 23 + j], 23 + j: [22 + j, 24 + j], 24 + j: [23 + j, 25 + j], 25 + j: [24 + j, 26 + j], 26 + j: [25 + j, 26 + 2 * j]}

dots_graf = {} #return sprite fot the given graf vert
dots_to_graf = {} #return the graf vert for the given sprite

graf = answ(level)

def collision(Obj, level):
    global score
    some_dots = []
    main_sprite = Obj.sprite
    some_dots = list(graf[Obj.vert])
    #print(some_dots)
    some_dots.append(Obj.vert)
    #print(some_dots)
    for sprite in [dots_graf[i] for i in some_dots if (not dots_graf.get(i) == None)]:
        if (sprite.x - main_sprite.x)**2 + (sprite.y - main_sprite.y)**2 < 10:
            score += 1
            level.lbl.element.text = str(score)
            print(dots_to_graf[sprite])
            dots_graf[dots_to_graf[sprite]].kill()
            del dots_graf[dots_to_graf[sprite]]
    for obj in privedenia:
        sprite = obj.sprite
        if (sprite.x - main_sprite.x)**2 + (sprite.y - main_sprite.y)**2 < 10:
            print('Game over')

def choose_direction(self):
    return self.abs_speed * random.choice([i - self.vert for i in graf[self.vert]])





def kuda(self, Packman):
    graf_vert_to_steps = dict()
    graf_vert_to_steps[self.vert] = -1
    where = 0
    tr_set = set()
    next_vert = [Packman]
    for i in range(100000):
        nnv = []
        for v in next_vert:
            nnv.extend(graf[v])
            graf_vert_to_steps[v] = i
        tr_set.update(set(list(copy(next_vert))))
        next_vert = []
        for i in nnv:
            if not(i in tr_set):
                next_vert.append(i)
        if (graf_vert_to_steps[self.vert] != -1):
            where = min(map(lambda x: (graf_vert_to_steps[x], x) if x in tr_set else (10000000,x), graf[self.vert]))
            break
    print(graf_vert_to_steps)
    return self.abs_speed * (where - self.vert)







class Object:

    def __init__(self, my_vert, speed, image, abs_speed, ai = lambda self: self.wanted_speed):
        self.wanted_speed = 0 * j
        self.ai = ai
        self.abs_speed = abs_speed
        self.cord = my_vert * coef
        self.vert = my_vert
        self.speed = speed
        self.sprite = cocos.sprite.Sprite(image, position=(self.cord.real, self.cord.imag))

    def change_speed(self, t, pacman = False):
        if self.wanted_speed:
            wanted_cord = round_forward((self.cord.real + self.wanted_speed.real * t) / coef, self.wanted_speed.real) + round_forward((self.cord.imag + self.wanted_speed.imag * t) / coef, self.wanted_speed.imag) * j
            if wanted_cord in graf.keys():
                sur = (self.speed * self.wanted_speed) / self.abs_speed ** 2
                if (sur == j or sur == -j) and np.absolute((self.sprite.x - left_offset + (self.sprite.y - down_offset) * j) / coef - self.vert) < 0.5:
                    act = actions.Place((self.vert.real * coef + left_offset, self.vert.imag * coef + down_offset))
                    self.sprite.do(act)
                    self.cord = self.vert * coef
                    # print((self.sprite.x, self.sprite.y), " ", (self.vert.real * coef + left_offset, self.vert.imag * coef + down_offset))
                    self.speed = self.wanted_speed
                    self.wanted_speed = 0 * j
                    if(pacman):
                        self.sprite.rotation = np.angle(np.conj(self.speed), deg=True)
                elif sur == 1 or sur == -1 or sur == 0:
                    self.speed = self.wanted_speed
                    self.wanted_speed = 0 * j
                    if(pacman):
                        self.sprite.rotation = np.angle(np.conj(self.speed), deg=True)

    def moving(self, t, level, collide = False, pacman=False):
        self.change_speed(t,pacman)

        new_cord = round_forward((self.cord.real + self.speed.real * t) / coef, self.speed.real) + round_forward((self.cord.imag + self.speed.imag * t) / coef, self.speed.imag) * j

        if collide:
            collision(self, level)


        if new_cord in graf.keys():
            self.cord += self.speed * t
            plus = (round_forward(self.cord.real / coef, 0) + round_forward(self.cord.imag / coef, 0) * j) - self.vert
            if not(plus == 0):
                self.wanted_speed = self.ai(self)
            elif self.speed == 0:
                self.wanted_speed = self.ai(self)
            self.vert += plus
            self.paint(t)
            sur = (self.speed.real) / self.abs_speed
            if self.vert == 1 + 16 * j and sur == -1:
                self.vert = 26 + 16 * j
                act = actions.Place((self.vert.real * coef + left_offset, self.vert.imag * coef + down_offset))
                self.sprite.do(act)
                self.cord = self.vert * coef
            if self.vert == 26 + 16 * j and sur == 1:
                self.vert = 1 + 16 * j
                act = actions.Place((self.vert.real * coef + left_offset, self.vert.imag * coef + down_offset))
                self.sprite.do(act)
                self.cord = self.vert * coef
        else:
            self.speed = 0
            self.wanted_speed = self.ai(self)

    def paint(self, dt):
        act = actions.MoveTo((self.cord.real + left_offset, self.cord.imag + down_offset), dt)
        self.sprite.do(act)

# Tester = Object(1 + j, 10, 'blue.jpg')

SPEED = 75
FS = 5

class MouseInput(layer.Layer):

    is_event_handler = True

    def __init__(self):
        super(MouseInput, self).__init__()

        self.pacman = Object(1 + 7 * j, 0, 'packman.png', 50*speeds()/100)
        self.pacman.sprite.scale = 1 / 24
        self.add(self.pacman.sprite)

    def on_key_press(self, key_pressed, modifiers):

        if key_pressed == key.LEFT:
            self.pacman.wanted_speed = - self.pacman.abs_speed
        elif key_pressed == key.RIGHT:
            self.pacman.wanted_speed = self.pacman.abs_speed
        elif key_pressed == key.UP:
            self.pacman.wanted_speed = self.pacman.abs_speed * j
        elif key_pressed == key.DOWN:
            self.pacman.wanted_speed = - self.pacman.abs_speed * j


class Level1(cocos.scene.Scene):
    def __init__(self):
        super().__init__()

        pole = cocos.sprite.Sprite('pole.png', position=(300,240))
        pole.scale = 1/3.2
        pole.scale_x = 1.0365
        # pole.scale_y = 0.936

        background = layer.Layer()
        midle = layer.Layer()
        foreground = MouseInput()

        from cocos.text import Label

        self.lbl = Label('0', (50, 440), color=(255, 255, 255, 255))

        background.add(pole)
        background.add(self.lbl)
        self.add(background)

        kuda1 = partial(kuda, Packman=Pack_c)
        blue_prived = Object(2 + j, 50, 'blue.png', 50, kuda1)
        blue_prived.sprite.scale = 1 / 14
        privedenia.append(blue_prived)

        for complex_number in graf.keys():
            dots.append(cocos.sprite.Sprite('dot.png', position=(complex_number.real * coef + left_offset, complex_number.imag * coef + down_offset)))
            dots[-1].scale = 1 / 2
            midle.add(dots[-1])
            dots_graf.update({complex_number: dots[-1]})
            dots_to_graf.update({dots[-1]: complex_number})


        def callback(dt, *args, **kwargs):
            global Pack_c
            blue_prived.moving(dt, self)
            foreground.pacman.moving(dt, self, collide = True, pacman=True)
            Pack_c = foreground.pacman.vert

        midle.add(blue_prived.sprite)
        self.add(midle)
        self.add(foreground)
        self.schedule(callback)

cocos.director.director.init(autoscale=False)

cocos.director.director.window.push_handlers(keyboard)

cocos.director.director.run(Level1())
