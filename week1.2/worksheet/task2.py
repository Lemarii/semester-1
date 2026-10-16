# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

numbers = read_numbers()

if len(numbers) == 0:
    sys.exit("Error: no numbers provided")

minimum = min(numbers)
maximum = max(numbers)

mean = sum(numbers) / len(numbers)

numbers.sort()

n = len(numbers)
middle = n // 2

if n % 2 == 0:
    median = (numbers[middle - 1] + numbers[middle]) / 2
else:
    median = numbers[middle]

print(f"Minimum = {minimum}")
print(f"Maximum = {maximum}")
print(f"Mean = {mean}")
print(f"Median = {median}")