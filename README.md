# Fibonacci-Computation

Inspired by a video I watched, I will explain the following:

How Fibonacci is created, what formula it uses to work, and computing the largest Fibonacci number in 1 second using different algorithms and formulas

Currently a work in progress document. Focusing currently on Linear Reccurence and Closed-Form Solution.

Future plans include Fourier Transform (DFT and FFT), Galois Theory, Karatsuba, and maybe 1 more.

Current results: [Linear Recurrence: 31st Fibonacci Number] [Binet's Formula: 785-805th Fibonacci Number]

Currently added `sympy` import, however, fluctuation is undergoing due to this

Added Memoization which allows a "cache" to be saved of previous computed Fibonacci results inside the `memo` library. Currently standing at the `125,089 Fibonacci Term`
Still working on the fluctuation problem

Added Tabulation which stores data in a `table`, before deleting it and calculating `F(n-1) and F(n-2)`. Using this calculation it can calculate at fast speeds without needing to hold onto older computed fibonacci numbers. Currently standing at `over 250,000 Fibonacci Terms`  
Like the others, fluctuation problems.
