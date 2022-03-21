import pygame, os

size = (220, 400)
screen = pygame.display.set_mode(size)

run = True

buttons = [
            pygame.Rect(10, 10, 200, 50),
            pygame.Rect(10, 70, 200, 50),
        ]

while run:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            left, middle, right = pygame.mouse.get_pressed()
            mx, my = pygame.mouse.get_pos()
            if left:
                if buttons[0].collidepoint((mx, my)):
                    os.system('python3 Encoder/newencoder.py')
                if buttons[1].collidepoint((mx, my)):
                    print('palette')

    for btn in buttons:
        pygame.draw.rect(screen, (255, 255, 255), btn)
    
    pygame.display.update()

pygame.quit()
