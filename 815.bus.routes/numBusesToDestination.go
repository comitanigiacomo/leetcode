func numBusesToDestination(routes [][]int, source int, target int) int {
	if source == target {
		return 0
	}

	stopToBuses := make(map[int][]int)

	for i, route := range routes {
		for _, stop := range route {
			stopToBuses[stop] = append(stopToBuses[stop], i)
		}
	}

	visitedBuses := make(map[int]bool)
	visitedStops := make(map[int]bool)

	queue := []int{source}
	count := 0

	for len(queue) > 0 {
		size := len(queue)
		for i := 0; i < size; i++ {
			currentStop := queue[i]

			for _, bus := range stopToBuses[currentStop] {
				if visitedBuses[bus] {
					continue
				}

				visitedBuses[bus] = true

				for _, nextStop := range routes[bus] {
					if visitedStops[nextStop] {
						continue
					}

					visitedStops[nextStop] = true

					if nextStop == target {
						return count + 1
					}

					queue = append(queue, nextStop)
				}
			}
		}

		count++
		queue = queue[size:]
	}

	return -1
}