import pygame

pygame.init()
# size of the screen, (width, height)
resolution = (600, 300)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((220,250,247))

    # puts the conetent on screen
    pygame.display.flip()
    clock.tick(60) # limits FPS to 60

pygame.quit()