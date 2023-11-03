func buildArray(target []int, n int) []string {

	output := []string{}
	stream := []int{}

	for i := 1; i <= n; i++ {
		stream = append(stream, i)
	}

	for i := 0; i < len(target); i++ {
		if target[i] == stream[0] {
			output = append(output, "Push")
			stream = stream[1:]
		} else if target[i] > stream[0] {
			output = append(output, "Push")
			stream = stream[1:]
			output = append(output, "Pop")
			i--
		}
	}
	return output
}