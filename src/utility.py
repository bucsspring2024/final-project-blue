
import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)

WIDTH = 800
HEIGHT = 600

pygame.font.init()
font = pygame.font.Font(None, 36)

def draw_text(text, font, color, surface, x, y):
    """
    Draw text on _____. 
    args: text (str): text to draw
    font (pygame.font.Font): font of the text
    surface(pygame.Surface): describes surface to draw on
    color(tuple) RGB
    x (int): X position of text
    y (int): y coordinate of text
    """
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)
