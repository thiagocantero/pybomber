'''
Created on 19/06/2009

@author: Vitor
'''
import pygame
class Bomba(object):
    '''
    classdocs
    '''


    
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bomb1.gif")
        self.pos = pos
        self.passo = 1
        
    def animar(self):
        if self.passo == 1:
            self.image = pygame.image.load("images/bomb2.gif")
            self.passo = 2
        elif self.passo == 2:
            self.image = pygame.image.load("images/bomb3.gif")
            self.passo = 3
        elif self.passo == 3:
            self.image = pygame.image.load("images/bomb1.gif")
            self.passo = 1
    def explodir(self):
        pass
            
        
        