"""
Add two random numbers together

Requires no setup. 
"""
import random

numA = random.random() * 10
"""Random number 1"""
    
numB = random.random() * 10    
"""Random number 2"""    

class Calc():
    """Provide methods for a calculator

    add -- Add two numbers and return sum.
    """    
    
    def add (self, num1, num2):
        """Add two numbers and return sum.
    
        Postional arguments:
        num1 -- an integer or double number (no default)
        num2 -- an integer or double number (no default)
    
        Returns:
        Sum of the two numbers.

        To run the doctest run "python -m doctest -v docs.py"

        >>> a = Calc()
        >>> a.add(1,2)
        3
        
        >>> a = Calc()
        >>> a.add(-1,-2)
        -3
        
        >>> a = Calc()
        >>> a.add(2**32,1)
        4294967297
        
        >>> a = Calc()
        >>> a.add(2**64,1)
        18446744073709551617

        >>> a = Calc()
        >>> a.add(2**64,2**64)
        36893488147419103232
        """
        return num1 + num2    

calc = Calc()
print(calc.add(numA, numB))



