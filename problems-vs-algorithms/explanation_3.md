## Approach

I sort the digits with a merge sort and then assign them alternately to two
numbers, starting with the largest digit. This places the largest available
digits in the highest-value positions as evenly as possible.

## Time Complexity

Merge sort takes `O(n log n)` time. The final alternating assignment takes
`O(n)`, so the total is `O(n log n)`.

## Space Complexity

The merge-sort slices and temporary merged lists use `O(n)` extra space.

## Design Choice

Sorting is necessary because digit position determines place value. Putting
larger digits first and alternating them gives the largest digits the most
valuable positions while keeping the two numbers' lengths balanced. Merge sort
was chosen because the problem forbids Python's built-in sorting function and
requires `O(n log n)` time.
