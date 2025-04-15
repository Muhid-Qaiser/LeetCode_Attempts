class Solution
{
public:
    int strStr(string haystack, string needle)
    {
        bool flag = false;
        int idx = 0;
        for (int i = 0; i < haystack.size(); i++)
        {
            if (haystack[i] == needle[0])
            {
                flag = true;
                idx = i + 1;
                for (int j = 1; j < needle.size(); j++)
                {
                    if (haystack[idx] != needle[j])
                    {
                        flag = false;
                        break;
                    }
                    idx++;
                }
            }
            if (flag)
                return i;
        }
        return -1;
    }
};