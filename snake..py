import pygame

pygame.init()

# Setting up interface for the game using pygame built-in functions
game_interface = pygame.display.set_mode((500,500))
pygame.display.update()
# Setting window caption
pygame.display.set_caption('Snake Game - Tirth Thakar')
# Variable to keep track of whether or not game has ended or not
game_finished = False
# Loop to keep playing game while it has not ended and keep track of events
while not game_finished:
    for event in pygame.event.get():
        # If close button is pressed then end game
        if event.type == pygame.QUIT:
            game_finished = True

# End game once while loop has been exited
pygame.quit()
quit()

