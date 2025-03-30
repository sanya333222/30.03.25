x=500
def setup():
    size(600, 400)
def draw():
    global x
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(300,200,x,x)
    x=x-1
    
