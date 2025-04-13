class Solution
{
public:
    int removeDuplicates(vector<int> &nums)
    {
        vector<int> dups;
        int i = 1, j = 1;

        for (; j < nums.size(); j++)
        {
            if (nums[j] != nums[i - 1])
                nums[i++] = nums[j];
        }

        // int i=0,k=-10,n=nums.size();

        // if (nums.size()>=1)
        //     for(; i<n && k<n-1; i++)
        //     {
        //         if ( check_dups(nums[i], dups))
        //         {
        //             if (i>=n-1)
        //                 break;

        //             k = i+1;
        //             while( k<n-1 && check_dups(nums[k], dups) )
        //                 k++;

        //             if (check_dups(nums[k], dups))
        //                 break;
        //             nums[i] = nums[k];
        //         }

        //         dups.push_back(nums[i]);
        //     }

        return i;
    }

    // bool check_dups(int val, vector<int> arr)
    // {
    //     for (int i = 0; i < arr.size(); i++)
    //         if (arr[i] == val)
    //             return true;
    //     return false;
    // }
};