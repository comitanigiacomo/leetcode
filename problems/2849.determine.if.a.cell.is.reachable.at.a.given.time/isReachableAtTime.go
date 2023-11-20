func isReachableAtTime(sx int, sy int, fx int, fy int, t int) bool {
	distX := abs(fx - sx)
	distY := abs(fy - sy)
	pMin := 0
	if sx == fx && sy == fy {
		if t != 1 {
			return true
		}
	} else {
		pMin = max(distX, distY)
		if t >= pMin {
			return true
		}
	}
	return false
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}