"""
This program draws a orange and yellow honeycomb with a black colored bee in the
corner. This programs works on CodeHS.
"""
#Function to color the background orange
radius = 40
def background():
    speed(0)
    penup()
    bgcolor("orange")
    setposition(-200,-200)

#Function to draw 3 hexagons drawn around one point(honeycomb)
def three_hex():
    pendown()
    color("gold")
    pensize(3)
    for i in range(3):
        circle(20, 360, 6)
        left(120)
        
#Function to repeat the function as many times as it takes to draw a row of hexgons (honeycomb)
def hex_row():
    for i in range(8):
        three_hex()
        left(90)
        penup()
        forward(60)
        right(90)
    
#Function to repeat drawing of rows to fill the screen with hexagons (honeycomb)
def honeycomb ():
    for i in range(8):
        hex_row()
        penup()
        left(90)
        backward(480)
        right(90)
        forward(70)
        
#Function to draw abdomen (bee)
def abdomen():
    penup()
    setposition(-100, -100)
    color("black")
    right(30)
    begin_fill()
    circle(radius, 160, 50)
    left(25)
    circle(radius, 160, 50)
    end_fill()
    left(100)
    forward(80)

#Function to draw thorax (bee)
def thorax():
    backward(15)
    right(90)
    begin_fill()
    circle(20)
    end_fill()
    
#Function to draw head (bee)
def head():
    pendown()
    left(90)
    forward(27.5)
    right(90)
    begin_fill()
    circle(15)
    end_fill() 
    
#Function to draw wings (bee)
def wings():
    penup()
    right(90)
    forward(15)
    left(65)
    #Make a function for the actual wing drawing since it repeats
    def one_wing():
        pendown()
        pensize(1)
        for i in range(2):
            circle(92, 60)
            left(110)
    one_wing()
    right(160)
    one_wing()
    
#Function to draw legs (bee)
def legs():
    penup()
    left(80)
    forward(20)
    def bottom_leg(direction):
        pensize(5)
        pendown()
        circle(direction, 19)
    def middle_leg(direction, rotation):
        #penup()
        right(180)
        circle(-direction, 30)
        right(rotation)
        pendown()
        circle(direction, 25)
    #color("red")
    bottom_leg(100)
    middle_leg(100, 200)
    penup()
    right(205)
    forward(55)
    right(35)
    bottom_leg(-100)
    middle_leg(-100, -200)
    penup()
    setposition(-100, -100)
    def top_leg(direction):
        penup()
        pensize(3)
        left(direction)
        pendown()
        forward(35)
        backward(35)
        right(direction)
    left(111)
    forward(93)
    left(3)
    top_leg(65)
    top_leg(-65)
    
#Function to draw antenna (bee)
def antennas():
    forward(20)
    def antenna(direction):
        left(direction)
        pensize(1)
        forward(25)
        backward(25)
        right(direction)
    antenna(25)
    antenna(-25)
    backward(20)
    
#Final program
background()
honeycomb()
abdomen()
thorax()
head()
wings()
legs()
antennas()
