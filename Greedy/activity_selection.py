'''
Given N activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.

Note : The start time and end time of two activities may coincide.

Example 1:

Input:
N = 5
start[] = {1,3,2,5,8,5}
end[] = {2,4,6,7,9,9}
Output: 4
Explanation:Perform the activites 1,2,4,5
'''


def maximumActivities(n,start,end):
    '''
    :param n: number of activities
    :param start: start time of activities
    :param end: corresponding end time of activities
    :return: Integer, maximum number of activities
    '''
    tab = []
    for i in range(n):
        tab.append([start[i],end[i]])
    tab = sorted(tab,key = lambda x : x[1])
    num = 0
    curr = -1
    i = 0
    while i < n:
        if curr <= tab[i][0]:
            num += 1
            curr = tab[i][1]
        i += 1
    return num
