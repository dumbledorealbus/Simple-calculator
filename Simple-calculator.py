a = float (input('Enter a Number: \n'))
op = input ("""Enter Operation \n'+' for Addition, '-' for subtraction, 'x', for Multiplication
            '/' for Division: \n""")
b = float (input ('Enter a Second Number: \n'))

def calculate (a,b):
    if op == '+':
        return a+b
    elif op == '-' :
        return a-b
    elif op == '/':
        return a/b
    elif op == 'x':
        return a*b

print ('Your Answer is:',calculate(a,b))
