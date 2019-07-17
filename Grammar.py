import re

class Rules:

    _regex = {
        '[aeiou]':'A',
        '[^aeiou]':'B'
    }

    def __init__(self,s):
        self.s = re.sub('[\s]+','',s)
    
    def apply(self):
        t = self.s
        for rxp in self._regex:
            t = re.sub(rxp,
                       self._regex[rxp],
                       t,
                       flags=re.IGNORECASE)
        return {self.s:t}