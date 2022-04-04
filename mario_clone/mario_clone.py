import pygame

pygame.init()
display_width = 800
display_height = 600
display_resolution = (display_width, display_height)
game_display = pygame.display.set_mode(display_resolution)
ground_color = (155, 118, 83)
screen_color = (0, 0, 0)
mountain_color = (21, 86, 130)
player_color = (0, 255, 0)
player_speed = 10
clock = pygame.time.Clock()
pygame.display.set_caption("Mario Clone")
font_style = pygame.font.SysFont(None, 10)

def gameLoop():
    game_close = False
    game_over = False
    player_x = 1
    player_y = 330
    player_size = 20
    new_x = 0
    new_y = 0
    while not game_close:
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameLoop()
                    if event.key == pygame.K_ESCAPE:
                        game_close = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    new_x = player_size
                    new_y = 0
                elif event.key == pygame.K_LEFT:
                    new_x = -player_size
                    new_y = 0
                elif event.key == pygame.K_UP:
                    new_x = 0
                    new_y = -player_size
                elif event.key == pygame.K_DOWN:
                    new_x = 0
                    new_y = player_size

                if event.key == pygame.K_SPACE:
                    new_x = 0
                    new_y = 0

        if player_x >= display_width or player_x < 0 or player_y >= display_height or player_y < 0:
            game_over = True

        player_x += new_x
        player_y += new_y

        game_display.fill(screen_color)
        pygame.draw.rect(game_display, ground_color, [0, 350, 800, 250]) #Ground Block
        pygame.draw.rect(game_display, player_color, [player_x, player_y, player_size, player_size]) #Player Block
        
        pygame.display.update()
        clock.tick(player_speed)
    pygame.quit()
    quit()
gameLoop()