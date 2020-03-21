package main

import (
	"fmt"
	"time"
)

func insertionSort(arr []int) {
	for index := 0; index < len(arr); index++ {
		if index-1 < 0 {
			continue
		}
		currentNumber := arr[index]
		previousNumber := arr[index-1]
		if previousNumber > currentNumber {
			// previous number in array is bigger - swap 
			arr[index] = previousNumber
			arr[index-1] = currentNumber
			currentSwappingIndex := index - 1
			currentNumber = arr[currentSwappingIndex]
			// continue checking the swapped number to push it forward if needed
			for currentSwappingIndex > 0 {
				if currentSwappingIndex-1 < 0 {
					break
				}
				previousNumber := arr[currentSwappingIndex-1]
				// number that we just swapped (moved forward) is still larger 
				// than the next previous number - swap again
				if currentNumber < previousNumber {
					arr[currentSwappingIndex] = previousNumber
					arr[currentSwappingIndex-1] = currentNumber
				}
				currentSwappingIndex--
			}
		}
	}
}

func main() {
	inputArray := []int{4, 6, 2, 3, 1, 8}
	fmt.Println(inputArray)
	start := time.Now()
	insertionSort(inputArray)
	totalTime := time.Since(start)
	fmt.Println(inputArray)
	fmt.Printf("sort took %s to sort array\n", totalTime)
}
