# problem5_fizzbuzz.py

"""
Problem 5: FizzBuzz
Solution + Test Cases + Analysis
"""

def fizzbuzz(n: int) -> list:
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

# Test cases
assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
assert fizzbuzz(3) == ["1", "2", "Fizz"]

"""
Analysis:
- Time Complexity: O(n)
- Space Complexity: O(n) (result list)
- Optimization: Could print values directly instead of storing in list if memory is a concern.
"""
