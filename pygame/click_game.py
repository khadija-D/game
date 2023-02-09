Tina_the_Blob = Actor('character')
Tina_the_Blob.pos= 100,50

WIDTH = 500
HEIGHT = Tina_the_Blob.height + 20

def draw():
    screen.clear
    screen.fill((0, 0, 255))
    Tina_the_Blob.draw()

def update():
    Tina_the_Blob.left = Tina_the_Blob.left + 2
    if Tina_the_Blob.left > WIDTH:
        Tina_the_Blob.right = 0
def on_mouse_down(pos):
    if Tina_the_Blob.collidepoint(pos):
        print ("Eek!")
        sounds.eep.play()
        set_character_clicked()
    else:
        print("LMAO")
def set_character_clicked():
    Tina_the_Blob.image = 'character_clicked'
    sounds.eep.play()
    clock.schedule_unique(set_character,1)
def set_character():
    Tina_the_Blob.image = 'character'

