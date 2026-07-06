class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
       
	# count of the number of intervals that survive 
        count = 0
	# keeps track of the farthest right endpoint we've seen so far
        max_end = 0

	# sort the intervals in ascending order
        intervals.sort(key=lambda x: (x[0], -x[1]))

	
        for start, end in intervals:
        # if the current end is larger than the max end, we add that to the count of intervals that survive
	    if end > max_end:
                count += 1
                max_end = end

        return count
