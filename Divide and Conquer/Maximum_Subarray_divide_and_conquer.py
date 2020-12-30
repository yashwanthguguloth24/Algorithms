'''
Leetcode: https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-2147483647]
Output: -2147483647

'''

class Solution:
    def CrossingSum(self,nums,l,m,h):
        s=0
        left_sum = float('-inf')
        for i in range(m,l-1,-1):
            s += nums[i]
            if s > left_sum:
                left_sum = s
                
        s=0
        right_sum = float('-inf')
        for i in range(m+1,h+1):
            s += nums[i]
            if s > right_sum:
                right_sum = s       
                
        return max(left_sum+right_sum,left_sum,right_sum)
                
            
    
    def SubarraySum(self,nums,l,h):
        if l == h:
            return nums[l]
        
        mid = (l+h)//2
        return max(self.SubarraySum(nums,l,mid),self.SubarraySum(nums,mid+1,h),self.CrossingSum(nums,l,mid,h))
            
    
    
    def maxSubArray(self, nums: List[int]) -> int:
        ans = self.SubarraySum(nums,0,len(nums)-1)
        return ans
        
        

