# leetcode
# ref https://www.youtube.com/watch?v=Zb4eRjuPHbM


'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        # base case
        if len(nums) == 1 and nums[0] == 0:
            return True
        
        if nums[0] == 0:
            return False
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i] >= target:
                target = i
                
        return target == 0
    
    
