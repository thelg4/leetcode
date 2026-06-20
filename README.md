# LeetCode



My solutions to LeetCode problems, written in Python.

## Structure

Solutions live in [`python/`](python/), one file per problem. Files are named `<problem-number>_<problem-slug>.py` and contain a `Solution` class matching LeetCode's expected signature.

## Solutions

| # | Problem | Topic |
|---|---------|-------|
| 49 | [Group Anagrams](python/49_group_anagrams.py) | Hash Map |
| 217 | [Contains Duplicate](python/217_contains_duplicate.py) | Hash Set |
| 242 | [Valid Anagram](python/242_valid_anagram.py) | Hash Map |
| 347 | [Top K Frequent Elements](python/347_top_k_frequent_elements.py) | Hash Map, Sorting |
| 1732 | [Find the Highest Altitude](python/1732_highest_altitude.py) | Prefix Sum |

## Running

Each file defines a standalone `Solution` class. To try one out:

```python
from python.group_anagrams import Solution  # adjust import to the file

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
```

Or paste the solution directly into the LeetCode editor for the corresponding problem.
