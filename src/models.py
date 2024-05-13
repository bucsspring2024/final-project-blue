import pygame
from src.utility import RED, GREEN, GREY, WHITE, WIDTH

class Brick:
    def __init__(self, x, y, width, height, color, health):
        """Creates brick object
        args: x(int): x position of brick
        y(int): y position of brick
        width(int): width of brick
        height (int): height of brick
        color(tuple): brick color
        health (int): brick health
        no return
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.health = health

    def draw(self, screen): 
        """
        Draws brick on screen
        args: screen (pygame.Surface): surface to be drawn on
        no return
        """
        pygame. draw.rect(screen, self.color, self.rect)

    def hit(self):
        """Reduces brick health when hit by a ball
        args: none"""
        self.health -= 1

class Paddle:
    def __init__(self, x, y, width, height, speed, color):
        """
        Initialize the paddle (Paddle) for the game.
        args:
            x (int): Initial x-coordinate of the Paddle.
            y (int): Initial y-coordinate of the Paddle.
            width (int): Width of the Paddle.
            height (int): Height of the Paddle.
            speed (int): Movement speed of the Paddle.
            color (tuple): RGB color tuple for the Paddle.
        return:
            None
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        """
        Draw the Paddle on the screen.
        args:
            screen (pygame.Surface): The display surface.
        return:
            None
        """
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, direction):
        """
        Move the Paddle left or right within the game window.
        args:
            direction (int): Direction of movement (-1 for left, 1 for right).
        return:
            None
        """
        self.x += direction * self.speed
        
        self.x = max(0, min(WIDTH - self.width, self.x)) #Keep Paddle in screen
        self.rect.x = self.x

class Ball:
    def __init__(self, x, y, radius, color, speed):
        """
        Initialize Ball
        args: x (int): Ball's x-position
        y (int): ball's y-position
        raidus (int): The radius of the ball
        speed (int): Ball speed
        no return"""
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.color = color
        self.dx = speed
        self.dy = -speed

    def draw (self, screen):
        """
        Draws ball on screen
        args: screen (pygame.Surface): Surface to draw on
        no return"""
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self, screen, paddle):
        """
        Update ball position based on speed
        args: screen (pygame.Surface): Surface to draw on
        paddle (Paddle): analyze collisions with paddle
        """
        self.x += self.dx
        self.y += self.dy

        if self.x - self.radius <= 0 or self.x + self.radius >= screen.get_width():
            self.dx *= -1
        if self.y - self.radius <= 0:
            self.dy *= -1

        if self.y + self.radius >= paddle.y and self.x > paddle.x and self.x < paddle.x + paddle.width:
            if self.y + self.radius <= paddle.y + paddle.height:
                self.dy *= -1

        if self.y + self.radius >= screen.get_height():
            self.dy *= -abs(self.dy)
    
    def check_collision(self, brick):
        """checks and handles collisions with a brick
        arg: brick (Brick): calls brick to check collision against
        return: bool: True if collision occurs, False otherwise
        """
        ball_rect = pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)
        if ball_rect.colliderect(brick.rect):
            self.dy *= -1
            brick.hit()
            return True
        return False
    
