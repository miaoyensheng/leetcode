def LongestPalindromicSequence(input_string, front_pointer, back_pointer):
    if front_pointer > back_pointer:
        return 0
    elif front_pointer == back_pointer:
        return 1
    else:

        lps1 = 0

        if input_string[front_pointer] == input_string[back_pointer]:
            lps1 = 2 + LongestPalindromicSequence(input_string, front_pointer + 1, back_pointer - 1)
        
        lps2 = LongestPalindromicSequence(input_string, front_pointer + 1, back_pointer)
        lps3 = LongestPalindromicSequence(input_string, front_pointer, back_pointer - 1)

        return max(lps1, lps2, lps3)

input_string = "MANABAVACCCLAKAJAHA"

print(LongestPalindromicSequence(input_string, 0, len(input_string)-1))