class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s += ' '
        word = ''
        sizes = []
        for c in s:
            is_space = c == ' '
            if not is_space:
                word += c
            elif is_space and len(word) > 0:
                sizes.append(len(word))
                word = ''

        return sizes[len(sizes)-1]