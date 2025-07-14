class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        
        hashmap = dict()
        hashmap[keysPressed[0]] = releaseTimes[0]
        press_time = releaseTimes[0]
        res = keysPressed[0]

        for i in range(1, len(releaseTimes)):
            time = releaseTimes[i] - releaseTimes[i - 1]
            hashmap[keysPressed[i]] = time + hashmap.get(keysPressed[i], 0)
            if time >= press_time:
                if time == press_time:
                    res = max(res, keysPressed[i])
                else:
                    res = keysPressed[i]    
                press_time = time

        print(hashmap)

        return res
    
# Time - O(N)
# Space - O(1)