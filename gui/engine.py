'''
Created on 7 juil. 2018

@author: Fab
'''
from .snake import Snake
from .apple import Apple
from .resources import Resources
from .gui import Gui
from .input import Input, Event

class Engine:
    
    directions_list = [ Event.KEY_UP, Event.KEY_DOWN, Event.KEY_LEFT, Event.KEY_RIGHT ]
    
    
    def __init__(self, input):
        self.gui = Gui()
        if input :
            self.input = input
        else :
            self.input = Input(True)
    
    def game_init(self):
        self.do_exit = False
        self.do_restart = False
        self.game_over = False
        self.snake = Snake(self.gui.res)
        self.apple = Apple(self.gui.res)
        self.direction = None
        self.score = 0
        self.next_turn = False
        
    def user_input(self):
        key = self.input.get_event()
#         print("key = ", key)
        if key in self.directions_list :
            self.direction = key
        else :
#             print("not a direction")
            if key == Event.KEY_QUIT :
                self.do_exit = True
            elif key == Event.KEY_RESTART :
                self.do_restart = True
        
    def score(self):
        return self.score
    
    def get_snake_pos(self):
        return self.snake.get_pos()
    
    def get_apple_pos(self):
        return self.apple.get_pos()
    
    def get_bounds(self):
        return self.gui.res.get_bounds()
    
    def distance_to_goal(self):
        dx = self.apple.pos.x - self.snake.head.x
        dy = self.apple.pos.y - self.snake.head.y
        # Manhattan distance
        dist = dx + dy
        # Vector
#         dist = np.array([dx, dy])
        return dist
    
    def is_over(self):
        return self.game_over
     
    
    def turn(self):
        # eat apple ?
        if self.snake.head.in_area(self.apple.rect) : 
            self.snake.increase()
            self.apple.move()
            self.score += 1
        # move snake 
        self.user_input()
        self.game_over = False
        if self.direction :
            self.game_over = self.snake.move(self.direction)
        else:
            print("no input")
            
        if not self.game_over :         
            # re-draw
            self.gui.update(self.snake, self.apple)
        else:
            self.score -= 2
            while not self.do_exit and not self.do_restart :
                self.gui.game_over_screen()
                self.user_input()
            if self.do_restart :
                self.game_init()
        return self.game_over
        

    def loop(self):
        self.game_init()
        while not self.do_exit:
            self.turn()
            self.gui.clock.tick(Resources.FPS)
        self.gui.quit()
        

        
