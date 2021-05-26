from main import eval_math
from random import randint, choice

def test_eval_math_simple_add():
    assert(eval_math("10 + 6") == "10 + 6 = 16")

def test_eval_math_simple_sub():
    assert(eval_math("11 - 6") == "11 - 6 = 5")

def test_eval_math_simple_sub2():
    assert(eval_math("6 - 12") == "6 - 12 = -6")

def test_eval_math_simple_mult():
    assert(eval_math("8 * 9") == "8 * 9 = 72")

def test_eval_math_simple_div():
    assert(eval_math("11 / 5") == "11 / 5 = 2.2")

def test_eval_math_simple_pow():
    assert(eval_math("3 ^ 4") == "3 ^ 4 = 81")

def test_eval_math_random_1():
    num1 = randint(0, 1000)
    num2 = randint(0, 1000)
    list_of_operators = ['+', '-', '*', '/', '**']
    op = choice(list_of_operators)
    str_input = f"{num1} {op} {num2}"
    ans = eval(str_input)
    if op == "**":
        str_input = f"{num1} ^ {num2}"
    expected = f"{str_input} = {ans}"
    assert(eval_math(str_input) == expected)

