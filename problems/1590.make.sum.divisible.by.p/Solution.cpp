#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  int minSubarray(vector<int> &nums, int p) {
    long totalSum = 0;
    for (int x : nums)
      totalSum += x;

    if (totalSum % p == 0) {
      return 0;
    }

    int need = totalSum % p;

    unordered_map<int, int> last_seen;
    last_seen[0] = -1;

    long cur = 0;
    int out = nums.size();

    for (int i = 0; i < nums.size(); ++i) {
      cur += nums[i];

      int mod = cur % p;

      int target = (mod - need + p) % p;

      if (last_seen.count(target)) {
        out = min(out, i - last_seen[target]);
      }

      last_seen[mod] = i;
    }

    return out < nums.size() ? out : -1;
  }
};

int main() {
  Solution sol;

  vector<int> nums = {3, 1, 4, 2};
  int p = 6;

  int risultato = sol.minSubarray(nums, p);

  cout << risultato << endl;
}
