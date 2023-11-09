#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,nums,N):
        ##Your code here
        max_sum=min(nums)
        curr_sum=0
        for i in range(len(nums)):
            curr_sum+=nums[i]
            if nums[i]>curr_sum:
                curr_sum=nums[i]
            if max_sum<curr_sum:
                max_sum=curr_sum
        return max_sum
            


