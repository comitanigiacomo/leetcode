#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

class Solution {
public:
  int minOperations(vector<int> &nums, int k) {
    int sum = accumulate(nums.begin(), nums.end(), 0LL);

    return sum % k;
  }
};

int main() {
  Solution sol;

  vector<int> nums = {3, 9, 7};
  int k = 5;

  int risultato = sol.minOperations(nums, k);

  cout << risultato << endl;
}
