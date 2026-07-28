import itertools
class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []   
        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        pools = [phone[d] for d in digits]
        return ["".join(p) for p in itertools.product(*pools)]
