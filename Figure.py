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
        self.angle = 90
        self.radius = 37.5
        self.xpos = self.dim/2
        self.ypos = self.xpos-self.radius
        self.img = Image.new('RGB',
                             (self.dim,self.dim),
                             (255,255,255,255))
    
    def create(self,set):
        def arc(slice):
            draw = ImageDraw.Draw(self.img)
            draw.ellipse([(self.xpos,self.ypos),
                          (-1*self.xpos,-1*self.ypos)],
                          fill=0,
                          outline=0)
            for c in slice[0]:
                if c == 'A':
                    draw.arc([(self.xpos,self.ypos),
                              (self.xpos+self.radius,self.ypos+self.radius)],
                              self.angle,
                              self.angle+90,
                              fill=0)
                self.xpos += self.radius
                self.ypos += self.radius
            self.angle -= 90
            self.radius += self.radius/3
        for g in set:
            self.setup()
            for elem in g:
                arc(elem)
        self.img.save('img/polar/test.png')