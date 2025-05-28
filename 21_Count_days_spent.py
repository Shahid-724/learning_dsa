class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        
        days = [0] * 366
        res = 0

        months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

        alice_month = int(arriveAlice[:2]) - 1
        arrive_alice = months[alice_month] + int(arriveAlice[3:])

        alice_month = int(leaveAlice[:2]) - 1
        leave_alice = months[alice_month] + int(leaveAlice[3:])

        bob_month = int(arriveBob[:2]) - 1
        arrive_bob = months[bob_month] + int(arriveBob[3:])

        bob_month = int(leaveBob[:2]) - 1
        leave_bob = months[bob_month] + int(leaveBob[3:])

        for i in range(arrive_alice, leave_alice + 1):
            days[i] += 1

        for i in range(arrive_bob, leave_bob + 1):
            days[i] += 1
            if days[i] == 2:
                res += 1
                
        return res
    
# Time - O(1)
# Space - O(1)