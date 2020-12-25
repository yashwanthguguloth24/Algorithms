'''
Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item. 

 

Example 1:

Input:
N = 3, W = 50
values[] = {60,100,120}
weight[] = {10,20,30}
Output: 240.00
Explanation: Total maximum value of item
we can have is 240.00 from the given
capacity of sack. 
'''

# Greedy approach

def fractionalknapsack(W,Items,n):
    '''
    :param W: max weight which can be stored
    :param Items: List contianing Item class objects as defined in driver code, with value and weight
    :param n: size of Items
    :return: Float value of max possible value, two decimal place accuracy is expected by driver code
    
    {
        class Item:
        def __init__(self,val,w):
            self.value = val
            self.weight = w
    }
    '''
    # to get max total
    # greedy approach
    Items = sorted(Items,key = lambda x:(x.value/x.weight),reverse = True)
    tot_val = 0
    i = 0

    while i < n:
        if W == 0:
            return tot_val
        
        a = min(Items[i].weight,W)
        tot_val += a*(Items[i].value/Items[i].weight)
        W = W - a
        i += 1
        
    return tot_val
        



