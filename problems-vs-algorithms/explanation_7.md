## Approach

I used a trie whose edges represent path parts separated by slashes. Adding a
route follows or creates one node per path part and stores the handler at the
final node. Lookup splits the requested path, ignores empty parts from leading
or trailing slashes, and follows the matching nodes.

## Time Complexity

For a path with `p` parts, insertion and lookup take `O(p)` time. Splitting the
path also takes time proportional to its length.

## Space Complexity

The trie uses `O(n)` space for the total number of distinct stored path parts.

## Design Choice

A path-part trie is useful because related routes share their common prefixes,
and lookup work depends on the number of path parts rather than scanning every
registered route. A flat dictionary can provide exact matches, but it does not
represent the route hierarchy as directly and makes shared path structure less
useful.
