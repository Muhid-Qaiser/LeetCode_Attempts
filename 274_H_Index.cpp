class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size(), res=0, count=0;

        for (int i=0; i<=n; i++)
        {
            count = 0;
            for (int j=0; j<n; j++)
            {
                if ( citations[j] >= i )
                    count++;
            }

            if (count >= i) 
                res = i;
            else
                break;
        }

        return res;

    }
};