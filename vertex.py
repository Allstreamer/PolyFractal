import pygame

class Vertex:
    def __init__(self, x, y, draw_size, draw_color):
        self.x = x
        self.y = y
        self.draw_size = draw_size
        self.draw_color = draw_color
    
    def detect_Touch(self, mouse_pos) -> bool:
        return ((mouse_pos[0] >= self.x and mouse_pos[0] <= self.x + self.draw_size) and
        (mouse_pos[1] >= self.y and mouse_pos[1] <= self.y + self.draw_size))
    
    def draw(self, screen):
        pygame.draw.ellipse(
            screen,
            self.draw_color,
            (self.x,self.y,
             self.draw_size,self.draw_size))
        
    def get_pos(self) -> tuple:
        return (self.x, self.y)
    
    def get_center_pos(self) -> tuple:
        return (self.x + (self.draw_size/2),self.y + (self.draw_size/2))
    
    def set_pos(self, pos):
        self.x = pos[0]
        self.y = pos[1]