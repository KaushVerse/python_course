# Missing Number Problem
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
# find the one that is missing from the array.

def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Example usage:
if __name__ == "__main__":
    nums = [3, 0, 1]
    print(f"The missing number is: {missing_number(nums)}")  # Output: 2