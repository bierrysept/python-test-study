from typing import Union

class Calculator:
    def divide(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y
    
    def add(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        return x + y
    
if  __name__ == "__main__":
    calculator = Calculator()
