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