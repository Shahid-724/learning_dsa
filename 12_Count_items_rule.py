class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        
        hashmap = {'type': 0, 'color': 1, 'name': 2}

        count = 0

        for item in items:
            if item[hashmap[ruleKey]] == ruleValue:
                count += 1

        return count
    
# Time - O(N)
# Space - O(1)