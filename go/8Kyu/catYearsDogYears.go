package main

import "fmt"

func main() {
	fmt.Println(CalculateYears(10))
}

func CalculateYears(years int) (result [3]int) {
	var catYears, dogYears, zeroInt, firstInt int
	var zero, first bool
	zero = years == 0
	if zero {
		zeroInt = 1
	}
	catYears += 15 * (1 - zeroInt)

	first = years == 1
	if first {
		firstInt = 1
	}
	catYears += 9 * (1 - firstInt)
	dogYears = catYears

	if years > 2 {
		catYears += 4 * (years - 2)
		dogYears += 5 * (years - 2)
	}

	return [3]int{years, catYears, dogYears}
}
