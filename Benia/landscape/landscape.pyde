x = 0

def setup():
    size(640, 480)


def draw():
    global x
    
    if x >= 765:
        x = 0
    x += 1.5
    
    background(135, 206, 250)  # sky blue
    
    #sun
    noStroke()
    fill("#F9D800")
    ellipse(600,0,240,240)
    
        #mountain 1
    stroke(1)
    fill(35,35,35)
    triangle(82*2.25,180*2.25,65*4.5,35*4.5,190*2.25,180*2.25)
    noStroke()
    fill(255,255,255)
    triangle(255,245,65*4.5,35*4.5,340,245)

    #mountain 2
    stroke(1)
    fill(50,50,50)
    triangle(-67,480,130,60,325,480)
    noStroke()
    fill(255,255,255)
    triangle(90.5,150,130,60,171,150)

    
        #grass
    noStroke()
    fill("#31B522")
    rect(0, height/1.25, 640, 480)
    
    #clouds 
    fill(245,245,2545)
    ellipse(x-15-55, 80, 50, 50)
    ellipse(x+15-55, 80, 50, 50)
    ellipse(x-5-55, 60, 50, 50)
    ellipse(x-50-55, 65, 55, 55)
    ellipse(x-10-55, 65, 55, 55)
    ellipse(x-30-55, 45, 55, 55)
