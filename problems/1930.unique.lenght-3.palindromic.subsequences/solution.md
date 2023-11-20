
```go
func countPalindromicSubsequence(s string) int {
	var count int
	var seen map[string]bool = make(map[string]bool)

	for i := 0; i < len(s)-2; i++ {
		for j := i + 1; j < len(s)-1; j++ {
			for k := j + 1; k < len(s); k++ {
				if s[i] == s[k] {
					palindrome := string(s[i]) + string(s[j]) + string(s[k])
					if !seen[palindrome] {
						count++
						seen[palindrome] = true
					}
				}
			}
		}
	}

	return count
}
```