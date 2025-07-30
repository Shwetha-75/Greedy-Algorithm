'''

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].

'''

import sys
class Solution:
    def jump(self, nums: list[int]) -> int:
        n=len(nums)
        def helper(index,jumps):
            if index>=n-1:
                return jumps
            min_index=sys.maxsize 
            for i in range(1,nums[index]+1):
                min_index=min(min_index,helper(index+i,jumps+1))
            return min_index
        return helper(0,0)
class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps=left=right=0
        n=len(nums)
        while right<n-1:
              farthest=0
              for i in range(left,right+1):
                  farthest=max(farthest,i+nums[i])
              jumps+=1
              left=right+1
              right=farthest 
        return jumps 
            

class TestApp:
      def testing_case_one(self):
          assert Solution().jump([2,3,1,1,4])==2
      def testing_case_two(self):
          assert Solution().jump([2,3,0,1,4])==2