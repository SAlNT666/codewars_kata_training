// https://www.codewars.com/kata/54ff3102c1bad923760001f3

package main

import "fmt"

func GetCount(str string) (count int) {
	for _, l := range str {
		switch l {
		case 'a', 'e', 'i', 'o', 'u':
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(GetCount("abracadabra"), 5)
}
