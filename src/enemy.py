import pygame
import random
#model
class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
      """
      This function creates the enemy image object that will be shown on the screen during gameplay.

      Parameter:
        self: This parameter represents the current object of the class
        name: This parameter is for the name of the enemy object
        x: This parameter is the x-coordinate of the top left corner of the enemy object
        y: This parameter is the y-coordinate of the top left corner of the enemy object
        img_file: This parameter is the link to the actual image to be used for the enemy object

      Returns:
        Returns the enemy image in the (x,y) coordinates on the screen.
      """
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name + str(id(self))
        self.speed = 2

    def update(self):
      """
      This function randomizes the movement of the enemys that are attacking the hero

      Parameters:
        self: This parameter represents the current object of the class

      Returns:
        Random x and y coordinates for the enemy's movements during gameplay
      """
      new_x = random.randrange(-1,1)
      new_y = random.randrange(-1,1)
      self.rect.x += new_x
      self.rect.y += new_y
        #print("'Update me,' says " + self.name)
