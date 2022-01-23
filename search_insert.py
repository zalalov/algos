class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def _search_insert(start, stop):
            _nums = nums[start:stop]
            
            if not len(_nums):
                return start
            
            if len(_nums) == 1:
                if _nums[0] == target:
                    return start
                elif _nums[0] < target:
                    return start + 1
                elif start == 0:
                    return 0
                else:
                    return start - 1
            else:
                middle_index = start + ((stop - start) // 2)                
                middle_value = nums[middle_index]
                
                if middle_value == target:
                    return middle_index
                
                if middle_value < target:
                    return _search_insert(middle_index, stop)
                else:
                    return _search_insert(start, middle_index)
                
        return _search_insert(0, len(nums))
