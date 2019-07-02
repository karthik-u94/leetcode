class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        def find_largest_value_smaller_than_target(array, target, low, high):
            start = low
            while low <= high:
                mid = low + (high-low) // 2
                if array[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            return array[high] if high >= start else None
        
        res = -1
        A.sort()
        for i, val1 in enumerate(A):
            target = K - val1
            val2 = find_largest_value_smaller_than_target(A, target, i + 1, len(A) - 1)
            if val2 is not None and res < val1 + val2:
                res = val1 + val2
        return res
