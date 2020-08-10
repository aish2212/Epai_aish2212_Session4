# Assignment: EPAi Session 4, Numeric Types - II
- This python assignment tests 
  - the understanding of python's decimal module, boolean objects and operations, 
  - practice writing test cases for the code
  - get familiar with github actions.

# Qualean Class
- Qualean Class accepts only 3 possible real states. True, False, and Maybe (1, 0, -1) as input.
- The input will be multiplied immediately with the imaginary number and get stored.
- the imaginary number is generated randomly using random.uniform(-1, 1) 
- The real state and imaginary number are multiplied with it and stores that number internally after using Bankers rounding to 10th decimal place. 

# Variables
- user_input - Input given by the user (either 1 or 0 or -1)
- input_value - Converted Qualean value by multiplying the user_input and the imaginary number

## Functions
# __init__(self,user_input)
   - 

# __and__(self, other)
	- Add a Qualean to another Qualean.
	- It also supports addition of Qualean to another data type like int, float or decimal
	
# __or__(self, other)
	- Checks wether one of the two are Qualean data types and not zero
	
# __bool__(self)
	- Converts the Qualean to bool
	- False if Qualean is 0 else True
	
# __eq__(self, other)
	- Checks if value of the Qualean object is equal to value
	- value can be int, float, bool or decimal
	
# __float__(self)
	- Converts Qualean to float
	- example, type (float (Qualean (1))) = 'float'
	
# __ge__(self, other)
	- return self>=value.
	
# __gt__(self, other)
	- return self>value.
	
# __invert__(self)
	- return (-1) * self
	
# __le__(self, other)
	- return self<=value.
	
# __lt__(self, other)
	- return self< value.
	
# __mul__(self, other)
	- return self * value
	
# __repr__(self)
	- return repr(self).
	
# __sqrt__(self)
	- return math.sqrt (self)
	
# __str__(self)
	- return str(self).

## Tests

- test_readme_exists
	- test to check whether README.md file exists

- test_readme_contents
    - test whether the README.md file have description  
	
- test_readme_file_for_formatting
    - test whether the readme file have proper formatting 

- test_readme_proper_description
	- check if readme has all these fields "__and__,  __or__, __repr__, __str__, __add__, __eq__, __float__, __ge__, __gt__, __invertsign__, __le__, __lt__, __mul__, __sqrt__, __bool__"

- test_indentations
    - check whether the source file have proper indentations and space according to PEP8

- test_function_name_had_cap_letter
	- test if the func name declared properly
	
- test_functions_list
    - test if all the function are declared such as "__and__,  __or__, __repr__, __str__, __add__, __eq__, __float__, __ge__, __gt__, __invertsign__, __le__, __lt__, __mul__, __sqrt__, __bool__"
	
- test_Qualean_equality
    - test if qualean1==qualean2
	
- test_Qualean_and
	- test the addition of two qualeans
	
- test_Qualean_mul
	- test the mul of two qualeans

- test_Qualean_and
	- test and operation on two qualeans
	
- test_Qualean_or
	- test or operation on two qualeans
	
- test_Qualean_float
    - test whether qualean is converted to float type

- test_Qualean_bool
    - test whether qualean is converted to bool type

- test_Qualean_repr
	- test the __repr__() function
	
- test_Qualean_str
	- test the __str__() function\
	
- test_Qualean_ge
	- test qualean1>=qualean2
	
- test_Qualean_gt
	- test qualean1>qualean2

- test_Qualean_le
	- test qualean1<=qualean2
	
- test_Qualean_lt
	- test qualean1< qualean2

- test_Qualean_sqrt
	- test the sqauare root function.
	- if the number is positive, the sqaure root of the number will be qualean type
	- if the number if of negative, the square root of the number will be of complex number.

- test_Qualean_sum_100times
	- test if qualean number is added for 100times with the right precision in place

- test_Qualean_return_false_if_q2_notdefined
	- check if q1 and q2 returns False, when q2 is not defined as well and q1 is False
	
- test_Qualean_return_True_if_q2_notdefined
	- check if q1 or q2 returns True, when q2 is not defined as well and q1 is not false
	
- test_Qualean_1millionsum_closetozero
	- test sum of million qualean which should be very close to zero as the initializations are from [-1,1,0]
	
- test_Qualean_invalid_integer_input
	- Test if the object declared is from [-1,0,1]
	
- test_Qualean_bankers_rounding
	- Test if the bankers rounding upto 10 digits is taken care of

- test_Qualean_invertsign
	- test invert function.
	- Inverting the q1  and adding with the qualean q1, test whether the output is equal to zero.

