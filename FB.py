import cocos
from cocos.layer.util_layers import ColorLayer
#cocos.layer.base_layers.Layer
from cocos.actions.interval_actions import MoveTo, MoveBy, RotateBy
from math import sin, cos, pi, atan2
from cocos.actions.base_actions import Repeat
from time import sleep
from random import uniform
import schedule
import time

phi = 0

class Level1(cocos.scene.Scene):
    is_event_handler = True
    def __init__(self):
        super().__init__()
        rx = 400
        ry = 600
        
        Background = ColorLayer(0, 255,255,50, width=rx, height=ry)
        Background.position = (50,50)
        self.add(Background)
        Scenery = cocos.sprite.Sprite('Scenery.png', position=(0,0), color=(127,0,127))
        Scenery.scale = 1
        Background.add(Scenery)
        
        Columns = ColorLayer(0, 255,128,10, width=rx, height=ry)
        Columns.position = (40,60)
        self.add(Columns)
        Tube1 = []
        Tube2 = []
        a = MoveBy((-50, 0), duration = 10) + MoveTo((300, 50), duration = 0.1)
        a = Repeat(a)

        lasty = 0

        def make_column():
            lasty = 0
            rand = uniform(400)
            lasty = max(lasty + rand, -lasty-rand)
            lasty = min(lasty, 800 - lasty)
            Tube1.append(cocos.sprite.Sprite('Tube1.png', position=(100,lasty), color=(127,0,255)))
            Tube1[len(Tube1)].scale = 1/3
            Columns.add(Tube1[len(Tube1)])
            Tube1[len(Tube1)].do(a)
            print(lasty)
            '''
            Tube = cocos.sprite.Sprite('Tube2.png', position=(100 + i*150,50), color=(127,0,255))
            Tube.scale = 1/3
            Tube2.append(Tube)
            Columns.add(Tube2[i])'''
        schedule.every(0.2).minutes.do(make_column)
        
        Player = cocos.layer.Layer()
        Player.position = (0,0)
        self.add(Player)

        Bird = cocos.sprite.Sprite('Bird.png', position=(0,0), color=(127,0,127))
        Bird.scale = 1/10
        Player.add(Bird)

        Bird.do(MoveTo((100,100), duration=0))

        '''r = 150
        a = MoveBy((0,r), duration=1)
        a2 = RotateBy(360, duration=2)*25
        for act in [MoveBy((r*cos(2*pi/5*2*alpha),r*sin(2*pi/5*2*alpha)),duration=2) for alpha in range(5)]*5:
            a += act

        a = Repeat(a)'''

        #mish1.do(a)
        #mish2.do(a)
        
        mouse_layer = MouseDisplay(Bird)
        mouse_layer.position = (0, 0)
        self.add(mouse_layer)

        

class MouseDisplay(cocos.layer.Layer):

    is_event_handler = True     #: enable director.window events
    global phi

    def __init__(self, Bird):
        super( MouseDisplay, self ).__init__()
        self.Bird = Bird

        self.posx = 100
        self.posy = 240
        self.text = cocos.text.Label('No mouse events yet', font_size=18, x=self.posx, y=self.posy )
        self.add( self.text )

    def update_text (self, x, y):
        text = 'Mouse @ %d,%d' % (x, y)
        self.text.element.text = text
        self.text.element.x = self.posx
        self.text.element.y = self.posy
        
    def on_mouse_motion (self, x, y, dx, dy):
        self.update_text (x, y)
        phi = 0 
        phi = atan2(y, x)

        self.Bird.rotation = -180/pi*phi

    def on_mouse_press(self, x, y, buttons, modifiers):
        a2 = MoveBy((0,0), duration=0)
        for act in [MoveBy((0,-4*(i-0.5)**2+25),duration = 0.4) for i in range(10)]:
            a2 += act

        a2 = Repeat(a2)
        self.Bird.do(a2)
    '''
import schedule
import time

def job():
    print("I'm working...")

schedule.every(0.2).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)


'''
'''
while 1:
    schedule.run_pending()
    time.sleep(1)
'''
cocos.director.director.init()
main_scene = cocos.scene.Scene (Level1())
cocos.director.director.run (main_scene)
