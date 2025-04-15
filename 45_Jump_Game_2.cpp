class Solution {
public:
    int jump(vector<int>& nums) {
        
        int g = nums.size()-1, k=0;

        while (g > 0)
        {
            for (int i=0; i<g; i++)
            {
                if ( (nums[i] + i) >= g ) 
                {
                    k++;
                    g = i;
                    break;
                }
            }
        }
        return k;
    }
};