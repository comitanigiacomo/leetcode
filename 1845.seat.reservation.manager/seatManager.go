type SeatManager struct {
	seats []bool
	min   int
}

func Constructor(n int) SeatManager {
	return SeatManager{make([]bool, n+1), 1}
}

func (this *SeatManager) Reserve() int {
	for this.seats[this.min] {
		this.min++
	}
	this.seats[this.min] = true
	return this.min
}

func (this *SeatManager) Unreserve(seatNumber int) {
	this.seats[seatNumber] = false
	if seatNumber < this.min {
		this.min = seatNumber
	}
}