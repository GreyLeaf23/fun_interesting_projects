import pygame

pygame.init()

# Creating window where game will be display
WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))

# Change the game name being display
pygame.display.set_caption("Pong_But_Better")


# Variable that allows control  program RUN
run = True

# Colors in RGB
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Ball creation
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius

# Paddle Creation
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH - (100 - paddle_width/2)


# Spawn ball in screen
pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius)

# Spawn paddles in screen
pygame.draw.rect(wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))

# Update game to current state
pygame.display.update()

# Main Loop
while run:
    for input in pygame.event.get():
        if input.type is pygame.QUIT:
            run = False


