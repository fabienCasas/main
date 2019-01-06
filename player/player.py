'''
Created on Jan 6, 2019

@author: fab
'''

from gui.engine import Engine
from gui.input import Input
from pygame import dx_version_string



class Player:
    
    NONE = 'none'
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    QUIT = 'quit'
    
    def __init__(self):     
        self.control = Input(False, self.compute)
        self.game = Engine(self.control)
        
    def play(self):
        self.last_dir = self.UP
        self.u_turn = False
        self.last_dx = 0
        self.last_dy = 0
        self.game.loop()
        
        
    def find_apple(self):   
        dx = self.game.get_snake_pos()[0].x - self.game.get_apple_pos().x
        dy = self.game.get_snake_pos()[0].y - self.game.get_apple_pos().y
        return dx,dy
        
        
    def choose_dir(self, dx, dy):
        
        if not self.u_turn :
            
            if abs(dx) >= abs(dy) :            
                if dx > 0 : # must go LEFT
                    if self.last_dir == self.RIGHT :
                        d = self.UP   
                        self.u_turn = True
                    else :
                        d = self.LEFT
                        
                elif dx < 0 : # must go RIGHT
                    if self.last_dir == self.LEFT :
                        d = self.DOWN   
                        self.u_turn = True
                    else :
                        d = self.LEFT
            else :        
                if dy > 0 : # must go UP
                    if self.last_dir == self.DOWN :
                        d = self.LEFT   
                        self.u_turn = True
                    else :
                        d = self.UP
                
                elif dy < 0 : # must go DOWN
                    if self.last_dir == self.UP :
                        d = self.RIGHT   
                        self.u_turn = True
                    else :
                        d = self.DOWN

        else:
            self.u_turn = False
            if self.last_dir == self.RIGHT:
                d = self.UP
            if self.last_dir == self.LEFT:
                d = self.DOWN
            if self.last_dir == self.UP:
                d = self.LEFT
            if self.last_dir == self.DOWN:
                d = self.RIGHT
                  
        self.last_dir = d
        self.last_dx = dx
        self.last_dy = dy
        
        if self.u_turn : 
            s = 'yes'
        else:
            s = 'no'
        print ("dx: ", dx, " dy: ", dy, "last dir : ", self.last_dir, " dir: ", d, "u-turn : ", s)    
        
        return d
        
    def compute(self):
        
        dx, dy = self.find_apple()        
        
        
        d = self.choose_dir(dx, dy)              
        
        if d == Player.UP:
                self.control.go_up()
        elif d == Player.DOWN :
                self.control.go_down()
        if d == Player.LEFT:
                self.control.go_left()
        elif d == Player.RIGHT :
                self.control.go_right()
                
        self.last_dx = dx
        self.last_dy = dy      
        
        if self.game.is_over() :
            self.control.restart()
#             self.control.quit()        
        
        
        
        


        
        

