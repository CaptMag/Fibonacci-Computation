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