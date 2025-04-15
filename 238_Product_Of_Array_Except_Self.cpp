class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size(), left = 1, right = 1;
        vector<int> arr(n, 1);

        for (int i=0, j=n-1; i<n || j>0; i++, j--)
        {
            arr[i] *= left;
            arr[j] *= right;

            left *= nums[i];
            right *= nums[j];
        }

        return arr;
    }
};