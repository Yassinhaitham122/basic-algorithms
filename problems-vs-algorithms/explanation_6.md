## Approach

I scan the array once while maintaining two variables: the smallest value seen
so far and the largest value seen so far. Each new integer updates one or both
variables when necessary.

## Time Complexity

Every element is inspected once, so the runtime is `O(n)`.

## Space Complexity

Only two tracking variables are added, so the extra space is `O(1)`.

## Design Choice

A single pass is preferable to sorting because sorting would take `O(n log n)`
time even though only the two extremes are needed. The tracking approach also
does not reorder or copy the input list.
