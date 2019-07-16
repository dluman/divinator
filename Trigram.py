from itertools import permutations
from functools import reduce
from operator import add
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
        grams = permutations(g,3)
        self.grams = permutations(grams,2)

class Draw:

    def __init__(self,g):
        self.img = None
        self.dim = {
            'w':612,
            'h':825
        }
        self.grams = g
    
    def setup(self):
        self.xpos = 0
        self.ypos = 37.5
        self.img = Image.new('RGB',
                            (self.dim['w'],self.dim['h']),
                            (255,255,255,255))
        
    def create(self):
        def lines(slice):
            self.xpos = 0
            draw = ImageDraw.Draw(self.img)
            for c in slice[0]:
                if c == 'A':
                    draw.line((self.xpos,self.ypos,
                               self.xpos+self.dim['w']/3,self.ypos),
                              fill=0,
                              width=75)
                    self.xpos += self.dim['w']/3
                if c == 'B':
                    self.xpos += self.dim['w']/3
            self.ypos += 150
        count = 0
        for g in self.grams:
            self.setup()
            gram = reduce(add,
                          (g))
            print count,':',gram
            for e in gram:
                lines(e)
            self.img.save('img/'+str(count).rjust(5,'0')+'.png')
            count += 1