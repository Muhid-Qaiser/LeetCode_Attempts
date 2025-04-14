class Solution
{
public:
    bool canJump(vector<int> &nums)
    {
        bool flag = true;
        if (nums.size() > 1)
        {
            int g = nums.size() - 1, i = nums.size() - 2;
            for (; i >= 0; i--)
            {
                if (i + nums[i] >= g)
                {
                    g = i;
                    flag = true;
                }
                else
                    flag = false;
            }
            return flag;
        }
        else
            return flag;
    }
};