// https://www.codewars.com/kata/5168bb5dfe9a00b126000018

package main

import (
	"fmt"
	"strings"
)

func Solution(word string) string {
	var b strings.Builder
	for i := len(word) - 1; i >= 0; i-- {
		b.WriteByte(word[i])
	}
	return b.String()
}

func main() {
	fmt.Println(Solution("world"), "dlrow")
}
