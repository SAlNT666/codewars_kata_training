// https://www.codewars.com/kata/513e08acc600c94f01000001

package main

import (
	"fmt"
)

func RGB(r, g, b int) string {
	r, g, b = clamp(r), clamp(g), clamp(b)
	rgbHex := fmt.Sprintf("%02X%02X%02X", r, g, b)
	return rgbHex
}

func clamp(value int) int {
	if value < 0 {
		return 0
	}
	if value > 255 {
		return 255
	}
	return value
}

func main() {
	fmt.Println(RGB(254, 253, 252), "FEFDFC")
	fmt.Println(RGB(-20, 275, 125), "00FF7D")
}
