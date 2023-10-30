// https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

package main

import (
	"fmt"
	"strings"
)

func DuplicateEncode(word string) string {
	word = strings.ToLower(word)
	charCount := make(map[rune]int)

	for _, char := range word {
		charCount[char]++
	}

	result := make([]byte, len(word))
	for i, char := range word {
		if charCount[char] > 1 {
			result[i] = ')'
		} else {
			result[i] = '('
		}
	}

	return string(result)
}

func main() {
	fmt.Println(DuplicateEncode("din"), "(((")
	fmt.Println(DuplicateEncode("recede"), "()()()")
}
