// https://www.codewars.com/kata/52fba66badcd10859f00097e

package main

import (
	"fmt"
	"unicode"
)

func Disemvowel(comment string) string {
	var newComment []int32
	for _, s := range comment {
		switch unicode.ToLower(s) {
		case 'a', 'e', 'i', 'o', 'u':
			continue
		default:
			newComment = append(newComment, s)
		}
	}
	return string(newComment)
}

func main() {
	fmt.Println(Disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")
}
