import cv2
import numpy as np
import Console
from PIL import Image, ImageDraw

class Trigrams:

    def __init__(self,figures):
        self.img = None
        self.type = None
        self.dim = {
            'trigrams':{
                'w': 612,
                'h': 375
            },
            'hexagrams':{
                'w': 612,
                'h': 825
            }
        }
        self.folders = {
            '3':'trigrams',
            '6':'hexagrams'
        }
        self.create(figures.trigrams)
        self.create(figures.hexagrams)
    
    def setup(self):
        self.xpos = 0
        self.ypos = 37.5
        self.img = Image.new('RGB',
                            (self.dim[self.type]['w'],self.dim[self.type]['h']),
                            (255,255,255,255))
        
    def create(self,set):
        def lines(slice):
            self.xpos = 0
            draw = ImageDraw.Draw(self.img)
            for c in slice[0]:
                if c == 'A':
                    draw.line((self.xpos,self.ypos,
                               self.xpos+self.dim[self.type]['w']/3,self.ypos),
                              fill=0,
                              width=75)
                self.xpos += self.dim[self.type]['w']/3
            self.ypos += 150
        count = 0
        display = Console.Progress(len(set))
        for g in set:
            self.type = self.folders[str(len(g))]
            self.setup()
            for elem in g:
                lines(elem)
            self.img.save('img/'+self.type+'/'+str(count).rjust(5,'0')+'.png')
            count += 1
            display.update(count,self.type)
            
class Polars:

    def __init__(self,figures):
        self.dim = 825
        self.img = None
        self.create(figures.trigrams)
    
    def setup(self):
        self.angle = 0
        self.radius = 10
        self.offset = self.radius
        self.img = np.zeros((self.dim,self.dim,3),np.uint8)
        self.img[:] = (255,255,255)
    
    def create(self,set):
        def arc(slice):
            xpos = int(self.dim/2)
            ypos = xpos
            angle = 120
            print slice[0]
            for c in slice[0]:
                if c == 'A':
                    cv2.ellipse(self.img,
                                (xpos,ypos),
                                (self.radius,self.radius),
                                0,
                                angle-120,
                                angle,
                                (0,0,0),
                                thickness=2,
                                lineType=cv2.LINE_AA)
                print angle
                angle += 120
            cv2.imwrite('img/polar/test.png',self.img)
        self.setup()
        for g in set:
            print g
            for elem in g:
                arc(elem)
            self.radius += 10