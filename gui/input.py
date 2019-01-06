'''
Created on 7 juil. 2018

@author: Fab
'''
import pygame
from .resources import Event
    
class Input:
    
    def __init__(self, use_keyboard):
        self.use_keyboard = use_keyboard
        self.evt = None
    
    def send_key(self, evt):
        self.evt = evt
    
    def get_event(self):
        if self.use_keyboard :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return Event.QUIT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        return Event.KEY_LEFT
                    elif event.key == pygame.K_RIGHT:
                        return Event.KEY_RIGHT
                    elif event.key == pygame.K_UP:
                        return Event.KEY_UP
                    elif event.key == pygame.K_DOWN:
                        return Event.KEY_DOWN
                    if event.key == pygame.K_a:
                        return Event.QUIT
                    if event.key == pygame.K_c: 
                        return Event.RESTART
        else:
            evt = self.evt
            self.evt = None
            return evt              
