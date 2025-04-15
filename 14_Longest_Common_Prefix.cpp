class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = getMinStr(strs);
        int n = strs.size(), min_len = prefix.size();
        bool flag = true;

        for (int i=0; i<n; i++)
        {
            flag = true;
            for(int j=0; j<strs[i].size() &&  j < prefix.size(); j++)
            {
                if ( prefix == strs[i])
                    break;
                else if (!flag)
                    min_len--;
                else if ( prefix[j] != strs[i][j])
                {
                    min_len--;
                    flag = false;
                }
            }
        min_len = ( min_len >= 0 ) ? min_len : 0;
        prefix.resize(min_len);
        }

        return prefix;
    }

    string getMinStr(vector<string> strs)
    {
        int min_val = INT_MAX;
        string res = "";

        for(int i=0; i<strs.size(); i++)
        {
            if (min_val > strs[i].size())
            {
                min_val = strs[i].size();
                res = strs[i];
            }
        }

        return res;

    }

};