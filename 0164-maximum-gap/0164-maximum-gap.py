class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        
        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0
        
        # Bucket sort (pigeonhole approach): distribute numbers into n-1
        # buckets sized so that the max possible gap WITHIN a bucket is
        # smaller than the true maximum gap must be. This guarantees
        # the answer is always found BETWEEN buckets, never inside one.
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        bucket_min = [float('inf')] * bucket_count
        bucket_max = [float('-inf')] * bucket_count
        
        for num in nums:
            idx = (num - min_val) // bucket_size
            bucket_min[idx] = min(bucket_min[idx], num)
            bucket_max[idx] = max(bucket_max[idx], num)
        
        # Walk buckets left to right; max gap is between a bucket's max
        # and the NEXT non-empty bucket's min (gaps inside a bucket
        # are provably smaller than this, by the pigeonhole principle)
        max_gap = 0
        prev_max = bucket_min[0]  # min_val, effectively
        
        for i in range(bucket_count):
            if bucket_min[i] == float('inf'):
                continue  # empty bucket, skip
            
            max_gap = max(max_gap, bucket_min[i] - prev_max)
            prev_max = bucket_max[i]
        
        return max_gap