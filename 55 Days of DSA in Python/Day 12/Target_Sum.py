def findTargetSumWays(nums, target):
    n = len(nums)
    summation = sum(nums)
    dp = [[None]*(2*summation+1) for _ in range(n)]

    def helper(index,sum_nums):
        #base case
        if index<0:
            if sum_nums==target:return 1
            else:return 0
        if dp[index][sum_nums+summation]!=None:return dp[index][sum_nums+summation]

        negative = helper(index-1,sum_nums+-1*nums[index])
        positive = helper(index-1,sum_nums+nums[index])    
        dp[index][sum_nums+summation] = negative+positive
        return dp[index][sum_nums+summation]
    return helper(n-1,0) 
