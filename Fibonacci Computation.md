# This document is only created to understand the idea of computing a Fibonacci number in 1 second

This is all stolen from [this video](https://www.youtube.com/watch?v=KzT9I1d-LlQ). I'm just trying to understand the mathematics behind it :D

## The Fibonacci Equation

The fibonacci sequence requires both the last and 2nd last numbers in order to produce a new fibonnaci number. Starting from 0 and going, fibonacci is an extraordinary sequence. However, one question may be, how do we calculate this?

Using something known as **Linear Reccurence** (or Fibonnaci Recurrence) we come up with an equation that can continuously output new fibonacci results.

$$
F_n = F_{n-1} + F_{n-2}, \quad \text{for } n \geq 2
$$

 Using this equation, we can constantly compute new numbers, but let's go a bit deeper.

### Explanation

(Initial Conditions F 0 = 0. F 1 = 1).

$$
\quad \text{The sequence begins as so: } 0,1,1,2,3,5,8,13,21,34,...
$$

Following this pattern, each term is the sum of the previous two terms.

$$
F_2 = F_1 + F_0 = 1 + 0 = 1
$$
$$
F_3 = F_2 + F_1 = 1 + 1 = 2
$$
$$
F_4 = F_3 + F_2 = 2 + 1 = 3 \quad \text{and so on }
$$

Although this is an efficient way to use liner reccurence, it is not the only way to calculate fibonacci

## Closed-Form Solution

Without being too complicated, a **Closed-Form Solution** is a formula that uses a finite number (whole numbers, fractions, decimals) of standard math operations (add, subtract, divide, multiply) and well-defined functions (sine, co-sine, or exponential functions)

### Fibonacci Sequence

To clearly define a closed-form solution, a great example is the fibonacci sequence

$$
F_n = F_{n-1} + F_{N-2}, \quad \text{with } F_0 \quad \text{and } F_1 = 1
$$

Here is the Fibonacci sequeunce using linear reccurence, however, we need this equation in a closed-form solution. In order to do that we have to "guess" what `N` is.

In a normal arithmetic series the equation goes as so:

$$S_n = 1 + 2 + 3 + ... + n$$

This simulates a pattern, of adding numbers until it reaches whatever value `N` is.

However, this is not all, we can simplify this into a **Closed-Form Solution**

$$S_n = \frac{n(n + 1)}{2}$$


Using the equation above we know that $$F_0 \quad \text{and } F_1 = 1$$

After figuring our base values, we will use the characteristic equation to solve this equation

$$\quad \text{First we will set } F_n = r^n. \quad \text{We then set } r^n \quad \text{Into the original equation. } r^n = r^{n-1} + r^{n-2}.

\quad \text{We then divide through } r^{n-1} \quad \text{for } r\neq0: r^2 = r + 1$$

Now that we have everything set, we must transfer everything to the other side, setting it into a quadratic form

$$r^2 - r -1 = 0$$

Now due to not being able to factor this, we must use the quadratic formula

$$r = \frac{-(-1) \pm \sqrt{(-1)^2 - 4(1)(-1)}}{2(1)} = \frac{1 \pm \sqrt{5}}{2}$$

Once we have found the solution of the quadratic we will use the golden ratio and the conjugate of the golden ratio to further calculate the fibonacci sequence using **Binet's Formula**

$$
\quad \text{Golden Ratio } \frac{1 + \sqrt{5}}{2}
\quad \text{and Conjugate } \frac{1 - \sqrt{5}}{2}
$$

Now that we have both, how can this be faster than **Linear Recurrence**?

Due to the golden ratio and conjugate rapidly growing compared the Linear Recurrence, this allows Binet's Formula to reach much larger numbers.  
Using this equation:

$$ F_n = F_(n-1) + F_(n-2)$$

This means we must calculate the 2 previous fibonacci numbers in order to get the current number, however with Binet's Formula we can do the same thing, but with fewer multiplication, exponentials and division.

$$ F_n = \frac{\phi^n - \psi^n}{\sqrt{5}} $$

Using this equation we can compute F(n) to exponential large numbers compared to a basic Linear Recurrence output. However, not everything is perfect, and with Binet's Formula comes percision errors, as it is not perfect when calculating an exact result.

Now how would this work in Python? Using the code below, we are able to calculate the largest Fibonacci number using Linear Recurrence in 1 second

```python
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

print(f"Linear Recurrence has reached the {n - 2}st Fibonacci Number!")
```

Although very simple, it clearly shows the calculation, using the last 2 terms to calculate the new term, all while under a 1 second time constraint.  
Unfortunately, this only gets us the 31st fibonacci number, quite pathetic compared to how large numbers can go.  
Now that we realize the lack of efficiency, it is time to try out Binet's Formula

```python
def Binet_Formula(limit):

    golden_ratio = (S(1) + math.sqrt(5)) / (2)
    conjugate = (S(1) - math.sqrt(5)) / (2)

    laps = time.perf_counter()

    x = 0
    calculation = 0

    while time.perf_counter() - laps < limit:

        calculation = (golden_ratio ** x - conjugate ** x) / math.sqrt(5)

        calculation = round(calculation)

        x += 1

    
    print(f"Binet's Formula has reached the({x - 1}th) Fibonacci Number!")


Binet_Formula(1)
```

Looking at this code, we are able to efficiently calculate the fibonacci sequence with minimal time delay and calculation. However, this comes with its own problems.  
After running this code, we reach around the 785th to 805th fibonacci number, while much higher than 31, it lacks percision and often varies depending on performance.  
This is also quite little compared to how large we can truly go, and with that we introduce top-down and bottom-up approaches to our code.

## Memoization and Top-Down Approach

We have used both **recursion and Binet's Formula (or Closed-Form Solution)** to compute the largest fibonacci number we can in 1 second.  
Although working well, we have not even stratched the surface of how large fibonacci numbers can go, and although the 800+ fibonacci number is a big number, it is nothing compared to the hundreds of thousands of fibonacci numbers we can compute in a limited time.

### What is a Top Down Approach

A top down approach starts by using the original problem and breaking it down into smaller sub-problems. In our case, we are trying to find F(n) and to do that we must go from **top to bottom** and recursively compute F(n-1) and F(n-2).

Now how is this different from Linear Recurrence? Well, they are very identical, however, **memoization** uses a **lazy evaluation** meaning they only compute sub-problems when needed.  
By doing this, they can save already computes fibonacci numbers into a cache (or dictionary) and reuse them when needed.

```bash
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34... N]
```

Following the example above, it will store previously calculated fibonacci numbers, and use them when needed, rather than constantly re-computing the numbers.

```python
def memoization(a, memo={}):
    if a in memo:
        return memo[a]
    
    if a <= 1:
        return a
    memo[a] = memoization(a - 1, memo) + memoization(a - 2, memo) 
    return memo[a]

a = 0

while time.perf_counter() - start < 1:

    memoization(a)
    a += 1

print(f'Memoization calculated the {a}th Fibonacci term!')
```

Looking at the Python code here, we can see the dictionary `memo` which saved previously computed fibonacci numbers, and reuses them when computing new ones.  
This small addition skyrockets our results, from a measly 805 to over 125 thousand!  
But like everything, there is always room for improvement, and this is where a Bottom-up approach comes in.

## Tabulation and Bottom-Up Approach

Similar to a Top-Down Approach, a **Bottom-Up Approach** starts from the smallest sub problem and builds its way up to the original problem. It stores these results in a table for reuse.  
Now although this seems identical to a Top-Down Approach there is 1 tweak you can do than will make a major difference. That is deleting un-used subproblems.  
Rather than keeping old subproblems it instead deletes them and only calculates the previous two fibonacci numbers, creating an endless loop.  
Using this, the program is much simpler and efficient, and there is no need to save nor re-calculate previous fibonacci terms, as the program only needs to calculate the previous 2, get the new term, and then repeat the process, deleting the ones that are not used.

### Python Tabulation

```python
def tabulation():
    
    prev = 0
    cur = 1
    iteration = 0

    starts = time.perf_counter()

    while time.perf_counter() - starts < 1:

        prev, cur = cur, prev + cur

        iteration += 1

    
    print(f'Tabulation reached the {iteration}th Fibonacci Number!')
    return cur

tabulation()
```

Compared to most of our code, this is the most simple one. It uses the set parameters of `prev (previous)` and `cur (current)` to store in the fibonacci numbers of F(n-1) and F(n-2).

This then sets a new parameter ``prev, cur = cur, prev + cur`` which sets `prev` into `cur` and `cur` into the soltuion of `prev + cur`, thus minimizing storage and latency.  
With this new code, we are able to compute to over 250 thousand Fibonacci Numbers! However, we can still go a lot more deeper and create larger fibonacci numbers...
