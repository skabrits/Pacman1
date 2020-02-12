import cocos
import random
from cocos.text import Label
from time import sleep
from cocos.actions.interval_actions import MoveTo, MoveBy, RotateBy
from cocos.actions.base_actions import Repeat
from math import sin, cos, pi, atan, degrees, fabs, radians, atan2
from cocos import layer
from cocos.sprite import Sprite
from cocos.actions.instant_actions import CallFunc

cocos.director.director.init(autoscale = False)

vx = 100
targ = []
class Bird(Sprite):
    gravity = 200
    def __init__(self, mi, L):
        super(Bird, self).__init__('fpfb.png', position=(100, 200))
        (self.corx, self.cory, self.vy) = (100, 200, 0)
        self.scale = 2
        self.schedule(self.move)
        self.mi = mi
        self.L = L

    def move(self, dt):
        self.cory += self.vy*dt
        v = self.vy*dt
        self.do(MoveBy((0, v), dt))
        self.vy -= self.gravity*dt
        self.colis_earth()
        self.mi.objcol(self.corx, self.cory)
        self.rotation = degrees(-atan2(self.vy, vx))

    def colis_earth(self):
        if self.cory < 60:
            self.L.die()
    def up(self):
        self.vy = 0
        self.vy += 250


class MouseInput(layer.Layer):

    is_event_handler = True

    def __init__(self, L):
        super(MouseInput, self).__init__()
        self.bird = Bird(self,L)
        self.add(self.bird)
        global  targ
        self.targ = targ
        self.L = L

    def objcol(self, x, y):
        global targ
        self.targ = targ
        for i in self.targ:
            if (i.x - i.width/2 <= x and i.x + i.width/2 >= x and i.y - i.height/2 <= y and i.y + i.height/2 >= y):
                self.L.die()

    def on_mouse_press(self, x, y, buttons, modifiers):
        self.bird.up()

class Tubes(layer.Layer):
    def __init__(self, cx):
        super(Tubes, self).__init__()
        a = random.randint(-15, 70)
        self.checked = False
        self.t1 = cocos.sprite.Sprite('fptb.png', position=(cx, 480 + a))
        self.t1.scale = 2
        self.t2 = cocos.sprite.Sprite('fptbupsd.png', position=(cx, a))
        self.t2.scale = 2

        global targ
        targ.append(self.t1)
        targ.append(self.t2)

        self.add(self.t1)
        self.add(self.t2)

        self.cx = cx

        self.schedule(self.move)
    def move(self, dt):
        self.t1.do(MoveBy((-vx*dt, 0), dt))
        self.t2.do(MoveBy((-vx * dt, 0), dt))

        if self.t1.x < -20:
            self.t1.kill()
            self.t2.kill()

            a = random.randint(-15, 70)
            self.checked = False
            self.t1 = cocos.sprite.Sprite('fptb.png', position=(500+self.cx, 480 + a))
            self.t1.scale = 2
            self.t2 = cocos.sprite.Sprite('fptbupsd.png', position=(500+self.cx, a))
            self.t2.scale = 2

            global targ
            targ.append(self.t1)
            targ.append(self.t2)

            self.add(self.t1)
            self.add(self.t2)

    def objscore(self, x):
        if (self.t1.x - self.t1.width/2 <= x and self.t1.x + self.t1.width/2 >= x):
            j = self.checked
            self.checked = True
            return True and not j
        return False



class Ground(layer.Layer):
    def __init__(self):
        super(Ground, self).__init__()
        self.g1 = cocos.sprite.Sprite('fpzemlya.png', position=(167, 0))
        self.g1.scale = 2
        self.g1.scale_x = 3
        self.g2 = cocos.sprite.Sprite('fpzemlya.png', position=(167*3, 0))
        self.g2.scale = 2
        self.g2.scale_x = 3

        self.add(self.g1)
        self.add(self.g2)

        self.schedule(self.move)
    def move(self, dt):
        self.g1.do(MoveBy((-vx*dt, 0), dt))
        self.g2.do(MoveBy((-vx * dt, 0), dt))
        if (self.g1.x <= -167):
            self.g1.kill()
            self.g2.kill()
            self.g1 = cocos.sprite.Sprite('fpzemlya.png', position=(167, 0))
            self.g1.scale = 2
            self.g1.scale_x = 3
            self.g2 = cocos.sprite.Sprite('fpzemlya.png', position=(167 * 3, 0))
            self.g2.scale = 2
            self.g2.scale_x = 3

            self.add(self.g1)
            self.add(self.g2)

class Death(cocos.scene.Scene):

    def tend(self):
        self.killl = True

    def __init__(self):
        super().__init__()
        global targ
        targ = []
        l = Label('Wasted', (300, 200))
        self.add(l)
        l.do(RotateBy(720, 1))
        d1 = cocos.sprite.Sprite('fpfb.png', position=(200, 200))
        self.killl = False
        self.schedule(killl, self, d1)
        self.add(d1)
        a = RotateBy(360, 6) + CallFunc(self.tend())
        d1.do(a)

class Level1(cocos.scene.Scene):
    def die(self):
        self.is_dead = True

    def __init__(self):
        super().__init__()

        self.is_dead = False

        lb = layer.Layer()
        lbm = Ground()
        self.lt = Tubes(300)
        self.lt2 = Tubes(800)
        # lt3 = Tubes(150)
        self.lt4 = Tubes(550)
        sp = cocos.sprite.Sprite('fpbg.png', position=(142,240))
        sp.scale = 2
        spa = cocos.sprite.Sprite('fpbg.png', position=(142+275, 240))
        spa.scale = 2
        spar = cocos.sprite.Sprite('fpbg.png', position=(142 + 275*2, 240))
        spar.scale = 2

        self.scor = 0
        self.lbl = Label('0', (50,440), color = (0,0,0,255))
        self.schedule(self.score)

        self.lf = MouseInput(self)
        
        lb.add(sp)
        lb.add(spa)
        lb.add(spar)

        self.add(lb)

        self.add(lbm)

        self.add(self.lt)

        self.add(self.lt2)

        # self.add(lt3)

        self.add(self.lt4)

        self.lf.add(self.lbl)
        self.add(self.lf)

    def score(self, dt):
        if (self.lt.objscore(100) or self.lt2.objscore(100) or self.lt4.objscore(100)):
            self.scor += 1
            self.lbl.element.text = str(self.scor)

def killl(dt, v, s):
    if (v.killl and s.rotation > 350):
        v.killl = False
        l2 = Level1()
        l2.schedule(dest, l2)
        cocos.director.director.replace(l2)


def dest(dt, l1):
    if (l1.is_dead):
        l2 = Level1()
        l2.schedule(dest, l2)
        cocos.director.director.replace(Death())

l1 = Level1()

l1.schedule(dest, l1)

cocos.director.director.run(l1)