class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int max_val = 0, min_val = INT_MAX, n = prices.size();

        for (int i = 0; i < n; i++)
        {
            if (min_val > prices[i])
                min_val = prices[i];

            if (prices[i] - min_val > max_val)
                max_val = prices[i] - min_val;
        }

        return max_val;
    }
};