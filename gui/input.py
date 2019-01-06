'''
Created on 7 juil. 2018

@author: Fab
'''
import pygame
from .resources import Event
    
class Input:
    
#     KEYS = {
#         'no event': Event.KEY_NONE ,
#         'up': Event.KEY_UP ,
#         'down': Event.KEY_DOWN ,
#         'left': Event.KEY_LEFT ,
#         'right': Event.KEY_RIGHT ,
#         'restart': Event.KEY_RESTART ,
#         'quit': Event.KEY_QUIT         
#         }
    
    def __init__(self, use_keyboard = True, callback = None):
        self.use_keyboard = use_keyboard
        self.callback = callback
        self.evt = None
    
    def go_up(self):
        self.evt = Event.KEY_UP
    def go_down(self):
        self.evt = Event.KEY_DOWN
    def go_left(self):
        self.evt = Event.KEY_LEFT
    def go_right(self):
        self.evt = Event.KEY_RIGHT
    def restart(self):
        self.evt = Event.KEY_RESTART
    def quit(self):
        self.evt = Event.KEY_QUIT

    
    def get_event(self):
        if self.use_keyboard :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return Event.KEY_QUIT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        return Event.KEY_LEFT
                    elif event.key == pygame.K_RIGHT:
                        return Event.KEY_RIGHT
                    elif event.key == pygame.K_UP:
                        return Event.KEY_UP
                    elif event.key == pygame.K_DOWN:
                        return Event.KEY_DOWN
                    if (event.key == pygame.K_a) or (event.key == pygame.K_q):
                        return Event.KEY_QUIT
                    if event.key == pygame.K_c: 
                        return Event.KEY_RESTART
        else:
            if self.callback :
                self.callback()
            evt = self.evt
            self.evt = None
            return evt              
