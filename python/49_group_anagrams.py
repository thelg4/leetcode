class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # hold the lists of anagrams
        groups = {}

        # loop through the words
        for word in strs:

            # empty count for each word
            count = [0] * 26

            # count the indicies of the characters
            for char in word:
                index = ord(char) - ord('a')
                count[index] += 1

            # make that the key
            key = tuple(count)

            # if not similar key, add it
            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
