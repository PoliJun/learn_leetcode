class Solution:
    '''
    use stack
    input: s: string
    output: ans: string
    -----
    create a char_list = []
    add characters from the end of s: string to the char_list:
        if the character is * , then  not add star and the left non-star char.
    return char_list.toString
    '''
    def removeStars(self, s: str) -> str:

        n = len(s)
        s_list = list()
        i = n-1
        while i >=0:
            if s[i] != "*":
                s_list.append(s[i])
            else:
                for j in reversed(range(i)):
                    if s[j] != "*":
                        i -= 2*(i-j)
                        if i < 0:
                            return "".join(reversed(s_list))
                        s_list.append(s[i])
        return "".join(reversed(s_list))
                
