from random import uniform

def start(state):
    state.points = [[uniform(100, 400), uniform(100,400), uniform(-5, 5), uniform(-5,5)] for _ in range(100)]

def update(state):
    state.points = [[
        x+vx if 0<=x<500 else x-vx,
        y+vy if 0<=y<500 else y-vy,
        vx if 0<=x<500 else -vx,
        vy if 0<=y<500 else -vy]
        for x,y,vx,vy in state.points]
