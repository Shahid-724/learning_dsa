class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        
        one_step_before = 0
        two_step_before = 0

        for i in range(2, len(cost) + 1):

            one_step = one_step_before + cost[i - 1]
            two_step = two_step_before + cost[i - 2]

            two_step_before = one_step_before
            one_step_before = min(one_step, two_step)

        return one_step_before
    
# Time - O(N)
# Space - O(1)