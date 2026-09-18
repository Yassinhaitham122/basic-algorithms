"""
Problem 3: Rearrange Array Elements

Rearrange Array Elements so as to form two number such that their sum is 
maximum. Return these two numbers. You can assume that all array elements are 
in the range [0, 9]. The number of digits in both the numbers cannot differ by 
more than 1. You're not allowed to use any sorting function that Python 
provides and the expected time complexity is O(nlog(n)).

You should implement the function body according to the rearrange_digits 
function signature. Use the test cases provided below to verify that your 
algorithm is correct. If necessary, add additional test cases to verify that 
your algorithm works correctly.
"""

def rearrange_digits(input_list):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge(left, right)

    def merge(left, right):
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    digits = merge_sort(input_list)

    first = 0
    second = 0

    for i, digit in enumerate(digits):
        if i % 2 == 0:
            first = first * 10 + digit
        else:
            second = second * 10 + digit

    return first, second

def test_function(test_case: tuple[list[int], list[int]]) -> None:
    """
    Test the rearrange_digits function with a given test case.

    Args:
    test_case (tuple[list[int], list[int]]): A tuple containing two elements:
        - A list of integers representing the input array to be rearranged.
        - A list of two integers representing the expected output.

    Returns:
    None: Prints "Pass" if the sum of the output from rearrange_digits matches 
    the sum of the expected output, otherwise prints "Fail".
    """
    output: tuple[int, int] = rearrange_digits(test_case[0])
    solution: list[int] = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

if __name__ == '__main__':
    # Edge cases
    print(rearrange_digits([9]))
    # Expected output: (9, 0)

    print(rearrange_digits([8, 1]))
    # Expected output: (8, 1)

    print(rearrange_digits([0, 0, 0, 0]))
    # Expected output: (0, 0)

    # Normal cases
    print(rearrange_digits([1, 2, 3, 4, 5]))
    # Expected output: (531, 42)

    print(rearrange_digits([]))
    # Expected output: (0, 0)

    print(rearrange_digits([4, 6, 2, 5, 9, 8]))
    # Expected output: (964, 852)