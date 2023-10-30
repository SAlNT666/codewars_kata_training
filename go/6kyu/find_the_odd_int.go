// https://www.codewars.com/kata/54da5a58ea159efa38000836

package main

import (
	"fmt"
)

func FindOdd(seq []int) (odd int) {
	for _, n := range seq {
		odd ^= n
	}

	return
}

func main() {
	fmt.Println(FindOdd([]int{20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5}), 5)
}
