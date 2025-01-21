import math
import sys
import time
from sympy import S, sqrt

lap = time.perf_counter()

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    
n = 0

while time.perf_counter() - lap < 1:

    fibonacci_recursive(n)
    n += 1

print(f"Linear Recurrence has reached the {n - 1}st Fibonacci Number!")

# End result: 31st Fibonacci Number

#def Quadratic_Example(a, b, c):

#    inside = b**2 - 4*a*c

#    if inside < 0:
#        return "No Solution"

#    root1 = (- b + math.sqrt(inside)) / (a * 2)
#    root2 = (- b - math.sqrt(inside)) / (a * 2)

#    return root1, root2

#a, b, c = 1, 5, 3

#solutions = Quadratic_Example(a, b, c)

#print (solutions)

def Binet_Formula(limit):

    golden_ratio = (S(1) + math.sqrt(5)) / (2)
    conjugate = (S(1) - math.sqrt(5)) / (2)

    lap = time.perf_counter()

    n = 0
    calculation = 0

    while time.perf_counter() - lap < limit:

        calculation = (golden_ratio ** n - conjugate ** n) / math.sqrt(5)

        calculation = round(calculation)

        n += 1

    
    print(f"Binet's Formula has reached the({n - 1}th) Fibonacci Number!")


Binet_Formula(1)
