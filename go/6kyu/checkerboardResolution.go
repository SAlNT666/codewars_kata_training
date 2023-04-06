// https://www.codewars.com/kata/60576b180aef19001bce494d

package main

import "fmt"

func CountCheckerboard(width, height, resolution uint64) uint64 {
	nBlackFirstRow := width/resolution/2*resolution + width%resolution*(width/resolution%2)
	nBlackFirstColumn := height/resolution/2*resolution + height%resolution*(height/resolution%2)
	nBlack := nBlackFirstRow*(height-nBlackFirstColumn) + (width-nBlackFirstRow)*nBlackFirstColumn

	return nBlack
}

func main() {
	fmt.Println(CountCheckerboard(11, 6, 1), 33)
	fmt.Println(CountCheckerboard(11, 6, 2), 32)
	fmt.Println(CountCheckerboard(11, 6, 5), 31)
	fmt.Println(CountCheckerboard(9, 5, 2), 22)
	fmt.Println(CountCheckerboard(9, 5, 4), 21)
	fmt.Println(CountCheckerboard(9, 5, 8), 5)
}
