class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if self.freq(st=s) == self.freq(st=t):
            return True
        return False


    def freq(self, st: str) -> dict:
        hashh = {}
        for i in st:
            if i in hashh.keys():
                hashh[i] = hashh[i]+1
            else:
                hashh[i]=1

        return hashh


        