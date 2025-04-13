class Solution
{
public:
    int removeElement(vector<int> &nums, int val)
    {

        int i = 0, j = nums.size() - 1;

        for (; i < nums.size() && i <= j; i++)
        {
            if (nums[i] == val)
            {
                while (j > i && nums[j] == val)
                    j--;
                swap(nums[i], nums[j]);
                j--;
                i--;
            }
        }

        return i;
    }
};