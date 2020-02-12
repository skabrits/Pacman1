from random import uniform

def start(state):
    state.points = [[uniform(100, 400), uniform(100,400), uniform(-5, 5), uniform(-5,5)] for _ in range(100)]

def update(state):
    for p in state.points:
        p[0] += p[2]
        p[1] += p[3]
        p[2] = p[2] if 0<=p[0]<500 else -p[2]
        p[3] = p[3] if 0<=p[1]<500 else -p[3]
