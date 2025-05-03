class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        word, temp = "", ""
        i = 0

        if str1 + str2 != str2 + str1:
            return ""

        for i in range(min( len(str1), len(str2) )):
            if str1[i] == str2[i]:
                temp += str1[i]
            
                if len(str1) % len(temp) == 0 and len(str2) % len(temp) == 0:
                    word = temp
            else:
                word, temp = "", ""
                break

        if len(str1) > len(str2):
            k = 0
            for j in range(i+1, len(str1)):
                if str1[j] != str2[k]:
                    word, temp = "", ""
                k = (k+1) % len(str2)

        # if len(str1) > len(str2):
        #     j = 0
        #     for i in range( len(str1) ):
        #         if str1[i] == str2[j]:
        #             temp += str1[i]

        #             if len(str1) % len(temp) == 0 and len(str2) % len(temp) == 0:
        #                 word = temp

        #         else:
        #             word, temp = "", ""
        #             break
        #         j = (j + 1) % len(str2)
        # else:
        #     j = 0
        #     for i in range( len(str2) ):
        #         if str2[i] == str1[j]:
        #             temp += str2[i]

        #             if len(str1) % len(temp) == 0 and len(str2) % len(temp) == 0:
        #                 word = temp

        #         else:
        #             word, temp = "", ""
        #             break
        #         j = (j + 1) % len(str1)

        

                

        return word
                    

        