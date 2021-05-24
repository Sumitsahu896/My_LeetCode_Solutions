class Solution:
    def __init__(self):
        self.dict = {0:0, 1:1}
    
    def fib(self, n: int) -> int:
        if n not in self.dict:
            self.dict[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.dict[n]        
