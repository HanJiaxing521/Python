class Solution(object):
    def backtrack(self, rtlist, templist, nums):
        if len(templist) == len(nums):
            rtlist.append(templist[:])
        else:
            for i in nums:
                if i in templist:
                    continue
                templist.append(i)
                self.backtrack(rtlist, templist, nums)
                templist.pop()

    def permute(self, nums):
        rtlist = []
        templist = []
        self.backtrack(rtlist, templist, nums)
        return rtlist


list = Solution()
list = list.permute([1, 2, 3, 4])
print(list)
