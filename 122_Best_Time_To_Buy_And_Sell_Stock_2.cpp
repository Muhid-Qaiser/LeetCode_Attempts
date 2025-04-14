class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int min_val = INT_MAX, max_val = 0, n = prices.size(), total = 0;

        for (int i = 0; i < n; i++)
        {
            if (min_val > prices[i])
                min_val = prices[i];

            if (prices[i] - min_val >= max_val)
            {
                max_val = prices[i] - min_val;

                if (i == n - 1 || prices[i] > prices[i + 1])
                {
                    min_val = prices[i];
                    total += max_val;
                    max_val = 0;
                }
            }
        }

        return total;
    }
};