# 2265.count.nodes.equal.to.average.of.subtree



Here's the full description of the [problem](https://leetcode.com/problems/build-an-array-with-stack-operations/description/?envType=daily-question&envId=2023-11-03)


# Approach

Initially my idea was to create two support arrays, one to return the output of the function and one for the stream of integers in the range `[1-n]`. By looping through the `target` array, the program checks at each iteration whether the target value is greater than or equal to the first integer of `stream`. if the values ​​are the same, the program puts the value of the stream on the stack, otherwise it adds it and removes it immediately, to be able to insert the element of the next stream onto the stack, at the next iteration


# Complexity

- Time complexity: O(n)
- Space complexity: O(n)

# code

```go
func buildArray(target []int, n int) []string {

    output := []string{}
    stream := []int{}

    for i := 1; i <= n; i++ {
        stream = append(stream, i)
    }
    
    for i:= 0; i < len(target); i++ {
        if target[i] == stream[0] {
            output = append(output, "Push")
            stream = stream[1:]
        }else if target[i] > stream[0] {
            output = append(output, "Push")
            stream = stream[1:]
            output = append(output, "Pop")
            i--
        }
    }
    return output
}
```

# Intuition

Since `n` is always greater than or equal to the largest value of target, I can directly use the value n as a stram, without having to use a supporting array. Furthermore, with this modification I can also speed up the program, because I eliminate the first loop of construction of the stream array

# complexity 2

- Time Complexity: O(n) - The function's time complexity is linear with respect to the length of the `target` slice.

- Space Complexity: O(n) - The function's space complexity is linear with respect to the length of the `target` slice, primarily due to the output slice.

# code 2

```go
func buildArray(target []int, n int) []string {

    output := []string{}

    n = n - n + 1
    
    for i:= 0; i < len(target); i++ {
        if target[i] == n {
            output = append(output, "Push")
            n++
        }else if target[i] > n {
            output = append(output, "Push")
            output = append(output, "Pop")
            i--
            n++
        }
    }
    return output
}
```


