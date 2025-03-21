import pygame
import random
import math

# Initialize pygame
pygame.init()

# Create screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load("player.png")
player_x = 370
player_y = 480
player_x_change = 0

# Enemy
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
enemy_count = 3

for i in range(enemy_count):
    enemy_img.append(pygame.image.load("enemy.png"))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(0.45)  # Changed from 0.9 to 0.45
    enemy_y_change.append(20)

# Bullet
bullet_img = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 480
bullet_y_change = 10
bullet_state = (
    "ready"  # "ready" means bullet is not visible, "fire" means bullet is moving
)

# Score
score = 0
font = pygame.font.Font(None, 36)
text_x = 10
text_y = 10

# Game Over
game_over_font = pygame.font.Font(None, 72)
game_over = False

# Add these new variables after the game_over declarations
restart_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
restart_button_color = (0, 255, 0)
restart_button_hover_color = (0, 200, 0)


def show_game_over():
    game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(game_over_text, (WIDTH // 2 - 160, HEIGHT // 2 - 36))

    # Draw restart button
    mouse_pos = pygame.mouse.get_pos()
    button_color = (
        restart_button_hover_color
        if restart_button_rect.collidepoint(mouse_pos)
        else restart_button_color
    )

    pygame.draw.rect(screen, button_color, restart_button_rect)
    restart_text = font.render("Restart Game", True, (0, 0, 0))
    text_rect = restart_text.get_rect(center=restart_button_rect.center)
    screen.blit(restart_text, text_rect)


def reset_game():
    global score, game_over, player_x, bullet_state, bullet_y

    score = 0
    game_over = False
    player_x = 370
    bullet_state = "ready"
    bullet_y = 480

    # Reset enemies
    for i in range(enemy_count):
        enemy_x[i] = random.randint(0, 736)
        enemy_y[i] = random.randint(50, 150)
        enemy_x_change[i] = 0.45


def show_score(x, y):
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (x, y))


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(
        math.pow(enemy_x - bullet_x, 2) + math.pow(enemy_y - bullet_y, 2)
    )
    return distance < 27


# Game loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over:  # Only handle game controls if not game over
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change = -5
                if event.key == pygame.K_RIGHT:
                    player_x_change = 5
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bullet_x = player_x
                        fire_bullet(bullet_x, bullet_y)

            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    player_x_change = 0

        # Handle restart button click
        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            if restart_button_rect.collidepoint(event.pos):
                reset_game()

    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    for i in range(enemy_count):
        # Game Over condition
        if enemy_y[i] > 440:  # Check if enemy is close to player
            for j in range(enemy_count):
                enemy_y[j] = 2000  # Move all enemies off screen
            game_over = True
            break

        enemy_x[i] += enemy_x_change[i]

        if enemy_x[i] <= 0:
            enemy_x_change[i] = 0.45
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 736:
            enemy_x_change[i] = -0.45
            enemy_y[i] += enemy_y_change[i]

        if is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y):
            bullet_y = 480
            bullet_state = "ready"
            score += 1
            enemy_x[i] = random.randint(0, 736)
            enemy_y[i] = random.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i], i)

    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"

    player(player_x, player_y)
    show_score(text_x, text_y)
    if game_over:
        show_game_over()
    pygame.display.update()

pygame.quit()
