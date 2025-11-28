#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    long long maxSubarraySum(vector<int>& nums, int k) {
        long long INF = LLONG_MAX;

        vector<long long> min_prefix(k, INF);

        min_prefix[k - 1] = 0;
        
        long long current_sum = 0;
        long long out = LLONG_MIN;
        
        for (int i = 0; i < nums.size(); ++i) {
            current_sum += nums[i];
            
            int r = i % k;
            
            if (min_prefix[r] != INF) {
                out = max(out, current_sum - min_prefix[r]);
            }
            
            min_prefix[r] = min(min_prefix[r], current_sum);
        }
        return out;
    }
};

int main() {
    Solution sol;
    
    vector<int> nums = {-5, 1, 2, -3, 4}; 
    int k = 2;

    long long risultato = sol.maxSubarraySum(nums,k); 

    cout << risultato << endl;

    return 0;
}

