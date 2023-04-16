from pygame import *

#создай окно игры

window = display.set_mode((700,500))
display.set_caption("vietnam run:1969")
background = transform.scale(image.load("background.jpg"),(700,500))
viet = transform.scale(image.load("sprite1.jpg"),(50,50))
usa = transform.scale(image.load("sprite2.jpg"),(50,50))
x1= 0
x2 = 50
y1 = 0
y2 = 50 
clock = time.Clock()
FPS  = 60

game = True
while game:
    window.blit(background,(0,0))
    window.blit(viet,(x1,y1))
    window.blit(usa,(x2,y2))
    for e in event.get():
        if e.type == QUIT:
            game = False

    keys_pressed = key.get_pressed()

    if keys_pressed[K_UP]and y1 > 0:
        y1 -= 10
    if keys_pressed[K_DOWN]and y1 < 450:
        y1 += 10
    if keys_pressed[K_LEFT]and x1 > 0:
        x1 -= 10
    if keys_pressed[K_RIGHT]and x1 < 650:
        x1 += 10
    if keys_pressed[K_s] and y2 < 450:
        y2 += 10
    if keys_pressed[K_w] and y2 > 0:
        y2 -= 10
    if keys_pressed[K_d] and x2 < 650:
        x2 += 10
    if keys_pressed[K_a] and x2 > 0:
        x2 -= 10

    
    display.update()
    clock.tick(FPS)
      
#задай фон сцены




#обработай событие «клик по кнопке "Закрыть окно"»