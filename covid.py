import turtle as t

def drawTriangel(small):
    t.fd(-small/2)
    for i in range(3):
        t.fd(small)
        t.lt(120)
    t.fd(small/2)


def drawSpike(small):
    t.pu()
    t.fd(size)
    t.pd()
    t.fd(20)
    t.rt(90)
    t.pd()

    t.fillcolor("orange")
    t.begin_fill()
    drawTriangel(small)
    t.end_fill()
    t.lt(90)
    t.pu()
    t.fd((-size)-20)
    


# change this variable to set the square size
size = 100
small = 20


# --------------------------------
# Main program starts here
#---------------------------------
t.title("620610589 Draw Covid-19")

t.clear()
t.speed(100)
t.pd()
t.fillcolor("red")
t.begin_fill()
t.circle(size)
t.end_fill()
t.lt(90)
t.pu()
t.fd(size)

for i in range(18):
    drawSpike(small)
    t.lt (360/18)








