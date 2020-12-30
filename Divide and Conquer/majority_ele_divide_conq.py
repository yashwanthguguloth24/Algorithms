'''
Divide and conquer approach
O(nlogn) -- time
O(nlogn) -- space

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
    def MajorityElement(self,nums,low,high):
        if low == high:
            return nums[low]
        
        mid = low + (high-low)//2
        left = self.MajorityElement(nums,low,mid)
        right = self.MajorityElement(nums,mid+1,high)
        
        if left == right:
            return left
        
        left_count = 0
        right_count = 0
        for i in range(low,high+1):
            if nums[i] == left:
                left_count += 1
            elif nums[i] == right:
                right_count += 1
                
        if left_count > right_count:
            return left
        else:
            return right

    
    
    def majorityElement(self, nums: List[int]) -> int:
        return self.MajorityElement(nums,0,len(nums)-1)
        
        
        
