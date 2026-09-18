## Approach

I used binary search to find the floor of the square root. The square of a
candidate increases as the candidate increases, so each comparison tells us
which half of the remaining range can be discarded. When the exact square is
not found, the right boundary is the largest integer whose square is below the
input.

## Time Complexity

The search range is cut in half on every iteration, so the runtime is
`O(log n)`.

## Space Complexity

The algorithm uses a fixed number of variables, so the extra space is `O(1)`.

## Design Choice

Binary search is a better fit than scanning upward from zero because the
monotonic relationship between an integer and its square makes half of the
possibilities unnecessary after every comparison.
