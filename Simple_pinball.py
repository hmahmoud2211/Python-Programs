import pygame 
import random
import math

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pinball")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

ball_radius = 10
ball = pygame.Surface((ball_radius * 2, ball_radius * 2), pygame.SRCALPHA)
pygame.draw.circle(ball, WHITE, (ball_radius, ball_radius), ball_radius)
ball_rect = ball.get_rect(center=(screen_width // 2, screen_height // 2))
paddle = pygame.Rect(screen_width // 2 - 50, screen_height - 50, 100, 20)
bricks = []
for i in range(7):
    for j in range(5):
        brick = pygame.Rect(i * 80 + 20, j * 30 + 50, 60, 20)
        bricks.append(brick)

ball_speed_x = 2 * random.choice([-1, 1])
ball_speed_y = -2
paddle_speed = 0
score = 0
font = pygame.font.Font(None, 36)

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_speed = -5
            elif event.key == pygame.K_RIGHT:
                paddle_speed = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and paddle_speed == -5:
                paddle_speed = 0
            elif event.key == pygame.K_RIGHT and paddle_speed == 5:
                paddle_speed = 0

    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y
    paddle.x += paddle_speed
    if ball_rect.colliderect(paddle):
        ball_speed_y = -3
    for brick in bricks[:]:
        if ball_rect.colliderect(brick):
            bricks.remove(brick)
            ball_speed_y *= -1
            score += 10

    if ball_rect.y < 0:
        ball_speed_y = 3
    elif ball_rect.y > screen_height + ball_radius:
        game_over = True

    if ball_rect.x < 0 or ball_rect.x > screen_width:
        ball_speed_x *= -1
    screen.fill(BLACK)
    screen.blit(ball, ball_rect)
    pygame.draw.rect(screen, GREEN, paddle)
    for brick in bricks:
        pygame.draw.rect(screen, BLUE, brick)
    score_text = font.render("Score: " + str(score), True, RED)
    screen.blit(score_text, (10, 10))
    title_text = font.render("King-Soft", True, GREEN)
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 20))

    pygame.display.flip()
    

    pygame.time.wait(10)
if score == 350:
    message = "Congratulations! You won!"
else:
    message = "Game over"

message_text = font.render(message, True, GREEN)
message2 = "Your second message here"
message2_text = font.render(message2, True, GREEN)

screen.fill(BLACK)
screen.blit(message_text, (screen_width // 2 - message_text.get_width() // 2, screen_height // 2 - 20))
screen.blit(message2_text, (screen_width // 2 - message2_text.get_width() // 2, screen_height // 2 + 30))
pygame.display.flip()
pygame.time.delay(3000)
pygame.quit()