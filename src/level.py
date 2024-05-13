import random
from src.models import Brick
from src.utility import RED, GREEN, GREY, WIDTH, HEIGHT

def create_level():
    """
    Creates a level with randomly placed bricks (in the upper part of the screen)
    args: 
    return: list: a list of Bricks"""
    bricks = []
    cols = 10
    brick_width = WIDTH // cols
    brick_height = 20
    rows = 5
    max_bricks = int(rows * cols * 0.5)

    for _ in range (max_bricks):
        x = random.randint(0, WIDTH - brick_width)
        y = random.randint(0, HEIGHT // 4 - brick_height)
        color = (200, 0, 0)
        health = 1
        bricks.append(Brick(x, y, brick_width, brick_height, color, health))
    return bricks
