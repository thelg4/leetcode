class Solution(object):
    def topKFrequent(self, nums, k):
        counts = {}

        for num in nums:
            if num not in counts:
                counts[num] = 0

            counts[num] += 1

        sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)

        result = []

        for i in range(k):
            result.append(sorted_counts[i][0])

        return result
