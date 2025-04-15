class Solution {
public:
    int romanToInt(string s) {
        int num = 0, total = 0, nextNum = 0;

        for (int i=0; i<s.size(); i++)
        {
            num = getInt(s[i]);

            if (i <= s.size() - 2)
            {
                nextNum = getInt(s[i+1]);
                if (nextNum > num)
                {
                    num = nextNum - num ;
                    i++;
                }
            }
            total += num;
        }
        return total;
    }

    int getInt(char c)
    {
        if (c == 'I')
            return 1;
        else if (c == 'V')
            return 5;
        else if (c == 'X')
            return 10;
        else if (c == 'L')
            return 50;
        else if (c == 'C')
            return 100;
        else if (c == 'D')
            return 500;
        else if (c == 'M')
            return 1000;
        else
            return 0;
    }

};