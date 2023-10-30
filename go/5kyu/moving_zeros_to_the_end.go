// https://www.codewars.com/kata/52597aa56021e91c93000cb0

package main

import (
	"fmt"
)

func MoveZeros(arr []int) []int {
	newArr := make([]int, len(arr))
	j := 0
	for i := range arr {
		if arr[i] != 0 {
			newArr[j] = arr[i]
			j++
		}
	}
	return newArr
}

func main() {
	fmt.Println(MoveZeros([]int{1, 2, 0, 1, 0, 1, 0, 3, 0, 1}), "[1 2 1 1 3 1 0 0 0 0]")
}
