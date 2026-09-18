## Approach

I used the Dutch National Flag algorithm with three pointers: `low` marks the
next position for a zero, `mid` examines the current value, and `high` marks
the next position for a two. Zeros and twos are swapped into their regions,
while ones remain in the middle.

## Time Complexity

Each element is processed a constant number of times, so the runtime is
`O(n)`.

## Space Complexity

The array is rearranged in place and only three pointers are used, so extra
space is `O(1)`.

## Design Choice

The three-pointer swap approach was chosen over counting values and writing
them back because it performs the required single traversal and does not need a
second pass to rebuild the array.
