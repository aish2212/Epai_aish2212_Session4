import pytest
import random
import string
import session4
import os
import inspect
import re
import math, cmath

import decimal
from decimal import Decimal

ZERO_INPUT_VALUE = 0
INPUT_VALUE_1 = Decimal(random.choice([-1, 1, 0]))
INPUT_VALUE_2 = Decimal(random.choice([-1, 1, 0]))

README_CONTENT_CHECK_FOR = [
    'Qualean',
    '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__ge__',
    '__gt__',
    '__invertsign__',
    '__le__',
    '__lt__',
    '__mul__',
    '__sqrt__',
    '__bool__',
]

FUNCTION_LIST = [
    '__and__',
    '__or__',
    '__repr__',
    '__str__'
    '__add__'
    '__eq__'
    '__float__'
    '__ge__'
    '__gt__'
    '__invertsign__'
    '__le__'
    '__lt__'
    '__mul__'
    '__sqrt__'
    '__bool__'
]
#1
def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

#2
def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

#3
def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

#4    
def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

#5
def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

#6
def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

#7
def test_functions_list():
    ALL_FUNCTIONS_PRESENT = True
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        if function not in FUNCTION_LIST:
            assert ALL_FUNCTIONS_PRESENT == False, "You have not added all the functions/class"
        else:
            ALL_FUNCTIONS_PRESENT == True

#8            
def test_Qualean_equality():
    r1 = session4.Qualean(ZERO_INPUT_VALUE)
    r2 = session4.Qualean(ZERO_INPUT_VALUE)
    assert r1 == r2, "Both the qualean values are equal"

#9   
def test_Qualean_add():
    q1 = session4.Qualean(INPUT_VALUE_1)
    q2 = session4.Qualean(INPUT_VALUE_2)
    assert math.isclose(q1.__add__(q2), q1.input_value+q2.input_value, rel_tol=1e-8 )
 
#10
def test_Qualean_mul():
    q1 = session4.Qualean(INPUT_VALUE_1)
    q2 = session4.Qualean(INPUT_VALUE_2)
    assert math.isclose(q1.__mul__(q2), q1.input_value*q2.input_value, rel_tol=1e-8 )

#11    
def test_Qualean_and():
    q1=session4.Qualean(0)
    q2=session4.Qualean(1)
    q3=session4.Qualean(-1)
    assert((q1 & q2)==False)
    assert((q2 & q3)==True)
    assert((q1 & q3)==False)
    

#12
def test_Qualean_or():
    q1=session4.Qualean(1)
    q2=session4.Qualean(-1)
    q3=session4.Qualean(0)
    assert((q1 | q2)==True)
    assert((q2 | q3)==True)
    assert((q1 | q3)==True)
 
#13 
def test_Qualean_float():
    q1=session4.Qualean(INPUT_VALUE_1)
    assert(float(q1)==float(round(q1)))

#14
def test_Qualean_bool():
    q1=session4.Qualean(0)
    q2=session4.Qualean(1)
    q3=session4.Qualean(-1)
    assert(bool(q1)==False)
    assert(bool(q2)==True)
    assert(bool(q3)==True)

#15
def test_Qualean_repr() :
    q1=session4.Qualean(INPUT_VALUE_1)
    assert(repr(q1)==('Qualean_value['+ str(INPUT_VALUE_1) + '] = '+str(round(q1))))

#16
def test_Qualean_str() :
    q1=session4.Qualean(INPUT_VALUE_1)
    assert(str(q1)==('Qualean_value['+ str(INPUT_VALUE_1) + '] = '+str(round(q1))))

#17
def test_Qualean_ge():
    q1=session4.Qualean(INPUT_VALUE_1)
    q2=session4.Qualean(INPUT_VALUE_2)
    assert((q1>=q2)==(round(q1)>=round(q2)))

#18
def test_Qualean_gt():
    q1=session4.Qualean(INPUT_VALUE_1)
    q2=session4.Qualean(INPUT_VALUE_2)
    assert((q1>q2)==(round(q1)>round(q2)))
    
#19
def test_Qualean_le():
    q1=session4.Qualean(INPUT_VALUE_1)
    q2=session4.Qualean(INPUT_VALUE_2)
    assert((q1<=q2)==(round(q1)<=round(q2)))
    
#20
def test_Qualean_lt():
    q1=session4.Qualean(INPUT_VALUE_1)
    q2=session4.Qualean(INPUT_VALUE_2)
    assert((q1<q2)==(round(q1)<round(q2)))
    
#21
def test_Qualean_sqrt():
    q1=session4.Qualean(INPUT_VALUE_1)
    if(q1>=0):
        assert ((q1.__sqrt__())==math.sqrt(q1))
    else:
        assert ((q1.__sqrt__())==cmath.sqrt(q1))
    
#22
def test_Qualean_sum_100times():
    q1 =session4.Qualean(INPUT_VALUE_1)
    new_q = session4.Qualean(0)
    for i in range(100):
        new_q += q1.input_value
    assert math.isclose(new_q, q1 * 100, rel_tol=1e-4)
    
#23
#q1 or q2 returns True when q2 is not defined as well and q1 is not false
def test_Qualean_return_True_if_q2_notdefined():
    q1 = session4.Qualean(1)
    q3 = session4.Qualean(-1)

    assert True == (bool(q1) or q2)
    assert True == (bool(q3) or q4)
    
#24
#q1 and q2 returns False when q2 is not defined as well and q1 is False    
def test_Qualean_return_false_if_q2_notdefined():
    q1 = session4.Qualean(0)

    assert False == (q1 and q2)
   
#25
def test_Qualean_1millionsum_closetozero():
     q1 = 0
     new_q = session4.Qualean(0)
     for i in range(1000000):
         q1 = Decimal(random.choice([-1, 1, 0]))
         q1 = session4.Qualean(q1)
         new_q += q1.input_value
     assert math.isclose(new_q, 0, rel_tol=1)
  
#26
def test_Qualean_invalid_integer_input():
    with pytest.raises(ValueError) as execinfo:
        _ = session4.Qualean(2)
    assert "ValueError" in str(execinfo)
	
#27
def test_Qualean_bankers_rounding():
    q1 = session4.Qualean(1)
    assert len(str(q1).split(".")[-1]) == 10
	
#28 
def test_Qualean_invertsign():
    q1 = session4.Qualean(INPUT_VALUE_1)
    y = q1.__invertsign__()
    assert q1 + y == 0

    