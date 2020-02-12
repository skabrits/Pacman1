from random import uniform

def start(state):
    state.points = [[uniform(100, 400), uniform(100,400), uniform(-5, 5), uniform(-5,5)] for _ in range(100)]

def update(state):
    def update_coord(point):
        x,y,vx,vy = point
        x += vx
        y += vy
        return [x,y,vx,vy]
    def update_velocity(point):
        x,y,vx,vy = point
        vx = vx if 0<=x<500 else -vx
        vy = vy if 0<=y<500 else -vy
        return [x,y,vx,vy]
    state.points = [update_velocity(update_coord(point)) for point in state.points]
