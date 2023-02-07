Tina_the_Blob = Actor('character')
Tina_the_Blob.pos= 100,50

WIDTH = 500
HEIGHT = Tina_the_Blob.height + 20

def draw():
    screen.clear()
    screen.fill((0, 0, 255))
    Tina_the_Blob.draw()

def update():
    Tina_the_Blob.left = Tina_the_Blob.left + 2
    if Tina_the_Blob.left > WIDTH:
        Tina_the_Blob.right = 0


