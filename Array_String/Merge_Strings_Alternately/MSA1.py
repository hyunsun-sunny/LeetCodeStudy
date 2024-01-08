class Solution(object):
    def mergeAlternately(self, word1, word2):
        len1 = len(word1)
        len2 = len(word2)
        flag = 0
        if len1 > len2:
            short_len = len2
            flag = 1
        elif len1 == len2:
            short_len = len1
        else:
            short_len = len1
            flag = 2
        result = ''
        for i in range(short_len):
            result += word1[i]
            result += word2[i]

        if flag ==1:
            result = result + word1[-(len1-len2):]
        elif flag == 2:
            result = result + word2[-(len2-len1):]
        return result
