# 1561.maximum.number.of.coins.you.can.get

Here's the full description of the [problem](https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/?envType=daily-question&envId=2023-11-24)


# Approach

The approach to solving this problem involves sorting the array of piles in ascending order.

Once this is done, I assume that each tuple is formed by the two largest elements available in the array and the smallest element. Of these, I take the middle one. I iterate this process until I have considered all the tuples.

# Complexity

- Time complexity: O(n log n) - Sorting the array takes O(n log n) time.
- Space complexity: O(1) - The algorithm uses only a constant amount of space



# code

```go
func maxCoins(piles []int) int {
    sort.Ints(piles)

    out := 0

    var flag bool

    for i := len(piles)-1; i >= len(piles)/3; i-- {

        flag = !flag
        if flag == false {
             out += piles[i]
        }
    }
    return out
}
```