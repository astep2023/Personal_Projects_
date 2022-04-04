import pygame
import random

pygame.init()
display_width = 500
display_height = 400
display_resolution = (display_width, display_height)
game_display = pygame.display.set_mode(display_resolution)
snake_color = (60, 27, 179)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
snake_size = 10
snake_speed = 20
num_range = [i for i in range(display_width)]
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("comicsansms", 35)
pygame.display.set_caption("Snake Game")

def our_snake(snake_size, snake):
    for i in snake:
        pygame.draw.rect(game_display, snake_color, [i[0], i[1], snake_size, snake_size])

def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, snake_color)
    game_display.blit(value, [0,0])

def message(msg, color):
    msg = font_style.render(msg, True, color)
    game_display.blit(msg, [20, 20])

def gameLoop():
    game_over = False
    game_close = False
    new_x = 0
    new_y = 0
    x1 = display_width // 2
    y1 = display_height // 2
    snake = []
    snake_length = 1
    foodx = round(random.randrange(0, display_width - snake_size) / 10) * 10
    foody = round(random.randrange(0, display_height - snake_size) / 10) * 10

    while not game_close:
        while game_over == True:
            game_display.fill((0, 0, 0))
            message("You Lost! Press Escape-Quit or Q-Play Again", red)
            your_score(snake_length - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameLoop()
                    if event.key == pygame.K_ESCAPE:
                        game_close = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    new_x = -snake_size
                    new_y = 0
                elif event.key == pygame.K_RIGHT:
                    new_x = snake_size
                    new_y = 0
                elif event.key == pygame.K_UP:
                    new_x = 0
                    new_y = -snake_size
                elif event.key == pygame.K_DOWN:
                    new_x = 0
                    new_y = snake_size

                if event.key == pygame.K_ESCAPE:
                    game_close = True
            
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_over = True
        
        x1 += new_x
        y1 += new_y
        game_display.fill((0, 0, 0))
        pygame.draw.rect(game_display, blue, [foodx, foody, snake_size, snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake.append(snake_head)

        if len(snake) > snake_length:
            del snake[0]

        for x in snake[:-1]:
            if x == snake_head:
                game_over = True
        
        our_snake(snake_size, snake)
        your_score(snake_length - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_size) / 10) * 10
            foody = round(random.randrange(0, display_height - snake_size) / 10) * 10
            snake_length += 1
        
        clock.tick(snake_speed)
    pygame.quit()
    quit()
gameLoop()