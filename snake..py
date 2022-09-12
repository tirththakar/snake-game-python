import pygame

pygame.init()

# Setting up colours for the background, snake and food
background_colour = (255, 255, 191)
snake_colour = (0, 0, 255)
# Positional data
current_position = [250, 250, 10, 10]
x_cord_change = 0
y_cord_change = 0
# Setting up interface for the game using pygame built-in functions
game_interface = pygame.display.set_mode((500,500))
pygame.display.update()
# Setting window caption
pygame.display.set_caption('Snake Game - Tirth Thakar')
# Variable to keep track of whether or not game has ended or not
game_finished = False
# Function to action on event types
def execute_events(game_finished, x_cord_change, y_cord_change):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_cord_change = -10
                y_cord_change = 0
            elif event.key == pygame.K_RIGHT:
                x_cord_change = 10
                y_cord_change = 0
            elif event.key == pygame.K_UP:
                x_cord_change = 0
                y_cord_change = -10
            elif event.key == pygame.K_DOWN:
                x_cord_change = 0
                y_cord_change = 10
    return game_finished, x_cord_change, y_cord_change
clock = pygame.time.Clock()
# Loop to keep playing game while it has not ended and keep track of events
while not game_finished:
    game_finished, x_cord_change, y_cord_change = execute_events(game_finished, x_cord_change, y_cord_change)
    current_position[0] += x_cord_change
    current_position[1] += y_cord_change
    game_interface.fill(background_colour)
    pygame.draw.rect(game_interface, snake_colour, current_position)
    pygame.display.update()
    clock.tick(10)
# End game once while loop has been exited
pygame.quit()
quit()

