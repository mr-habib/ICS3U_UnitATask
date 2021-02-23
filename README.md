# ICS3U_UnitATask

Your job is to create a calculator in python.

## Input Specifications
The input will be a line that consists of a mathematical expression consisting only of one operator and two operands (two numbers and one math operation).
Example:
```
>>> Enter expression: 187 + 45
```
Feel free to get creative with your prompt!
The operator will always be surrounded by a space.

## Output Specification
The output will consist of the original expression, followed by an equal sign, followed by the answer.
Example:
```
>>> 187 + 45 = 232
```

To accomplish this, you will need to:
1. Split up the operation into two numbers and an operator (Hint: input_list = input_string.split(' ') will put the three elements in a list. THen input_list[0] will give you the first number (as a string), input_list[1] will give you the operator ('+' in this case) and input_list[2] will give you the second number)
2. Convert the two numbers into integers
3. Determine what operation to perform on the two numbers (use if statements: ``` if operator == '+': ...```)
4. Possible operators include:
  * \+
  * \-
  * \*
  * /
  * ^ (power, so 2 ^ 3 should = 8) 

I have included a .pyc file. This is a compiled python file. You can run it like a normal file to see what your code should do. 

# Important
Your output needs to be exactly in the following manner:
```
num + num = num
```
Notice all of the outputs in my .pyc.

If you do not output exactly like this, you will not pass the autograder!

Also, you will be marked on your variable naming conventions, neatness of code (ample spacing and such) and on providing comments where you think it necessary.
