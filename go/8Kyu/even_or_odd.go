// https://www.codewars.com/kata/53da3dbb4a5168369a0000fe

package main

import "fmt"

func EvenOrOdd(number int) string {
	return []string{"Even", "Odd"}[number&1]
}

func main() {
	fmt.Println(EvenOrOdd(5), "Odd")
	fmt.Println(EvenOrOdd(10), "Even")
}
