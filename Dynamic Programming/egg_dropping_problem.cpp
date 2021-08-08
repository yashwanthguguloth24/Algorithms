// https://practice.geeksforgeeks.org/problems/egg-dropping-puzzle-1587115620/1#
// https://www.youtube.com/watch?v=UvksR0hR9nA

// Reducing it into smaller sub problems dp[i][j] - min moves for i eggs and j floors 


class Solution
{
    public:
    //Function to find minimum number of attempts needed in 
    //order to find the critical floor.
    int eggDrop(int n, int k) 
    {
        vector<vector<int>> dp(n+1,vector<int> (k+1,0));
        for(int i = 1;i<=n;i++)
        {
            for(int j = 1;j<=k;j++)
            {
                if(i == 1)
                {
                    dp[i][j] = j;
                }
                else if(j == 1)
                {
                    dp[i][j] = 1;
                }
                else
                {
                    int min_val = INT_MAX;
                    int pf = 0;
                    for(int cf = j-1;cf>=0;cf--,pf++)
                    {
                        int v1 = dp[i-1][pf];
                        int v2 = dp[i][cf];
                        int val = max(v1,v2);
                        min_val = min(min_val,val);
                    }
                    dp[i][j] = min_val+1;
                }
            }
        }
        
        return dp[n][k];
        
    }
};
