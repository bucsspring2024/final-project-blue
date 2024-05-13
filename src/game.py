import pygame
from src.utility import WIDTH, HEIGHT,font, BLACK, WHITE
from src.models import Ball, Paddle
from src.level import create_level
from src.controller import main_menu, game_over_screen

def Game(): 
    """
    Main function for running game loop
    args: quit (pygame.quit): allows user to quit game
    difficulty: 
    """
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Brick Breaker")
    clock = pygame.time.Clock()
    running = True
    font = pygame.font.Font(None, 74)

    if main_menu(screen, font) == "quit":
        pygame.quit()
        return
    
    
    bricks = create_level()
    ball = Ball(WIDTH // 2, HEIGHT - 50, 10, WHITE, 4)
    paddle = Paddle(WIDTH // 2 - 50, HEIGHT - 30, 100, 10, 10, WHITE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paddle.move(-5)
                elif event.key == pygame.K_RIGHT:
                    paddle.move(5)
                elif event.type == pygame.KEYUP:
                    if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                        paddle.move(0)

        if ball.update(screen, paddle) or not bricks:
            if not bricks:
                game_over_screen(screen, font, "You Win!")
            else:
                game_over_screen(screen, font, "Game Over")
            pygame.time.wait(2000)
            break


        screen.fill(BLACK)
        paddle.draw(screen)
        
        for brick in bricks:
                brick.draw(screen)
                if ball.check_collision(brick) and brick.health <= 0:
                    bricks.remove(brick)
        ball.draw(screen)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    Game()