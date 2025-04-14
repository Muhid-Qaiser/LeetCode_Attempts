class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {

        int total=0, curr=0, start=0, diff=0;

        for (int i=0; i<gas.size(); i++)
        {
            diff = gas[i] - cost[i];
            total += diff;
            curr += diff;

            if (curr < 0)
            {
                curr = 0;
                start = i+1;
            }
        }

        return (total >= 0) ? start : -1;

    }
};