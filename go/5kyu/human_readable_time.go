// https://www.codewars.com/kata/52685f7382004e774f0001f7

package main

import (
	"fmt"
)

func HumanReadableTime(seconds int) string {
	return fmt.Sprintf("%02d:%02d:%02d", seconds/3600, seconds/60%60, seconds%60)
}

func main() {
	fmt.Println(HumanReadableTime(359999), "99:59:59")
}
