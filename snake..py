import pygame
import time
import random

pygame.init()

# Setting up colours for the background, snake and food
background_colour = (255, 255, 191)
snake_colour = (0, 0, 255)
# Positional data
interface_width = 500
interface_height = 500
snake_speed = 50
snake_dimension = 25
game_finished = False
close_game = False
current_highscore = 0
# Setting up interface for the game using pygame built-in functions
game_interface = pygame.display.set_mode((interface_width, interface_height))
pygame.display.update()
# Setting window caption
pygame.display.set_caption('Snake Game - Tirth Thakar')
score_style = pygame.font.SysFont('arial', 20)

def display_score(score, highscore):
    your_score = score_style.render('Your score: ' + str(score), True, (1, 50 ,32))
    high_score = score_style.render('Highscore: ' + str(highscore), True, (139, 0 , 0))
    game_interface.blit(your_score, [0, 0])
    game_interface.blit(high_score, [interface_width - 180, 0])

def snake(snake_dimension, snake_list):
    for segment in snake_list:
        pygame.draw.rect(game_interface, snake_colour, [segment[0], segment[1], snake_dimension, snake_dimension])
        pygame.draw.rect(game_interface, snake_colour, [segment[0], segment[1], snake_dimension, snake_dimension])
# Function to action on event types
def movement_events(x_cord_change, y_cord_change):
    global game_finished
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_cord_change = -2
                y_cord_change = 0
            elif event.key == pygame.K_RIGHT:
                x_cord_change = 2
                y_cord_change = 0
            elif event.key == pygame.K_UP:
                x_cord_change = 0
                y_cord_change = -2
            elif event.key == pygame.K_DOWN:
                x_cord_change = 0
                y_cord_change = 2
    return x_cord_change, y_cord_change

def new_game_or_close():
    global game_finished
    global close_game
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                game_finished = True
                close_game = False
            if event.key == pygame.K_SPACE:
                play()

def hit_boundary(x_pos, y_pos):
    global close_game
    global interface_height
    global interface_width
    if x_pos >= interface_width or x_pos < 0 or y_pos >= interface_height or y_pos < 0:
        close_game = True

def ate_food(x_pos, y_pos, food_x, food_y, snake_length):
    global interface_height
    global interface_width
    global snake_dimension

    # if x_pos == food_x and y_pos == food_y:
    if snake_in_food_region(x_pos, y_pos, food_x, food_y):
        food_x = round(random.randrange(0, interface_width - snake_dimension) / 10.0) * 10.0
        food_y = round(random.randrange(0, interface_height - snake_dimension) / 10.0) * 10.0
        snake_length += 1
    return food_x, food_y, snake_length

def snake_in_food_region(x_pos, y_pos, food_x, food_y):
    if x_pos <= food_x + 15 and x_pos >= food_x - 15 and y_pos <= food_y + 15 and y_pos >= food_y - 15:
        return True
    else:
        return False

def display_message(message, colour):
    msg = pygame.font.SysFont(None, 25).render(message, True, colour)
    game_interface.blit(msg, [interface_width/10, interface_height/3])

clock = pygame.time.Clock()

def play():
    # Variable to keep track of whether or not game has ended or not
    global interface_height
    global interface_width
    global snake_dimension
    global close_game
    global game_finished
    global current_highscore

    snake_list = []
    snake_length = 1

    close_game = False
    game_finished = False

    x_cord_change = 0
    y_cord_change = 0
    current_position = [interface_width/2, interface_height/2, snake_dimension, snake_dimension]

    # Loop to keep playing game while it has not ended and keep track of events
    food_x = round(random.randrange(0, interface_width - snake_dimension) / 10.0) * 10.0
    food_y = round(random.randrange(0, interface_height - snake_dimension) / 10.0) * 10.0

    while not game_finished:

        while close_game == True:
            game_interface.fill(background_colour)
            display_message('You lost! Press Q to quit or Spacebar to play again!', (255, 0, 0))
            pygame.display.update()
            new_game_or_close()

        x_cord_change, y_cord_change = movement_events(x_cord_change, y_cord_change)
        hit_boundary(current_position[0], current_position[1])
        if not close_game and not game_finished:
            current_position[0] += x_cord_change
            current_position[1] += y_cord_change
            game_interface.fill(background_colour)
            pygame.draw.rect(game_interface, (0, 0, 0), [food_x, food_y, 10, 10])
            snake_head = []
            snake_head.append(current_position[0])
            snake_head.append(current_position[1])
            snake_list.append(snake_head)
            if len(snake_list) > snake_length:
                del snake_list[0]
            for item in snake_list[:-1]:
                if item == snake_head:
                    close_game = True
            snake(snake_dimension, snake_list)
            display_score(snake_length*10 - 10, current_highscore)
            if current_highscore <= snake_length*10 - 10:
                current_highscore = snake_length*10 - 10
            pygame.display.update()
            food_x, food_y, snake_length = ate_food(current_position[0], current_position[1], food_x, food_y, snake_length)
            clock.tick(snake_speed)

    pygame.display.update()
    time.sleep(2)
    # End game once while loop has been exited
    pygame.quit()
    quit()

play()
