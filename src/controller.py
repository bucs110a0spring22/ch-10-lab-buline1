import sys
import pygame
import random
from src import hero
from src import enemy


class Controller:
    def __init__(self, width=640, height=480):
      """This function adds value to object properties. In this case the object is the screen
      
      Parameters:
        self: This parameter represents the current object of the class
        width: This parameter is for the screen width value
        height: This parameter is for the screen width value
      
      Returns:
        This function returns a white screen with the dimensions 640 by 480"""
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((250, 250, 250))  # set the background to white
        pygame.font.init()  # you have to call this at the start, if you want to use this module.
        pygame.key.set_repeat(1, 50)  # initialize a held keey to act as repeated key strikes
        """Load the sprites that we need"""

        self.enemies = pygame.sprite.Group()
        num_enemies = 3
        for i in range(num_enemies):
            x = random.randrange(100, 400)
            y = random.randrange(100, 400)
            self.enemies.add(enemy.Enemy("Boogie", x, y, 'assets/enemy.png'))
        self.hero = hero.Hero("Conan", 50, 80, "assets/hero.png")
        self.all_sprites = pygame.sprite.Group((self.hero,) + tuple(self.enemies))
        self.state = "GAME"

    def mainLoop(self):
      """
      This function runs the gameLoop when true but starts the gameOver function when false
      
      Parameters:
        self: This parameter represents the current object of the class/function
      
      Returns:
        Either the game itself or the game over screen depending on whether it is true or not
      """
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()

    def gameLoop(self):
      """
      This function is the game itself. This function runs the actual game that is created and calls on the enemy and hero classes to do so.

      Parameters:
        self: This parameter represents the current object of the class

      Returns:
        The game between the hero fighting the moving enemies.
      """
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        self.hero.move_up()
                    elif(event.key == pygame.K_DOWN):
                        self.hero.move_down()
                    elif(event.key == pygame.K_LEFT):
                        self.hero.move_left()
                    elif(event.key == pygame.K_RIGHT):
                        self.hero.move_right()

            # check for collisions
            fights = pygame.sprite.spritecollide(self.hero, self.enemies, True)
            if(fights):
                for e in fights:
                    if(self.hero.fight(e)):
                        e.kill()
                        self.background.fill((250, 250, 250))
                    else:
                        self.background.fill((250, 0, 0))
                        self.enemies.add(e)

            # redraw the entire screen
            self.enemies.update()
            self.screen.blit(self.background, (0, 0))
            if(self.hero.health == 0):
                self.state = "GAMEOVER"
            self.all_sprites.draw(self.screen)

            # update the screen
            pygame.display.flip()

    def gameOver(self):
      """
      This function is what occurs when the game is completed. 

      Parameters:
       self: This parameter represents the current object of the class

      Returns:
        This function returns a red screen when the hero is defeated and text saying game over. Nothing occurs when the hero survives the attack.
      """
        self.hero.kill()
        myfont = pygame.font.SysFont(None, 23)
        message = myfont.render('Game Over, Would you like to play again? Press y for Yes and n for No', False, (0, 0, 0))
        self.screen.blit(message, (25, 25))
        pygame.display.flip()
        while True:
          for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
              if(event.key == pygame.K_n):
                sys.exit()
              if(event.key == pygame.K_y):
                gameLoop()
            if event.type == pygame.QUIT:
              sys.exit()
        pygame.display.flip()        
                  
    
      
