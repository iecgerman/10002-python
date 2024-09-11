import pygame

from personaje import Cubo 
from enemigo import Enemigo

# pip install pygame

ANCHO = 1000
ALTO = 800
VENTANA = pygame.display.set_mode([ALTO,ANCHO])

jugando = True

cubo = Cubo(100,100)


enemigos = []

enemigos.append(Enemigo(ANCHO/2,100))

def gestionar_teclas(teclas):
    if teclas[pygame.K_w]:
        cubo.y -= cubo.velocidad
    if teclas[pygame.K_s]:
        cubo.y += cubo.velocidad
    if teclas[pygame.K_a]:
        cubo.x -= cubo.velocidad
    if teclas[pygame.K_d]:
        cubo.x += cubo.velocidad

while jugando:
    eventos =  pygame.event.get()

    teclas = pygame.key.get_pressed()

    gestionar_teclas(teclas)

    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False

    VENTANA.fill("black")
    cubo.dibujar(VENTANA)

    for enemigo in enemigos:
        enemigo.dibujar(VENTANA)
        enemigo.movimiento()

    pygame.display.update()

quit()