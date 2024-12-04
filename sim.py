import pygame 

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280,720))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
    pygame.draw.rect(screen,(200,200,150),(640,700,20,20))
    pygame.display.flip()
    clock.tick(60)