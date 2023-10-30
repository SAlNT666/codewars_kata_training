// https://www.codewars.com/kata/554b4ac871d6813a03000035

package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func HighAndLow(in string) string {
	min, max := math.MaxInt, math.MinInt
	for _, n := range strings.Fields(in) {
		intN, _ := strconv.Atoi(n)
		if intN < min {
			min = intN
		} else if intN > max {
			max = intN
		}
	}

	return fmt.Sprintf("%d %d", max, min)
}

func main() {
	fmt.Println(HighAndLow("1 9 3 4 -5"), "9 -5")
}
