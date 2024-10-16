import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
light_blue = (173, 216, 230)
dark_green = (34, 139, 34)
purple = (138, 43, 226)

# Game window size
width = 600
height = 400

# Create game window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Attractive Snake Game')

# Snake settings
snake_block = 10
snake_speed = 15

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display score
def display_score(score):
    value = score_font.render(f"Your Score: {score}", True, purple)
    screen.blit(value, [0, 0])

# Snake drawing function (with new colorful snake body)
def draw_snake(snake_block, snake_list):
    for i, x in enumerate(snake_list):
        # Alternate colors between dark green and light blue for each snake segment
        color = dark_green if i % 2 == 0 else light_blue
        pygame.draw.rect(screen, color, [x[0], x[1], snake_block, snake_block])

# Gradient background function (improved look)
def draw_gradient_background():
    for y in range(0, height, 2):
        color_value = 255 - (y // 2)
        pygame.draw.line(screen, (0, color_value, 255), (0, y), (width, y))

# Message display function
def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

# Game loop
def gameLoop():
    game_over = False
    game_close = False

    # Starting position of the snake
    x1 = width / 2
    y1 = height / 2

    # Change in position (initially 0)
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_list = []
    snake_length = 1

    # Food position
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    clock = pygame.time.Clock()

    # Main game loop
    while not game_over:

        while game_close:
            # Game Over screen with a smoother look
            screen.fill(black)
            display_message("Game Over! Press Q-Quit or C-Play Again", red)
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Handling key events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Snake movement and boundary conditions
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change

        # Draw gradient background
        draw_gradient_background()

        # Draw food (with a new color)
        pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])

        # Snake growing logic
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Snake collision with itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        display_score(snake_length - 1)

        pygame.display.update()

        # Check if snake eats the food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
