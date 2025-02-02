#import numpy as np

#rows = int(input("Enter # of rows: "))
#columns = int(input("Enter # of columns: "))

#matrix = []

#for i in range(rows):
#    row = list(map(int, input(f"Enter {columns} numbers for row {i+1}, seperated by spaces: ").split()))
#    matrix.append(row)

#print("your matrix:")
#for row in matrix:
#    print(row)

#num = list(map(int, input("Enter the numbers: ").split()))

#for x in range(rows):
#    for y in range(columns):
#        print(num, end="")
#    print()

row = int(input("Select # of rows: "))
columns = int(input("Select # of columns: "))

#print(f"Enter {row * columns} numbers separated by spaces: ")
nums = list(map(int, input(f"Enter {row * columns} numbers separated by spaces: ").split()))

if len(nums) != row * columns:
    print("Error: Incorrect number of values entered!")
    exit()

print(f"Enter {row * columns} numbers for Matrix A:")
nums_A = list(map(int, input().split()))
matrix_A = [nums_A[i * columns:(i + 1) * columns] for i in range(row)]

print(f"Enter {columns * row} numbers for Matrix B:")
nums_B = list(map(int, input().split()))
matrix_B = [nums_B[i * row:(i + 1) * row] for i in range(columns)]

result = [[sum(matrix_A * matrix_B for matrix_A, matrix_B in zip(matrix_A_row, matrix_B_columns))
           for matrix_B_columns in zip(*matrix_B)]
            for matrix_A_row in matrix_A]

print("\nMatrix A:")
for row in matrix_A:
    print(row)

print("\nMatrix B:")
for row in matrix_B:
    print(row)

print("\nResultant Matrix:")
for r in result:
    print(r)
