'''

Reference:https://www.geeksforgeeks.org/smallest-number-k-product-digits-k-equal-n/


Given a number N, find the smallest number K, such that product of digits of K is equal to N.

Input:
First line of input contains number of testcases T. For each testcase, there will be a single line containing N.

Output:
For each testcase, print K. If K is not possible, print -1.
 

Your Task: 
Your task is to complete the function smallestK() which takes the value N as input parameter and return the value K.
 

Constraints:
1 <= T <= 105
1 <= N <= 1015
 

Example:
Input:
2
12
5

Output:
26
5

Explanation:
Testcase 1: 26 is the smallest number, and product of 2 and 6 is 12.
Testcase 2: 5 is the smallest number which is itself equal to 5.
'''

def smallestK(n):
    if (n >= 0 and n <= 9): 
        return n 

    digits = [] 
    for i in range(9,1, -1): 
      
        while (n % i == 0): 
            digits.append(i) 
            n = n //i 
          
 
    if (n != 1): 
        return -1
  
    k = 0
    while (len(digits) != 0): 
      
        k = k * 10 + digits[-1] 
        digits.pop() 

    return k 



