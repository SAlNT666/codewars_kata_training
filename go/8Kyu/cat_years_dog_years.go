// https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b

package main

import "fmt"

func CalculateYears(years int) (result [3]int) {
	switch years {
	case 1:
		result = [3]int{1, 15, 15}
	case 2:
		result = [3]int{2, 24, 24}
	default:
		result = [3]int{years, 24 + 4*(years-2), 24 + 5*(years-2)}
	}
	return result
}

func main() {
	fmt.Println(CalculateYears(5), "[5 36 39]")
	fmt.Println(CalculateYears(10), "[10 56 64]")
}
