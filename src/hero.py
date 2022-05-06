import pygame
import random
#model
class Hero(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
      """
      This function creates the hero image object that will be shown on the screen during gameplay.

      Parameter:
        self: This parameter represents the current object of the class
        name: This parameter is for the name of the hero object
        x: This parameter is the x-coordinate of the top left corner of the hero object
        y: This parameter is the y-coordinate of the top left corner of the hero object
        img_file: This parameter is the link to the actual image to be used for the hero object

      Returns:
        Returns the hero image in the (x,y) coordinates on the screen.
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
        self.name = name
        self.speed = 3
        self.health = 3

    #methods to make moving our hero easier
    def move_up(self):
        self.rect.y -= self.speed
    def move_down(self):
        self.rect.y += self.speed
    def move_left(self):
        self.rect.x -= self.speed
    def move_right(self):
        self.rect.x += self.speed

    def fight(self, opponent):
      """
      This function simulates the fight between the enemies and the hero

      Parameters:
        self: This parameter represents the current object of the class
        opponent: This parameter represents the enemy objects the hero is fighting

      Returns:
        A message depending on whether or not the enemy inflicts a hit on the hero
      """
        if(random.randrange(3)):
            self.health -= 1
            print("attack failed. Remaining Health: ", self.health)
            return False
        else:
            print("successful attack")
        return True
