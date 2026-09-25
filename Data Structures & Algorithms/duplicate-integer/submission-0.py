class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashh = {}
        for i in nums:
            if i in hashh.keys():
                hashh[i] = hashh[i] + 1
            else :
                hashh[i] = 1

        for j in hashh.values():
            if j>1:
                return True
        return False

        