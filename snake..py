import pygame

pygame.init()

game_interface = pygame.display.set_mode((500,500))
pygame.display.update()
pygame.display.set_caption('Snake Game - Tirth Thakar')
game_finished = False
while not game_finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_finished = True
pygame.quit()
quit()

