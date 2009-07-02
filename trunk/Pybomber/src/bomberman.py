'''
Created on 11/06/2009

@author: Vitor
'''
import pygame   

from pygame.locals import *

class Bomberman(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bomberman11.PNG")
        self.speed = 20
        self.pos = [50,50]
        self.passo = 1
        self.rect = self.image.get_rect()
        lista_bombas = []
        
        
    def atualiza(self,time,tecla=None):
        if tecla == None:
            for bomba in lista_bombas:
                if bomba.explodiu:
                    lista_bombas.remove(bomba)
                else:
                    bomba.atualiza(time)
                    
        
        

    def soltar_bomba(self,time):
        bomba = Bomba(self.pos,time)
        lista_bombas.append(bomba)
        return bomba
       
        
        
    def acao(self,tecla):
        if tecla in ["UP", "DOWN", "LEFT", "RIGHT"]:
            self.move(tecla)
        elif tecla == "SPACE":
            self.soltar_bomba()
            
    
    def move(self,tecla):
        if tecla == "DOWN":
            if self.passo == 1:
                self.image = pygame.image.load("images/bomberman12.PNG")
                self.passo = 3
            elif self.passo == 2:
                self.image = pygame.image.load("images/bomberman10.PNG")
                self.passo = 3
            elif self.passo == 3:
                self.image = pygame.image.load("images/bomberman11.PNG")
                self.passo = 2
            self.rect.move_ip(0*self.speed,1*self.speed)
        

        elif tecla == "UP":
            if self.passo == 1:
                self.image = pygame.image.load("images/bomberman9.PNG")
                self.passo = 2
            elif self.passo == 2:
                self.image = pygame.image.load("images/bomberman7.PNG")
                self.passo = 3
            elif self.passo == 3:
                self.image = pygame.image.load("images/bomberman8.PNG")
                self.passo = 1
            self.rect.move_ip(0*self.speed,-1*self.speed)
            
        elif tecla == "LEFT":
            if self.passo == 1:
                self.image = pygame.image.load("images/bomberman4.PNG")
                self.passo = 2
            elif self.passo == 2:
                self.image = pygame.image.load("images/bomberman5.PNG")
                self.passo = 3
            elif self.passo == 3:
                self.image = pygame.image.load("images/bomberman6.PNG")
                self.passo = 1
            self.rect.move_ip(-1*self.speed,0*self.speed)
       
        elif tecla == "RIGHT":
            if self.passo == 1:
                self.image = pygame.image.load("images/bomberman1.PNG")
                self.passo = 2
            elif self.passo == 2:
                self.image = pygame.image.load("images/bomberman2.PNG")
                self.passo = 3
            elif self.passo == 3:
                self.image = pygame.image.load("images/bomberman3.PNG")
                self.passo = 1
            self.rect.move_ip(1*self.speed,0*self.speed)
        