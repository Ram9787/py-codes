Shortest Unsorted Continuous Subarray in Python
class Solution(object):
   def findUnsortedSubarray(self, nums):
      res = sorted(nums)
      ans = 0
      r = []
      for i in range(len(res)):
         if nums[i] != res[i]:
            r.append(i)
         if not len(r):
            return 0
         if len(r) == 1:
            return 1
         return r[-1]-r[0]+1
ob1 = Solution()
print(ob1.findUnsortedSubarray([2,6,4,8,10,9,15]))
