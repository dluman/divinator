from itertools import product
from functools import reduce
from operator import add
from PIL import Image, ImageDraw

class Gram:

    def __init__(self):
        self.trigrams = None
        self.hexagrams = None
        
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
        self.combine([[l] for l in g])
    
    def combine(self,g):
        self.trigrams = [e for e in product(g,repeat=3)]
        self.hexagrams = [reduce(add,e) for e in product(self.trigrams,repeat=2)]