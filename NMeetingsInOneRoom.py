'''

You are given timings of n meetings in the form of (start[i], end[i]) where start[i] is the start time of meeting i and end[i] is the finish time of meeting i. Return the maximum number of meetings that can be accommodated in a single meeting room, when only one meeting can be held in the meeting room at a particular time. 

Note: The start time of one chosen meeting can't be equal to the end time of the other chosen meeting.

Examples :

Input: start[] = [1, 3, 0, 5, 8, 5], end[] =  [2, 4, 6, 7, 9, 9]
Output: 4
Explanation: Maximum four meetings can be held with given start and end timings. The meetings are - (1, 2), (3, 4), (5,7) and (8,9)
Input: start[] = [10, 12, 20], end[] = [20, 25, 30]
Output: 1
Explanation: Only one meetings can be held with given start and end timings.
Input: start[] = [1, 2], end[] = [100, 99]
Output: 1
Constraints:
1 ≤ n ≤ 105
0 ≤ start[i] < end[i] ≤ 106

'''

class Solution:
      def maximumMeetings(self,start:list[int],end:list[int]): 
          meetings=sorted(zip(start,end),key=lambda x:x[1])
          count,ending_time=1,meetings[0][1]
          for i in range(1,len(meetings)):
              if ending_time<meetings[i][0]:
                  count+=1
                  ending_time=meetings[i][1]
          return count 
class TestApp:
      def testing_case_one(self):
          assert Solution().maximumMeetings([1, 3, 0, 5, 8, 5],[2, 4, 6, 7, 9, 9])==4 
      def testing_case_two(self):
          assert Solution().maximumMeetings([10, 12, 20],[20, 25, 30])==1
      def testing_case_three(self):
          assert Solution().maximumMeetings([1,2],[100,99])==1
          
          