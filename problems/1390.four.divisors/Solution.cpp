#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int sumFourDivisors(vector<int> &nums) {
    int totalSum = 0;
    for (int n : nums) {
      vector<int> divisori;
      int limite = sqrt(n);
      for (int j = 1; j * j <= n; ++j) {
        if (n % j == 0) {
          divisori.push_back(j);
          if (j * j != n) {
            divisori.push_back(n / j);
          }
        }
      }
      if (divisori.size() == 4) {
        for (int d : divisori) {
          totalSum += d;
        }
      }
    }
    return totalSum;
  }
};

int main() {
  vector<int> nums{21, 4, 7};
  int risultato = Solution().sumFourDivisors(nums);
  cout << risultato << endl;
}
