class Solution
{
public:
    int majorityElement(vector<int> &nums)
    {
        unordered_map<int, int> counts;
        int res = -1;

        for (int i = 0; i < nums.size(); i++)
        {
            if (counts.count(nums[i]) == 0)
                counts[nums[i]] = 1;
            else
                counts[nums[i]] += 1;

            if (counts[nums[i]] > nums.size() / 2)
                res = nums[i];
        }

        return res;
    }
};