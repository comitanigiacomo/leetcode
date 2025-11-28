#import "@preview/bubble:0.2.2": *
#import "@preview/note-me:0.4.0": *

#show: bubble.with(
  title: "Knowledge",
  author: "Giacomo Comitani",
  date: datetime.today().display(),
  year: "2025",
  main-color: "#005FDB"
)

#let green(x) = text(fill: rgb("#2ecc40"), x)
#let orange(x) = text(fill: rgb("#ff851b"), x)
#let red(x) = text(fill: rgb("#ff2929"), x)
#let blue(x) = text(fill: rgb("#2971b8"), x)

#show table.cell: set text(weight: "bold")

#set table(
  fill: (_, y) => if calc.odd(y) { rgb("#a5e1f7") },
  stroke: rgb("#000000"),
)

#outline()

#pagebreak()

= Prefix Sum and Optimization

Let's analyze the following problem proposed by LeetCode: #link("https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/description/")[Maximum Subarray Sum With Length Divisible by K]

Given an integer array `nums` and an integer `k`, the problem asks to calculate the #green("maximum sum") of a subarray of `nums`, such that the #orange("length") of the subarray is #blue("divisible by k").

== 1. The Naive Approach (Brute Force)

A first approach might be to iterate through the array `nums` using two pointers, $i$ and $j$. For every subarray `nums[i:j]` where the length satisfies the condition, we compare the sum with a value stored in an `out` variable to find the maximum.

Here is an example of this logic in Python:

```python
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_sum = float('-inf')
        
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                
                length = j - i + 1

                if length % k == 0:
                    max_sum = max(max_sum, current_sum)
                    
        return max_sum if max_sum != float('-inf') else 0
```

Although this approach is conceptually correct, it is computationally expensive. It has a time complexity of $O(N^2)$ due to the nested loops required to check every possible subarray. For large inputs (e.g., N=105), this will result in a Time Limit Exceeded (TLE).

== 2. The Prefix Sum Technique

To resolve the problem in less time, we resort to the #blue("Prefix Sum") technique.

The core idea of Prefix Sum is to create (either in-place or in a new array) a structure where, for every index i:

$ P[i] = P[i-1] +"nums"[i] $

#note[ Why do we do this? Once the Prefix Sum array is calculated, we can obtain the sum of any subarray from index L to R in O(1) time using the property: $ "Sum"(L, R) = P[R] - P[L-1] $ ]

This reduces the complexity of calculating a subarray sum from linear time to constant time. By leveraging this property, we can optimize the previous algorithm significantly.

== 3. Optimized Solution (O(N))

To achieve linear time complexity O(N), we combine Prefix Sums with modular arithmetic.

The problem requires the subarray length to be divisible by k. $ ("current_index" - "start_index") % k == 0 $ This implies that current_index and start_index must have the #orange("same remainder") when divided by k.

To maximize the subarray sum: $ "MaxSum" = P["curr"] - P["prev"] $

We must #blue("minimize") P[prev]. Therefore, we only need to store the minimum prefix sum seen so far for each remainder class (0 to k−1).

Here is the optimized implementation:

```python
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        
        inf = sys.maxsize
        current_sum = 0
        out = -inf

        min_prefix = [inf] * k
        
        min_prefix[-1 % k] = 0

        for i, num in enumerate(nums):
            current_sum += num
            remainder = i % k

            if min_prefix[remainder] != inf:
                out = max(out, current_sum - min_prefix[remainder])

            min_prefix[remainder] = min(min_prefix[remainder], current_sum)

        return out if out != -inf else 0
```

= 4. General Applications of Prefix Sum

The Prefix Sum technique is not limited to this specific problem. It is a fundamental pattern in algorithmic problem solving. Here are other common scenarios where it is essential:

- *Range Sum Queries (Static Arrays)*: If you have an array that doesn't change (static), and you need to answer thousands of queries asking for the "sum between index i and j", Prefix Sum allows you to answer each query in O(1) after an O(N) preprocessing step.

- *Finding the "Equilibrium Index"*: An equilibrium index is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes. $ P[i-1] == "TotalSum" - P[i] $ Using the total sum and the current prefix sum, you can check this condition in a single pass.