class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        
        counts = {}

        for char in text:
            counts[char] = counts.get(char, 0) + 1

        target = 'balloon'

        return min(
            counts.get(char, 0) // target.count(char) for char in target
        )
