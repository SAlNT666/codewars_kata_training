// https://www.codewars.com/kata/54d496788776e49e6b00052f

package main

import (
	"fmt"
	"math"
	"sort"
	"strings"
)

func SumOfDivided(lst []int) string {
	factorSum := make(map[int]int)

	for _, num := range lst {
		factors := primeFactors(num)
		for _, factor := range factors {
			factorSum[factor] += num
		}
	}

	keys := make([]int, 0, len(factorSum))
	for k := range factorSum {
		keys = append(keys, k)
	}
	sort.Ints(keys)

	pairs := make([]string, len(keys))
	for i, k := range keys {
		pairs[i] = fmt.Sprintf("(%d %d)", k, factorSum[k])
	}

	return strings.Join(pairs, "")
}

func primeFactors(n int) []int {
	factors := make([]int, 0)
	visited := make(map[int]bool)

	// Обрабатываем отрицательность числа
	if n < 0 {
		visited[-1] = true
		n = -n
	}

	// Обрабатываем деление на 2
	for n%2 == 0 {
		if !visited[2] {
			factors = append(factors, 2)
			visited[2] = true
		}
		n /= 2
	}

	// Обрабатываем остальные делители
	for i := 3; i <= int(math.Sqrt(float64(n))); i += 2 {
		for n%i == 0 {
			if !visited[i] {
				factors = append(factors, i)
				visited[i] = true
			}
			n /= i
		}
	}

	// Добавляем оставшийся простой делитель, если он больше 2
	if n > 2 && !visited[n] {
		factors = append(factors, n)
	}

	return factors
}

func main() {
	lst1 := []int{12, 15}
	fmt.Println(SumOfDivided(lst1), "(2 12)(3 27)(5 15)")
	lst2 := []int{15, 30, -45}
	fmt.Println(SumOfDivided(lst2), "(2 54)(3 135)(5 90)(7 21)")
}
