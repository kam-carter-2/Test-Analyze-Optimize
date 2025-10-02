# problem4_palindrome.py

"""
Problem 4: Palindrome Checker
Solution + Test Cases + Analysis
"""

# Basic solution using slicing
def is_palindrome(s: str) -> bool:
    return s == s[::-1]

# Test cases
assert is_palindrome("racecar") is True
assert is_palindrome("hello") is False
assert is_palindrome("a") is True
assert is_palindrome("") is True

"""
Analysis:
- Best, Worst, Average Case: O(n)
- Space Complexity: O(n) (string slice created)
- Optimization: Two-pointer method reduces space to O(1).
"""

# Optimized version (refactored, two-pointer method)
def is_palindrome_optimized(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Test cases for optimized
assert is_palindrome_optimized("racecar") is True
assert is_palindrome_optimized("hello") is False
assert is_palindrome_optimized("a") is True
assert is_palindrome_optimized("") is True

"""
Refactor Analysis:
- Time Complexity: O(n) (same as original)
- Space Complexity: O(1) (better than O(n))
- Trade-off: Slightly longer code but saves memory.
"""
