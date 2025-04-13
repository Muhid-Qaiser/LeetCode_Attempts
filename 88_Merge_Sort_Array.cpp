class Solution
{
public:
    void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
    {

        int *arr = new int[m + n];
        int i = 0, j = 0;

        if (n != 0)
        {
            for (int idx = 0; idx < m + n; idx++)
            {
                if (i < m && j < n)
                    arr[idx] = (nums1[i] <= nums2[j]) ? nums1[i++] : nums2[j++];
                else if (i >= m)
                    arr[idx] = nums2[j++];
                else
                    arr[idx] = nums1[i++];
            }

            for (int idx = 0; idx < m + n; idx++)
            {
                nums1[idx] = arr[idx];
            }
        }

        delete[] arr;
    }
};