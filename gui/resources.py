'''
Created on 7 juil. 2018

@author: Fab
'''

import pygame

class Resources:
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    green = (0,155,0)    
    display_width = 800
    display_height  = 600
    snake_girth = 20
    snake_color = green
    apple_size = snake_girth
    FPS = 15
    caption = 'Slither'
    
    def __init__(self):
        head_up = pygame.image.load('snakehead.png')
        head_down = pygame.transform.rotate(head_up, 180)
        head_right = pygame.transform.rotate(head_up, 270)
        head_left = pygame.transform.rotate(head_up, 90)        
        self.head = { Event.KEY_UP : head_up, 
                        Event.KEY_DOWN: head_down, 
                        Event.KEY_RIGHT: head_right, 
                        Event.KEY_LEFT: head_left }
        
    def get_bounds(self):
        return pygame.Rect(0, 0, self.display_width, self.display_height)
                
class Event:
    KEY_UP    = 10
    KEY_DOWN  = -10
    KEY_RIGHT = 20
    KEY_LEFT  = -20

    RESTART   = 254
    QUIT      = 255
