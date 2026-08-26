class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        fst_index: int = 0
        snd_index: int = 1
        
        if len(nums) < 2:
            return []
        
        if len(nums) == 2:
            return [fst_index, snd_index]
                   
        while snd_index <= len(nums):
            
            if snd_index >= len(nums):
                fst_index += 1
                snd_index = fst_index + 1    
            
            if nums[fst_index] + nums[snd_index] == target:
                break
            else:
                snd_index += 1

        return [fst_index, snd_index]