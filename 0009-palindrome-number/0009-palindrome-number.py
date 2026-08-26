class Solution:
    def isPalindrome(self, x: int) -> bool:
        # less then 0
        if x < 0:
            return False

        if x >= 0 and x < 10:
            return True

        # split number
        # 121 => [1, 2, 1]
        # 100 + 20 + 1
        # 1 * 100 + 2 * 10 + 1 * 1

        factor: int = 10

        parts: List[int] = []
        while True:
            part = x % factor
            parts.append(part)
            
            if part == x:
                break
            else:
                factor *= 10

        # subtract parts numbers
        i = len(parts) - 1

        while i > 0:
            parts[i] -= parts[i - 1]
            i -= 1
            
        # convert to single numbers
        factor = 1
        numbers: List[int] = []
        for part in parts:
            number: int = int(part / factor)
            numbers.append(number)
            factor *= 10

        palindrome = False

        i: int = 0
        j: int = len(numbers) - 1

        while i < j:
            if numbers[i] != numbers[j]:
                palindrome = False
                break
            else:
                palindrome = True   
                i += 1
                j -= 1

        return palindrome