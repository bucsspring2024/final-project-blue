import pygame
from src.utility import draw_text, WHITE, WIDTH, HEIGHT

def handle_game_events(ball, bricks, paddle):
   """
   Process game events and update game
   args: ball (Ball): Establishes loss condition of ball touching bottom of screen
   return: str: Returns the game state ('quit' if game closes)
   """
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 'quit'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                return 'quit'
        if ball.y - ball.radius >= HEIGHT:
            return "game_over"
        return "running"

def game_over_screen(screen, font):
    """
    Display game over screen and handle interaction
    args: screen (pygame.Surface): display surface
    font (pygame.font.Font): the font for text rendering
    return: str: the action chosen by the player ("retry", "quit")
    """
    screen.fill((0,0,0))
    draw_text("Game Over!", font, WHITE, screen, WIDTH // 2 - 100, HEIGHT // 2 - 50)
    draw_text("press R to retry or Q to quit", font, WHITE, screen, WIDTH // 2 - 150),
    pygame.display.update()
    pygame.time.wait(3000)
    return handle_game_events(None, None)

def main_menu(screen,font):
    """
    Display the main menu, handle user choices
    args: screen (pygame.Surface): load surface
    font (pygame.font.Font): font for text
    draw_text (str): directed text to be drawn, with location and font
    return: str: "start" if game should start, "quit" if it should close
    """
    screen.fill((0,0,0))
    draw_text("Welcome to BLUE", font, WHITE, screen, WIDTH // 2 - 140, HEIGHT // 2 - 100)
    draw_text("Press S to Start", font, WHITE, screen, WIDTH // 2 - 80, HEIGHT // 2)
    draw_text("Press Q to Quit", font, WHITE, screen, WIDTH // 2 - 100, HEIGHT // 2 + 60)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    return "start"
                elif event.key == pygame.K_q:
                    return "quit"
            
