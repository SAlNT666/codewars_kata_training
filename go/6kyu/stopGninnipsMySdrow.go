//https://www.codewars.com/kata/5264d2b162488dc400000001

package main

import (
	"fmt"
	"strings"
)

func SpinWords(str string) string {
	words := strings.Fields(str)
	for i, w := range words {
		if len(w) > 4 {
			words[i] = reverseString(w)
		}
	}
	return strings.Join(words, " ")
}

func reverseString(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func main() {
	fmt.Println(SpinWords("Hey fellow warriors qeq qwerty asdfghjkl zxcvvbnmnbvcxz is"))
}
