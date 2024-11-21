class Accumulator:
    def __init__(self):
        self._count = 0
    
    @property # nem felülírható
    def count(self):
        return self._count
    
    def add(self, more=1):
        self._count += more
        return self._count
    
