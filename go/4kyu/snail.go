// https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

package main

import (
	"fmt"
)

func Snail(snailMap [][]int) []int {
	result := make([]int, 0)

	if len(snailMap) == 0 {
		return result
	}

	rows := len(snailMap)
	cols := len(snailMap[0])
	topRow := 0
	bottomRow := rows - 1
	leftCol := 0
	rightCol := cols - 1

	for topRow <= bottomRow && leftCol <= rightCol {
		// Traverse top row
		for col := leftCol; col <= rightCol; col++ {
			result = append(result, snailMap[topRow][col])
		}
		topRow++

		// Traverse right column
		for row := topRow; row <= bottomRow; row++ {
			result = append(result, snailMap[row][rightCol])
		}
		rightCol--

		if topRow <= bottomRow {
			// Traverse bottom row
			for col := rightCol; col >= leftCol; col-- {
				result = append(result, snailMap[bottomRow][col])
			}
			bottomRow--
		}

		if leftCol <= rightCol {
			// Traverse left column
			for row := bottomRow; row >= topRow; row-- {
				result = append(result, snailMap[row][leftCol])
			}
			leftCol++
		}
	}

	return result
}

func main() {
	snailMap := [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	fmt.Println(Snail(snailMap), []int{1, 2, 3, 6, 9, 8, 7, 4, 5})
	fmt.Println(Snail([][]int{}), nil)
}
