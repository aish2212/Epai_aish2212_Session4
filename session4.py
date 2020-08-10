import random
import cmath
import decimal
from decimal import Decimal , ROUND_HALF_UP, localcontext

class Qualean:
    '''
        This is a Qualean Class. 
    '''
    def __init__(self, user_input):
        self.user_input = user_input
        if ((user_input == -1) | (user_input == 0) | (user_input == 1)):
            with localcontext() as ctx:
                ctx.rounding = ROUND_HALF_UP
                ctx.prec = 10
                self.input_value = Decimal(user_input) * Decimal(random.uniform(-1, 1))
        else:
            raise ValueError("input value must be either 1 or 0 or -1")
   

    def __round__(self):
        return self.input_value

    def __and__(self, other):
        return bool(self.input_value) and bool(other.input_value)
    
    def __or__(self, other):
        return bool(self.input_value) or bool(other.input_value)
        
    def __ge__(self, other):
        return self.input_value >= other.input_value

        
    def __gt__(self, other):
        return  self.input_value > other.input_value

        
    def __invertsign__(self):
        return  self.input_value*-1

        
    def __le__(self, other):
        return self.input_value <= other.input_value

        
    def __lt__(self, other):
        return self.input_value < other.input_value

        
    def __mul__(self, other):
        with localcontext() as ctx:
            ctx.rounding = ROUND_HALF_UP
            ctx.prec = 10
            return self.input_value * other.input_value

            
    def __eq__(self, other):
        return self.input_value == other.input_value

        
    def __add__(self, other):
        return  self.input_value + other.input_value

        
    def __str__(self):
        return 'Qualean_value[{0}] = {1}'.format(self.user_input, self.input_value)
    
    
    def __repr__(self):
        return 'Qualean_value[{0}] = {1}'.format(self.user_input, self.input_value)
    
    
    def __bool__(self):
        return bool(self.input_value)

        
    def __float__(self):
        return float(self.input_value)

        
    def __sqrt__(self):
        return cmath.sqrt(self.input_value)
