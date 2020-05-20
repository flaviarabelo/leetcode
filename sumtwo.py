class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c={}
        for i, a  in enumerate(nums):
            c[a] = i
            
        for j, b in enumerate(nums):
            complement = target -b
           
            if complement in c and c[complement] != None and c[complement] != j:
                return [j,c[complement]]
        return [-1,-1]
    
