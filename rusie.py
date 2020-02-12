import cocos
from cocos.actions.interval_actions import MoveTo, MoveBy, RotateBy
from cocos.actions.base_actions import Repeat
from math import sin, cos, pi, atan, degrees, fabs, radians
from cocos import layer
from cocos.actions.instant_actions import CallFunc

class MouseInput(layer.Layer):

    is_event_handler = True

    def __init__(self, targ):
        super(MouseInput, self).__init__()
        self.sp2 = cocos.sprite.Sprite('wep.png', position=(120, 35))
        self.sp2.scale = 0.6
        self.add(self.sp2)
        self.targ = targ

    def killen(self, x, y):
        for i in self.targ:
            if (i.x - i.width/2 <= x + self.x and i.x + i.width/2 >= x + self.x and i.y - i.height/2 <= y + self.y and i.y + i.height/2 >= y + self.y):
                i.kill()

    def on_mouse_motion(self, x, y, dx, dy):
        (x1, y1) = cocos.director.director.get_virtual_coordinates(x, y)
        try:
            self.sp2.rotation = degrees(atan((self.sp2.x - x1) / (self.sp2.y - y1))) + 90 * fabs(self.sp2.y - y1)/(self.sp2.y - y1) +7
        except:
            self.sp2.rotation = fabs(self.sp2.x - x1)/(self.sp2.x - x1) * 90 + 97

    def on_mouse_press(self, x, y, buttons, modifiers):
        (x1, y1) = cocos.director.director.get_virtual_coordinates(x, y)
        spb = cocos.sprite.Sprite('bul.png', position=(120 + (self.sp2.width/2) * (sin(radians(self.sp2.rotation + 83))), 40 + (self.sp2.width/2) * (cos(radians(self.sp2.rotation + 83)))))
        spb.rotation = self.sp2.rotation
        spb.scale = 0.3
        self.add(spb)
        self.killen(x1, y1)

class Level1(cocos.scene.Scene):
    def __init__(self):
        super().__init__()

        lb = layer.Layer()
        lt = layer.Layer()
        sp = cocos.sprite.Sprite('fon.jpg', position=(320,240), color=(127,0,255))
        sp.scale = 3

        sp11 = cocos.sprite.Sprite('enem.png', position=(420,240))
        sp11.scale = 0.4
        sp1 = cocos.sprite.Sprite('enem.png', position=(200,140))
        sp1.scale = 0.4

        lf = MouseInput([sp1, sp11])
        
        lb.add(sp)
        self.add(lb)
        
        lt.add(sp1)
        lt.add(sp11)
        self.add(lt)

        self.add(lf)
        

        r = 150
        b = MoveBy((0,r), duration=2)
        a = MoveBy((0,0), duration=0)
        a2 = Repeat(RotateBy(360, duration=2))
        a3 = Repeat(RotateBy(-560, duration=1))
        for act in [MoveBy((r*cos(2*pi/5*2*alpha),r*sin(2*pi/5*2*alpha)),duration=2) for alpha in range(5)]:
            a += act
        a = b + Repeat(a)
        sp1.do(a|a2)
        sp11.do(a|a3)

cocos.director.director.init(autoscale = False)
cocos.director.director.run(Level1())
