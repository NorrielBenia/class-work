x = 0
x_two=0

def setup():
    size(640, 480)


def draw():
    global x
    global x_two
    if mousePressed == True:
        coloursun= "#FFFFFF"
        skycolour= "#120026"
        cloudcolour="#B9B9B9"
        grasscolour="#2c6026"
        snow="#d1d1d1"
        mountain1="#161616"
        mountain2="#272727"
        

    else:
        coloursun= "#F9D800"
        skycolour="#87CEFA"
        cloudcolour="#F3F3F3"
        grasscolour="#31B522"
        snow="#FFFFFF"
        mountain1="#232323"
        mountain2="#323232"
        
    
    if x >= 766:
        x = 0
    x += 1.5

    background(skycolour)  # sky blue
    
    #sun
    noStroke()
    fill(coloursun)
    ellipse(600,0,240,240)
    
        #mountain 1
    stroke(1)
    fill(mountain1)
    triangle(82*2.25,180*2.25,65*4.5,35*4.5,190*2.25,180*2.25)
    noStroke()
    fill(snow)
    triangle(255,245,65*4.5,35*4.5,340,245)

    #mountain 2
    stroke(1)
    fill(mountain2)
    triangle(-67,480,130,60,325,480)
    noStroke()
    fill(snow)
    triangle(90.5,150,130,60,171,150)

        #grass
    noStroke()
    fill(grasscolour)
    rect(0, height/1.25, 640, 480)
    
    #clouds 
    fill(cloudcolour)
    ellipse(x-15-55, 80, 50, 50)
    ellipse(x+15-55, 80, 50, 50)
    ellipse(x-5-55, 60, 50, 50)
    ellipse(x-50-55, 65, 55, 55)
    ellipse(x-10-55, 65, 55, 55)
    ellipse(x-30-55, 45, 55, 55)
