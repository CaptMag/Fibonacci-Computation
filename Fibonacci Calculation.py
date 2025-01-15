import time
import math
import sys

# Time: Used to track the elapsed time for each algorithm
#Math: provides math functions
#sys: used to configure internal limits (large integers)

# Increase the max string digits limit for large integers
sys.set_int_max_str_digits(10**6)  # Increase the limit to 1 million digits

def linear_recurrence(limit):
    """Compute the largest Fibonacci number within the time limit using linear recurrence."""
    start_time = time.time()  # Record the start time
    F_0, F_1 = 0, 1  # Initialize the first two Fibonacci numbers
    n = 1  # Start counting from the first Fibonacci number

    while time.time() - start_time < limit:  # Continue until the time limit is reached
        F_next = F_0 + F_1  # Compute the next Fibonacci number
        F_0, F_1 = F_1, F_next  # Update for the next iteration
        n += 1  # Increment the index

    return n - 1, math.log10(F_0) if F_0 > 0 else 0  # Return the largest index and log10 of the Fibonacci number

# The purpose of this is to keep computing fibonacci numbers (for linear reccurence) until the time has stopped.
#Instead of representing a large number, it gives tthe logarithmic value, making it much smaller

def closed_form(limit):
    """Compute the largest Fibonacci number within the time limit using the closed-form solution."""
    start_time = time.time()
    sqrt_5 = math.sqrt(5)  # Calculate √5
    phi = (1 + sqrt_5) / 2  # Calculate the golden ratio (φ)

    n = 0
    log_phi = math.log10(phi)  # Precompute log10(φ)
    log_sqrt_5 = math.log10(sqrt_5)  # Precompute log10(√5)

    while time.time() - start_time < limit:  # Continue until the time limit is reached
        log_F_n = n * log_phi - log_sqrt_5  # Compute log10(F_n) using Binet's formula
        n += 1  # Increment the index

    return n - 1, log_F_n  # Return the largest index and log10 of the Fibonacci number

#The purpose of this is to use Binet's formula to compute fibonacci numbers directly into logarithmic form.
#  This is also more efficient than linear reccurence as it avoids repetition

def main():
    time_limit = 1  # 1 second

    print("Running Linear Recurrence...")
    linear_n, linear_log_fib = linear_recurrence(time_limit)
    print(f"Linear Recurrence: Largest Fibonacci index = {linear_n}, log10(value) = {linear_log_fib:.2f}")

    print("\nRunning Closed-Form Solution...")
    closed_n, closed_log_fib = closed_form(time_limit)
    print(f"Closed-Form: Largest Fibonacci index = {closed_n}, log10(value) = {closed_log_fib:.2f}")

# runs the iterative fibonacci algorithm, outputs largest index of (N)
# also runs the closed-form algorithm. Also outputs the largest index of (N)

if __name__ == "__main__":
    main()
