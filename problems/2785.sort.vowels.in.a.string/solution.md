# 2785.sort.vowels.in.a.string

Here's the full description of the [problem](https://leetcode.com/problems/sort-vowels-in-a-string/submissions/?envType=daily-question&envId=2023-11-13)


# Approach

Initially my idea was to scan the string and use support structures to save important information in memory for solving the problem. In particular, the program uses the `index` slice to save the indices of the vowels within the `s` string, and the `vowels` slice containing all the vowels. I also created a slice `reorder`, containing the vowels that need to be reordered. Once this has been done, the program iterates again on the string s and, if it finds a vowel, uses the information from the supporting data structures to insert the correct vowel into the string s, taking it from the slice reorder which will contain them ordered based on the corresponding ASCII character.

# Complexity

- Time complexity: O(k * log(k)), where k is the number of vowels

- Space complexity: O(n)


# code

```go
    index := []int{}
    vowels := []string{"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    reorder := []string{}
    out := ""

    for i := 0; i < len(s); i++ {
        if contiene(string(s[i]), vowels){
            index = append(index, i)
            reorder = append(reorder, string(s[i]))
        }
    } 

    if len(index) == 0{
        return s
    }

    sort.Strings(reorder)

    count := 0

    for i := 0; i < len(s); i++ {
        if count < len(index) && count < len(reorder) && i == index[count] {
            out += reorder[count]
            count++
        } else {
            out += string(s[i])
        }
    }
    return out

}

func contiene(s string, vowels []string)bool {
    for _,v := range vowels {
        if s == v {
            return true
        }
    }
    return false
}

```

# Intuition

At this point the program was functional, but its execution time was too long. To reduce it, I avoided creating an array for the vowel indices and worked directly on the original indices. I used a byte buffer to accumulate the vowels before sorting them. Then I used another buffer to construct the resulting string, replacing the sorted vowels in their respective original indices


# Complexity

- Time complexity: O(k * log(k)), where k is the number of vowels

- Space complexity: O(k)


# code 

```go
func sortVowels(s string) string {
	vowelMap := make(map[rune]bool)
	for _, v := range "aeiouAEIOU" {
		vowelMap[v] = true
	}

	var buf bytes.Buffer
	count := 0

	for i := 0; i < len(s); i++ {
		if vowelMap[rune(s[i])] {
			buf.WriteByte(s[i])
			count++
		}
	}

	if count == 0 {
		return s
	}

	vowelSlice := buf.String()
	sortedVowels := sortString(vowelSlice)

	count = 0
	var result bytes.Buffer

	for i := 0; i < len(s); i++ {
		if vowelMap[rune(s[i])] {
			result.WriteByte(sortedVowels[count])
			count++
		} else {
			result.WriteByte(s[i])
		}
	}

	return result.String()
}

func sortString(s string) string {
	runes := []rune(s)
	sort.Slice(runes, func(i, j int) bool {
		return runes[i] < runes[j]
	})
	return string(runes)
}
```