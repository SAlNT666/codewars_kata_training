// https://www.codewars.com/kata/55c4eb777e07c13528000021

package main

import (
	"fmt"
	"math"
)

func Zeroes(base, number int) int {
	result := math.MaxInt

	for prime := 2; prime <= base; prime++ {
		if base%prime == 0 {
			baseExponent := 0
			for base%prime == 0 {
				baseExponent++
				base /= prime
			}
			numberExponent := 0
			currentMultiplier := prime
			for currentMultiplier <= number {
				numberExponent += number / currentMultiplier
				currentMultiplier *= prime
			}
			if numberExponent/baseExponent < result {
				result = numberExponent / baseExponent
			}
		}
	}

	if result == math.MaxInt {
		result = 0
	}

	return result
}

func main() {
	fmt.Println(Zeroes(10, 10), 2)
}
