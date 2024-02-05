class MathUtils:
    def __init__(self):
        self.a=6
        self.b=4
    
    def add(self):
        return self.a+self.b
    
    def substract(self):
        return self.a-self.b
    
    def mulltiply(self):
        return self.a*self.b

    def divide(self):
        if(self.b==0):
            return -1.0
        return self.a/self.b
    
