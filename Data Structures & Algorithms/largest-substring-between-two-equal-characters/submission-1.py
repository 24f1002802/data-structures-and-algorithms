class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        max_len = -1

        for i ,ch in enumerate(s):
            if ch in first:
                length =  i - first[ch]-1
                max_len = max(max_len, length)

            else:
                first[ch] = i
        return max_len
        