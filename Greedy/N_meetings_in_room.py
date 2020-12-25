'''
GFG Prob : https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1#

There is one meeting room in a firm. There are N meetings in the form of (S[i], F[i]) where S[i] is start time of meeting i and F[i] is finish time of meeting i.

What is the maximum number of meetings that can be accommodated in the meeting room? Also note start time of one chosen meeting can't be equal to the end time of the other chosen meeting.

Example 1:

Input:
N = 6
S[] = {1,3,0,5,8,5}
F[] = {2,4,6,7,9,9}
Output: 1 2 4 5
Explanation: Four meetings can held with
given start and end timings.
Example 2:

Input:
N = 8
S[] = {75250,50074,43659,8931,11273,
27545,50879,77924}
F[] = {112960,114515,81825,93424,
54316,35533,73383,160252}
Output: 6 7 1
Explanation: Only three meetings can held
with given start and end timings.
'''

# Greedy Implementation

def maximumMeetings(n,start,end):
    '''
    :param n: number of activities
    :param start: start time of activities
    :param end: corresponding end time of activities
    :return: Integer, maximum number of activities
    '''
    schedule = []
    for i in range(n):
        schedule.append([start[i],end[i],i])
        
    schedule = sorted(schedule,key = lambda x:x[1])
    
    meetings = []
    curr_time = -1
    i = 0
    while i < n:
        if curr_time < schedule[i][0]:
            meetings.append(schedule[i][2]+1)
            curr_time = schedule[i][1]
        i += 1
    print(*meetings)




