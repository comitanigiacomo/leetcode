# 1845.seat.reservation.manager

Here's the full description of the [problem](https://leetcode.com/problems/seat-reservation-manager/description/?envType=daily-question&envId=2023-11-06)


# Approach

I thought of implementing the SeatManager type using a struct containing a string of booleans representing seat reservations, and an integer that keeps track of the minimum seat number. Once this is done, the other operations can be performed easily


# Complexity

- Time complexity: O(n), where n is the number of seats

- Space complexity: O(n)


# code

```go
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
```
