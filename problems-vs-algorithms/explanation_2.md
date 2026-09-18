## Approach

I used a modified binary search. At every iteration, either the left half or
the right half is still sorted. I check whether the target lies inside that
sorted half; if it does, I search there, otherwise I discard it and search the
other half.

## Time Complexity

Only one half of the array is considered after each iteration, so the runtime
is `O(log n)`.

## Space Complexity

The search uses only boundary variables and therefore takes `O(1)` extra space.

## Design Choice

The rotation preserves a sorted half at every midpoint. That property allows
binary search to discard half the search space just as it does for a normally
sorted array, while a linear scan would ignore this useful structure.
