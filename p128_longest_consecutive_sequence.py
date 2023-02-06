class Solution:
    def longestConsecutive(self, nums):
        longest = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                curr_num = num
                curr_len = 1

                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_len += 1

                longest = max(longest, curr_len)

        return longest