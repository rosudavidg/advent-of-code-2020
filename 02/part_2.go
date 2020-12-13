package main

import (
	"fmt"
	"strconv"
	"strings"

	"../utils/reader"
)

func is_valid(text string, character byte, pos1, pos2 int) bool {
	counter := 0

	if text[pos1-1] == character {
		counter++
	}

	if text[pos2-1] == character {
		counter++
	}

	return counter == 1
}

func main() {
	validCount := 0
	input := reader.ReadInput()

	for _, line := range input {
		if line != "" {

			splitted := strings.Split(line, ":")
			text := strings.TrimSpace(splitted[1])

			splitted = strings.Split(splitted[0], " ")
			character := splitted[1][0]

			splitted = strings.Split(splitted[0], "-")
			start, _ := strconv.Atoi(splitted[0])
			stop, _ := strconv.Atoi(splitted[1])

			if is_valid(text, character, start, stop) {
				validCount++
			}
		}
	}

	fmt.Println(validCount)
}
