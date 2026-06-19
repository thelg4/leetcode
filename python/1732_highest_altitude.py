class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        start = 0
        highest = 0

        for g in gain:
            start += g

            if start > highest:
                highest = start

        return highest
        
