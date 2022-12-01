from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        digits = digits[::-1]
        i = 0

        while carry:
            if i < len(digits):
                tmp = digits[i] + carry
                digits[i] = tmp % 10
                carry = tmp // 10
                i += 1
            else:
                digits.append(carry)
                break

        return digits[::-1]


s = Solution()
print(s.plusOne([9]))
