// https://www.codewars.com/kata/514b92a657cdc65150000006

package main

import (
	"fmt"
)

func Multiple3And5(number int) int {
	var sum int
	for n := 3; n < number; n += 3 {
		sum += n
	}
	for n := 5; n < number; n += 5 {
		if n%3 != 0 {
			sum += n
		}
	}
	return sum
}

func main() {
	fmt.Println(Multiple3And5(10), 23)
}
