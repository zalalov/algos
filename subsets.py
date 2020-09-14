def subsets(nums):
        length = len(nums)
        result = []
        
        for i in range(1<<length):
            mask = bin(i)[2:].zfill(length)
            subset = []
            
            for k, j in enumerate(mask):
                if j == '1':
                    subset.append(nums[k])
                    
            result.append(subset)
            
        return result

print(subsets([1,2,3]))
print(subsets([4,5,6]))
