'''

You are given two arrays: deadline[], and profit[], which represent a set of jobs, where each job is associated with a deadline, and a profit. Each job takes 1 unit of time to complete, and only one job can be scheduled at a time. You will earn the profit associated with a job only if it is completed by its deadline.

Your task is to find:

The maximum number of jobs that can be completed within their deadlines.
The total maximum profit earned by completing those jobs.
Examples :

Input: deadline[] = [4, 1, 1, 1], profit[] = [20, 10, 40, 30]
Output: [2, 60]
Explanation: Job1 and Job3 can be done with maximum profit of 60 (20+40).
Input: deadline[] = [2, 1, 2, 1, 1], profit[] = [100, 19, 27, 25, 15]
Output: [2, 127]
Explanation: Job1 and Job3 can be done with maximum profit of 127 (100+27).
Input: deadline[] = [3, 1, 2, 2], profit[] = [50, 10, 20, 30]
Output: [3, 100]
Explanation: Job1, Job3 and Job4 can be completed with a maximum profit of 100 (50 + 20 + 30).
Constraints:
1 ≤ deadline.size() == profit.size() ≤ 105
1 ≤ deadline[i] ≤ deadline.size()
1 ≤ profit[i] ≤ 500



'''
class Solution:
        def jobSequencing(self, deadline:list[int], profit:list[int]):
            n=len(deadline)
            jobs=[[deadline[i],profit[i]] for i in range(n)]
            max_day=max(deadline)
            jobs.sort(reverse=True,key=lambda x:x[1])
            days=[-1]*(max_day+1)
            count=total_profit=0 
            for i in range(n):
                flag=False 
                for j in range(jobs[i][0],0,-1):
                    if days[j]!=-1:
                        continue 
                    days[j]=i 
                    flag=True 
                    break 
                if flag:
                    count+=1
                    total_profit+=jobs[i][1]
            return [count,total_profit]
class Solution:
    def jobSequencing(self, deadline:list[int], profit:list[int]):
        jobs=sorted(zip(deadline,profit),reverse=True,key=lambda x:x[1])
        max_day=max(deadline)
        days=list(range(max_day+2))
        def find(day):
            if days[day]==day:
                return day 
            days[day]=find(days[day])
            return days[day]
        count=total_profit=0
        for day,pr in jobs:
            alternative_days=find(day)
            if alternative_days>0:
                count+=1
                total_profit+=pr 
                days[alternative_days]=find(alternative_days-1)
        return [count,total_profit]        

      
class TestApp:
      def testing_case_one(self):
          assert Solution().jobSequencing([4, 1, 1, 1],[20, 10, 40, 30])==[2,60]
      def testing_case_two(self):
          assert Solution().jobSequencing([2, 1, 2, 1, 1],[100, 19, 27, 25, 15])==[2,127]
      def testing_case_three(self):
          assert Solution().jobSequencing([3, 1, 2, 2],[50, 10, 20, 30])==[3,100]     