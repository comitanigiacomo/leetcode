func buildArray(target []int, n int) []string {

	output := []string{}

	n = n - n + 1

	for i := 0; i < len(target); i++ {
		if target[i] == n {
			output = append(output, "Push")
			n++
		} else if target[i] > n {
			output = append(output, "Push")
			output = append(output, "Pop")
			i--
			n++
		}
	}
	return output
}