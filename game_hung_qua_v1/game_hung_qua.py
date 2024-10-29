import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Tải hình ảnh nền
background_image = pygame.image.load('bg2.jpg')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Tải hình ảnh của quả bóng
ball_image = pygame.image.load('ball_image.png')
ball_image = pygame.transform.scale(ball_image, (40, 50))  # Thay đổi kích thước nếu cần

# Tải hình ảnh của giỏ
basket_image = pygame.image.load('basket_image.png')
basket_image = pygame.transform.scale(basket_image, (100, 50))  # Thay đổi kích thước nếu cần

# Thông tin giỏ
basket_x = (WIDTH - 100) // 2  # 100 là chiều rộng của hình ảnh giỏ
basket_y = HEIGHT - 60  # 20 là chiều cao của hình ảnh giỏ

# Thông tin quả bóng
ball_x = random.randint(0, WIDTH - 30)  # 30 là kích thước của hình ảnh bóng
ball_y = 0
ball_speed = 10

# Điểm số
score = 0
missed_balls = 0  # Biến đếm số quả không đỡ được

# Trạng thái trò chơi
paused = False
game_over = False

# Hàm để reset trò chơi
def reset_game():
    global score, missed_balls, ball_x, ball_y, paused, game_over
    score = 0
    missed_balls = 0
    ball_x = random.randint(0, WIDTH - 30)
    ball_y = 0
    paused = False
    game_over = False

# Vòng lặp trò chơi
running = True
reset_game()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
            if event.key == pygame.K_r:
                reset_game()

    # Điều khiển giỏ
    keys = pygame.key.get_pressed()
    if not paused and not game_over:
        if keys[pygame.K_LEFT] and basket_x > 0:
            basket_x -= 10  # Tốc độ di chuyển giỏ
        if keys[pygame.K_RIGHT] and basket_x < WIDTH - 100:  # 100 là chiều rộng giỏ
            basket_x += 10

        # Cập nhật vị trí quả bóng
        ball_y += ball_speed
        if ball_y > HEIGHT:
            ball_x = random.randint(0, WIDTH - 30)
            ball_y = random.randint(-100, -30)
            missed_balls += 1  # Tăng số quả không đỡ được

        # Kiểm tra va chạm
        if (basket_y < ball_y + 30 and  # 30 là chiều cao hình ảnh bóng
            basket_x < ball_x + 30 and  # 30 là chiều rộng hình ảnh bóng
            basket_x + 100 > ball_x):  # 100 là chiều rộng giỏ
            score += 1
            ball_x = random.randint(0, WIDTH - 30)
            ball_y = random.randint(-100, -30)

    # Kiểm tra điều kiện kết thúc trò chơi
    if missed_balls > 10:
        game_over = True  # Đánh dấu trò chơi kết thúc

    # Vẽ nền
    screen.blit(background_image, (0, 0))

    # Vẽ hình ảnh giỏ
    screen.blit(basket_image, (basket_x, basket_y))

    # Vẽ hình ảnh bóng
    screen.blit(ball_image, (ball_x, ball_y))

    # Hiển thị điểm số và số quả không đỡ được
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f'Score: {score}', True, BLACK)
    missed_text = font.render(f'Missed: {missed_balls}', True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(missed_text, (10, 40))

    # Hiển thị nút pause, restart hoặc game over
    if paused:
        pause_text = font.render('Paused - Press R to restart', True, BLACK)
        screen.blit(pause_text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
    elif game_over:
        game_over_text = font.render('Game Over! Press R to Restart', True, BLACK)
        screen.blit(game_over_text, (WIDTH // 2 - 200, HEIGHT // 2 - 50))
    else:
        pause_text = font.render('Press P to pause', True, BLACK)
        screen.blit(pause_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
