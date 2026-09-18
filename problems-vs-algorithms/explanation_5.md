## Approach

I used a trie where each node stores a character and links to its child
characters. Inserting a word creates or follows one node per character.
Finding a prefix follows those same links, and `suffixes` recursively visits
the matching node's descendants to collect complete words.

## Time Complexity

Inserting or finding a word or prefix of length `p` takes `O(p)`. Collecting
suffixes takes `O(k)` in proportion to the characters visited in the matching
subtree.

## Space Complexity

The trie stores one node per stored character, requiring `O(n)` space for `n`
stored characters. The recursive suffix collection also uses stack space
proportional to the longest suffix.

## Design Choice

A trie is a good fit for autocomplete because prefix lookup follows only the
prefix characters. A list would require checking every stored word and
filtering it, while the trie immediately reaches the relevant subtree.
