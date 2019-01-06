'''
Created on 7 juil. 2018

@author: Fab
'''
import pygame
from .resources import Resources, Event

    
class Gui:
    
    def __init__(self):
        pygame.init()
        self.res = Resources()
        self.gameDisplay = pygame.display.set_mode((Resources.display_width,Resources.display_height))
        pygame.display.set_caption(Resources.caption)
        self.clock = pygame.time.Clock()
        self.direction = Event.KEY_RIGHT
        self.font = pygame.font.SysFont(None, 25)

    def text_objects(self,text,color):
        textSurface = self.font.render(text, True, color)
        return textSurface, textSurface.get_rect()
        
    def message_to_screen(self,msg,color, y_displace=0):
        textSurf, textRect = self.text_objects(msg,color)
        textRect.center = (Resources.display_width / 2), (Resources.display_height / 2)+y_displace
        self.gameDisplay.blit(textSurf, textRect)
    
#     def keys_processing(self, last_direction):
#         direction = last_direction
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     direction = Resources.dir_left
#                 elif event.key == pygame.K_RIGHT:
#                     direction = Resources.dir_right
#                 elif event.key == pygame.K_UP:
#                     direction = Resources.dir_up
#                 elif event.key == pygame.K_DOWN:
#                     direction = Resources.dir_down
#         return direction

    def game_over_screen (self):
        self.gameDisplay.fill(Resources.white)
        self.message_to_screen("Game over", Resources.red, y_displace=-50)
        self.message_to_screen("Press C to play again or Q to quit",Resources.black, 50)
        pygame.display.update()
                        
    def update(self, snake, apple):
        self.gameDisplay.fill(Resources.white)
        apple.draw(self.gameDisplay)
        snake.draw(self.gameDisplay)
        pygame.display.update()
    
    def quit(self):
        pygame.quit()
