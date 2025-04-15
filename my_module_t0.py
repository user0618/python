def say_hello(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

class Greeter:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hi, I'm {self.name}!"
