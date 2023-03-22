import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ping Pong')

# Set up the game clock
clock = pygame.time.Clock()

# Set up the game objects
BALL_SIZE = 20
ball = pygame.Rect(SCREEN_WIDTH/2-BALL_SIZE/2, SCREEN_HEIGHT/2-BALL_SIZE/2, BALL_SIZE, BALL_SIZE)
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 60
player_paddle = pygame.Rect(50, SCREEN_HEIGHT/2-PADDLE_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)
computer_paddle = pygame.Rect(SCREEN_WIDTH-50-PADDLE_WIDTH, SCREEN_HEIGHT/2-PADDLE_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)
PADDLE_SPEED = 5

# Set up the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_paddle.move_ip(0, -PADDLE_SPEED)
    if keys[pygame.K_DOWN]:
        player_paddle.move_ip(0, PADDLE_SPEED)

    # Move the ball
    ball.move_ip(ball_speed_x, ball_speed_y)

    # Check for collisions with walls
    if ball.left < 0:
        ball_speed_x = -ball_speed_x
    if ball.right > SCREEN_WIDTH:
        ball_speed_x = -ball_speed_x
    if ball.top < 0 or ball.bottom > SCREEN_HEIGHT:
        ball_speed_y = -ball_speed_y

    # Check for collisions with paddles
    if ball.colliderect(player_paddle) or ball.colliderect(computer_paddle):
        ball_speed_x = -ball_speed_x

    # Draw the game objects
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), player_paddle)
    pygame.draw.rect(screen, (255, 255, 255), computer_paddle)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    pygame.draw.aaline(screen, (255, 255, 255), (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))

    # Update the display
    pygame.display.update()

    # Wait for the next frame
    clock.tick(60)


