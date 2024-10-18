import pygame
import random

# Initialize Pygame
pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display settings
disp_width = 600
disp_height = 400

dis = pygame.display.set_mode((disp_width, disp_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# Snake settings
snake_block = 10
snake_speed = 25

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    """Display the current score."""
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    """Draw the snake on the display."""
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    """Display a message on the screen."""
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [disp_width / 6, disp_height / 3])

def gameLoop():
    """Main function for running the game."""
    game_over = False
    game_close = False

    x1 = disp_width / 2
    y1 = disp_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Generate initial food position
    foodx = round(random.randrange(0, disp_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, disp_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        gameLoop()  # Restart the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        # Check for wall collision
        if x1 >= disp_width or x1 < 0 or y1 >= disp_height or y1 < 0:
            game_close = True
            
        x1 += x1_change
        y1 += y1_change
        
        dis.fill(blue)  # Clear the display
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])  # Draw food

        snake_Head = [x1, y1]
        snake_List.append(snake_Head)  # Add new head position to the snake body

        if len(snake_List) > Length_of_snake:
            del snake_List[0]  # Remove the last segment of the snake

        # Check for self-collision
        if snake_Head in snake_List[:-1]:
            game_close = True

        our_snake(snake_block, snake_List)  # Draw the snake
        Your_score(Length_of_snake - 1)  # Display the score

        pygame.display.update()  # Refresh the display

        # Check for food collision
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, disp_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, disp_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1  # Increase snake length

        clock.tick(snake_speed)  # Control the speed of the game

    pygame.quit()
    quit()

# Start the game
gameLoop()
