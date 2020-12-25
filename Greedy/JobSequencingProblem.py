'''
Given a set of N jobs where each job i has a deadline and profit associated to it. Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit if and only if the job is completed by its deadline. The task is to find the maximum profit and the number of jobs done.

Input Format:

Jobs will be given in the form (Job id, Deadline, Profit) associated to that Job.

Example 1:

Input:
N = 4
Jobs = (1,4,20)(2,1,10)(3,1,40)(4,1,30)
Output: 2 60
Explanation: 2 jobs can be done with
maximum profit of 60 (20+40).

'''

# code by yashwanth

def JobScheduling(Jobs,n):
    '''
    :param Jobs: list of "Job" class defined in driver code, with "profit" and "deadline".
    :param n: total number of jobs
    :return: A list of size 2 having list[0] = count of jobs and list[1] = max profit
    '''
    '''
    {
        class Job:.
        def __init__(self,profit=0,deadline=0):
            self.profit = profit
            self.deadline = deadline
            self.id = 0
    }
    '''
    profit = 0
    slots = [False]*n
    Jobs = sorted(Jobs,key = lambda x : x.profit,reverse = True)
    for i in range(n):
        for j in range(min(n,Jobs[i].deadline)-1,-1,-1):
            if slots[j] == False:
                slots[j] = True
                profit += Jobs[i].profit
                break
    num_jobs = 0
    for k in range(n):
        if slots[k]:
            num_jobs += 1
            
    res = [num_jobs,profit]
    return res
    
    
