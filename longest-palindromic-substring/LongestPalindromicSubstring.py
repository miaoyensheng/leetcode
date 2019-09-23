def LongestPalindromicSubstring(input_string, front_pointer, back_pointer):

    if front_pointer > back_pointer:
        return 0
    elif front_pointer == back_pointer:
        return 1

    else: 

        lps1 = 0

        if input_string[front_pointer] == input_string[back_pointer]:

            remainingLength = back_pointer - front_pointer - 1
            lps1 = LongestPalindromicSubstring(input_string, front_pointer + 1, back_pointer - 1)

            if  lps1 == remainingLength:
                lps1 = 2 + remainingLength

        lps2=LongestPalindromicSubstring(input_string, front_pointer + 1, back_pointer)
        lps3=LongestPalindromicSubstring(input_string, front_pointer, back_pointer - 1)

        return max(lps1, lps2, lps3)


input_string = "MMMMAAAAMMMM"
print(LongestPalindromicSubstring(input_string, 0, len(input_string)-1))