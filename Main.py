import pygame
import PIL
from PIL import Image
from Config import* 


class Head:
    def __init__(self, pic_head, x=300, y=255):
        self.pic_head = pic_head
        self.x = x
        self.y = y
    
    def draw_items_head(self):
        sc.blit(self.pic_head, (300, 350))        

s = Head(image1, 35, 21)
s.draw_items_head()