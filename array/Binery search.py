#User function template for Python
class Solution:    
    def binarysearch(self, arr, n, k):
        # code here
        s=0
        e=len(arr)-1
        
        while s <= e:
 
            mid = s + (e - s) // 2
            if arr[mid] == k:
                return mid
    
            elif arr[mid] < k:
                s = mid + 1
 
            else:
                e = mid - 1
 
        return -1
    
s=Solution()
arr=[2,3,4,7]
s.binarysearch(arr,4,4)