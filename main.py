import pygame
from src.game import Game

def main():
    pygame.init()
    game = Game()
    game.run()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
