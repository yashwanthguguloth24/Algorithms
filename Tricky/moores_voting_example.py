'''
Leetcode
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = None
        ele_count = 0
        for i in range(len(nums)):
            if ele_count == 0:
                ele = nums[i]            
            if nums[i] == ele:
                ele_count += 1
            else:
                ele_count -= 1
        return ele
