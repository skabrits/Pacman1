from random import uniform

def start(state):
    state.points = [[uniform(100, 400), uniform(100,400), uniform(-5, 5), uniform(-5,5)] for _ in range(100)]

def update(state):
    new_points = []
    for x,y,vx,vy in state.points:
        vx = vx if 0<=x<500 else -vx
        vy = vy if 0<=y<500 else -vy
        x += vx
        y += vy
        new_points.append([x,y,vx,vy])
    state.points = new_points
