// https://www.codewars.com/kata/56747fd5cb988479af000028

package main

import (
	"fmt"
)

func GetMiddle(s string) string {
	runes := []rune(s)
	l := len(runes)
	if l < 3 {
		return s
	}
	return string(runes[(l-1)/2 : l/2+1])
}

func main() {
	fmt.Println(GetMiddle("test"), "es")
	fmt.Println(GetMiddle("testing"), "t")
}
