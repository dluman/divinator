from itertools import permutations
from PIL import Image, ImageDraw

class Gram:

    def __init__(self):
        self.grams = None
        
    def slice(self,s):
        return [s[i:i+3] for i in range(0,len(s),3)]
        
    def pad(self,g):
        i = g.index(min(g,key=len))
        for c in xrange(len(g[i]),3):
            g[i] = g[i] + 'B'
        return g
    
    def evaluate(self,s):
        g = self.slice(s)
        g = self.pad(g)
        return [[l] for l in g]
    
    def combine(self,g):
        self.grams = permutations(g,2)

class Draw:

    def __init__(self,g):
        self.img = None
        self.x = 612
        self.y = 750
        self.line_height = 37.5
        self.grams = g
        self.setup()
        self.create()
    
    def setup(self):
        self.img = Image.new('RGB',
                            (self.x,self.y),
                            (255,255,255,255))
        
    def create(self):
        def line(x,y,slice):
            w,h = self.img.size
            draw = ImageDraw.Draw(self.img)
            for c in slice:
                print c
        count = 0
        for g in self.grams:
            #g[0] = upper, g[1] = lower
            for c in g:
                line(x,y,c)