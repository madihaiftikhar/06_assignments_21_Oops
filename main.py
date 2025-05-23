class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor


mul = Multiplier(3)


print(callable(mul))  


print(mul(10))  
print(mul(5))  
