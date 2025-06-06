class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        
        if purchaseAmount % 10 == 0:
            return 100 - purchaseAmount

        rounded_amount = purchaseAmount // 10
        round_dir = purchaseAmount % 10
        if round_dir >= 5:
            rounded_amount += 1

        return 100 - rounded_amount * 10
    
# Time - O(1)
# Space - O(1)