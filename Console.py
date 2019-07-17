import sys

class Progress:

    def __init__(self,total):
        self.total = total
        
    def update(self,idx,type):
        sys.stdout.write("[%s] Progress: %d / %d \r" % (type,idx,self.total))
        sys.stdout.write("[%s] Progress: %d / %d \r" % (type,idx,self.total))
        sys.stdout.flush()