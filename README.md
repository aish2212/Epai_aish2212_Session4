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
   - The init function get the user input, and converts the user input to Qualean type
   - The init function checks whether the user input is of values -1, 0 or 1
   - Qualean type number is the number where the user input of [1,0,-1] is multiplied with a imaginary number generated randomly using random.uniform(-1, 1).
   - The precision of the output qualean value is of 10 decimal places.

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
	
#PYTEST

Run pytest -vv
  pytest -vv
  shell: /bin/bash -e {0}
  env:
    pythonLocation: /opt/hostedtoolcache/Python/3.8.5/x64
============================= test session starts ==============================
platform linux -- Python 3.8.5, pytest-6.0.1, py-1.9.0, pluggy-0.13.1 -- /opt/hostedtoolcache/Python/3.8.5/x64/bin/python
cachedir: .pytest_cache
rootdir: /home/runner/work/Epai_aish2212_Session4/Epai_aish2212_Session4
collecting ... collected 28 items

test_session4.py::test_readme_exists PASSED                              [  3%]
test_session4.py::test_readme_contents PASSED                            [  7%]
test_session4.py::test_readme_file_for_formatting PASSED                 [ 10%]
test_session4.py::test_readme_proper_description PASSED                  [ 14%]
test_session4.py::test_indentations PASSED                               [ 17%]
test_session4.py::test_function_name_had_cap_letter PASSED               [ 21%]
test_session4.py::test_functions_list PASSED                             [ 25%]
test_session4.py::test_Qualean_equality PASSED                           [ 28%]
test_session4.py::test_Qualean_add PASSED                                [ 32%]
test_session4.py::test_Qualean_mul PASSED                                [ 35%]
test_session4.py::test_Qualean_and PASSED                                [ 39%]
test_session4.py::test_Qualean_or PASSED                                 [ 42%]
test_session4.py::test_Qualean_float PASSED                              [ 46%]
test_session4.py::test_Qualean_bool PASSED                               [ 50%]
test_session4.py::test_Qualean_repr PASSED                               [ 53%]
test_session4.py::test_Qualean_str PASSED                                [ 57%]
test_session4.py::test_Qualean_ge PASSED                                 [ 60%]
test_session4.py::test_Qualean_gt PASSED                                 [ 64%]
test_session4.py::test_Qualean_le PASSED                                 [ 67%]
test_session4.py::test_Qualean_lt PASSED                                 [ 71%]
test_session4.py::test_Qualean_sqrt PASSED                               [ 75%]
test_session4.py::test_Qualean_sum_100times PASSED                       [ 78%]
test_session4.py::test_Qualean_return_True_if_q2_notdefined PASSED       [ 82%]
test_session4.py::test_Qualean_return_false_if_q2_notdefined PASSED      [ 85%]
test_session4.py::test_Qualean_1millionsum_closetozero PASSED            [ 89%]
test_session4.py::test_Qualean_invalid_integer_input PASSED              [ 92%]
test_session4.py::test_Qualean_bankers_rounding PASSED                   [ 96%]
test_session4.py::test_Qualean_invertsign PASSED                         [100%]

============================== 28 passed in 4.89s ==============================

