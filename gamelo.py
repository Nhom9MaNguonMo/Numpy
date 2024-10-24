import pygame
import random
import math
import sys

# Khởi tạo Pygame
pygame.init()

# Thiết lập kích thước cửa sổ
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Bắn Chim")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Tốc độ chim
BIRD_SPEED = 5

# Tải hình ảnh con chim thường
bird_image = pygame.image.load("thuchanh/bird2.png")
bird_image = pygame.transform.scale(bird_image, (50, 50))

# Tải hình ảnh con chim đặc biệt
special_bird_image = pygame.image.load("thuchanh/chim2.png")  # Hình ảnh chim đặc biệt
special_bird_image = pygame.transform.scale(special_bird_image, (75, 75))

# Tải hình nền
background_image = pygame.image.load("thuchanh/bg1.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Tải hình ảnh tâm ngắm
crosshair_image = pygame.image.load("thuchanh/sung.png")
crosshair_image = pygame.transform.scale(crosshair_image, (32, 32))

# Khởi tạo đồng hồ
clock = pygame.time.Clock()

# Lớp Chim
class Bird:
    def __init__(self, speed):
        self.size = 50
        self.alive = True
        self.hit = False
        self.speed = speed
        self.spawn_randomly()

    def spawn_randomly(self):
        self.side = random.choice(['left', 'right', 'top', 'bottom'])
        if self.side == 'left':
            self.x = -self.size
            self.y = random.randint(0, HEIGHT)
        elif self.side == 'right':
            self.x = WIDTH + self.size
            self.y = random.randint(0, HEIGHT)
        elif self.side == 'top':
            self.x = random.randint(0, WIDTH)
            self.y = -self.size
        elif self.side == 'bottom':
            self.x = random.randint(0, WIDTH)
            self.y = HEIGHT + self.size

        angle = random.uniform(0, 2 * math.pi)
        self.dx = self.speed * math.cos(angle)
        self.dy = self.speed * math.sin(angle)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        
        if (self.x < -self.size or self.x > WIDTH + self.size or 
            self.y < -self.size or self.y > HEIGHT + self.size):
            self.alive = False

    def draw(self, screen):
        if self.alive:
            screen.blit(bird_image, (int(self.x), int(self.y)))

# Lớp Chim Đặc Biệt
class SpecialBird(Bird):
    def draw(self, screen):
        if self.alive:
            screen.blit(special_bird_image, (int(self.x), int(self.y)))

# Hàm vẽ văn bản ở giữa nút
def draw_text_centered(text, font, color, rect):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

# Hàm hiển thị menu
def show_menu():
    menu_running = True
    font_large = pygame.font.SysFont('Times', 74)
    font_small = pygame.font.SysFont('Times', 48)
    
    while menu_running:
        screen.fill(WHITE)
        
        title_text = font_large.render("Game Bắn Chim", True, BLACK)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))
        
        start_button = pygame.Rect(WIDTH // 2 - 100, 250, 200, 50)
        pygame.draw.rect(screen, GRAY, start_button)
        draw_text_centered("Bắt đầu", font_small, BLACK, start_button)

        quit_button = pygame.Rect(WIDTH // 2 - 100, 350, 200, 50)
        pygame.draw.rect(screen, GRAY, quit_button)
        draw_text_centered("Thoát", font_small, BLACK, quit_button)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.collidepoint(mouse_pos):
                    menu_running = False
                if quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(30)

# Hàm hiển thị menu dừng
def show_pause_menu():
    pause_running = True
    font_large = pygame.font.SysFont('Times', 74)
    font_small = pygame.font.SysFont('Times', 48)

    pygame.mouse.set_visible(True)

    while pause_running:
        screen.fill(WHITE)

        pause_text = font_large.render("PAUSE", True, BLACK)
        screen.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, 100))

        resume_button = pygame.Rect(WIDTH // 2 - 100, 250, 200, 50)
        pygame.draw.rect(screen, GRAY, resume_button)
        draw_text_centered("Tiếp tục", font_small, BLACK, resume_button)

        replay_button = pygame.Rect(WIDTH // 2 - 100, 350, 200, 50)
        pygame.draw.rect(screen, GRAY, replay_button)
        draw_text_centered("Chơi lại", font_small, BLACK, replay_button)

        quit_button = pygame.Rect(WIDTH // 2 - 100, 450, 200, 50)
        pygame.draw.rect(screen, GRAY, quit_button)
        draw_text_centered("Thoát", font_small, BLACK, quit_button)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if resume_button.collidepoint(mouse_pos):
                    pause_running = False
                if replay_button.collidepoint(mouse_pos):
                    return True
                if quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(30)

    return False

# Hàm hiển thị Game Over
def show_game_over(score):
    over_running = True
    font_large = pygame.font.SysFont('Times', 74)
    font_small = pygame.font.SysFont('Times', 48)

    pygame.mouse.set_visible(True)  # Hiện chuột

    while over_running:
        screen.fill(WHITE)

        game_over_text = font_large.render("GAME OVER", True, BLACK)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, 100))

        score_text = font_small.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 200))

        replay_button = pygame.Rect(WIDTH // 2 - 100, 300, 200, 50)
        pygame.draw.rect(screen, GRAY, replay_button)
        draw_text_centered("Chơi lại", font_small, BLACK, replay_button)

        quit_button = pygame.Rect(WIDTH // 2 - 100, 400, 200, 50)
        pygame.draw.rect(screen, GRAY, quit_button)
        draw_text_centered("Thoát", font_small, BLACK, quit_button)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if replay_button.collidepoint(mouse_pos):
                    over_running = False
                if quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(30)

# Hàm khởi động lại trò chơi
def reset_game():
    return [], 0, 1  # Trả về danh sách chim rỗng, điểm số 0 và cấp độ 1

# Game loop
def main():
    birds = []
    score = 0
    level = 1
    running = True

    # Thời gian trò chơi (ví dụ: 60 giây)
    total_time = 60
    start_time = pygame.time.get_ticks()

    pygame.mouse.set_visible(False)

    while running:
        screen.blit(background_image, (0, 0))

        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        remaining_time = total_time - elapsed_time

        if remaining_time <= 0:
            show_game_over(score)  # Hiển thị Game Over
            birds, score, level = reset_game()  # Đặt lại trò chơi
            start_time = pygame.time.get_ticks()  # Đặt lại thời gian

        # Tăng cấp độ
        if score >= 50 * level:
            level += 1

        speed = BIRD_SPEED + (level - 1)  # Tăng tốc độ chim theo cấp độ

        if random.randint(1, 5) == 1:
            if random.randint(1, 10) <= 3:  # 30% khả năng tạo chim đặc biệt
                birds.append(SpecialBird(speed))
            else:
                birds.append(Bird(speed))

        for bird in birds[:]:
            if bird.alive:
                bird.move()
                bird.draw(screen)
            else:
                if bird.hit:
                    score += 6 if isinstance(bird, SpecialBird) else 4  # Cộng điểm cho chim
                birds.remove(bird)

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        time_text = font.render(f"Time: {remaining_time}", True, BLACK)
        screen.blit(time_text, (WIDTH - 110, 10))

        pause_button = pygame.Rect(WIDTH - 110, 40, 100, 50)
        pygame.draw.rect(screen, GRAY, pause_button)
        draw_text_centered("Pause", font, BLACK, pause_button)

        paused = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if pause_button.collidepoint(mouse_pos):
                    paused = True

            if not paused and event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for bird in birds:
                    if bird.alive and (bird.x < mouse_pos[0] < bird.x + bird.size) and (bird.y < mouse_pos[1] < bird.y + bird.size):
                        bird.alive = False
                        bird.hit = True

        if paused:
            play_again = show_pause_menu()
            if play_again:
                birds, score, level = reset_game()
                start_time = pygame.time.get_ticks()  # Đặt lại thời gian
            else:
                pygame.mouse.set_visible(False)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.blit(crosshair_image, (mouse_x - crosshair_image.get_width() // 2, mouse_y - crosshair_image.get_height() // 2))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    show_menu()
    main()
