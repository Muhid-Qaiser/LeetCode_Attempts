class Solution {
public:
    int lengthOfLastWord(string s) {

        int n = s.size(), count = 0;
        bool flag = false;

        for(int i=n-1; i>=0; i--)
        {
            if ( !flag && s[i] == ' ' )
                continue;
            else if ( s[i] != ' ' )
            {
                count++;
                flag = true;
            }
            else if (flag && s[i] == ' ')
                break;
        }
        return count;
    }
};