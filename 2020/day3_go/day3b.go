package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func getFirstLineLength(mapString string) (count int) {
	count = 0
	for {
		if mapString[count] == ' ' || mapString[count] == '\n' {
			break
		}
		count++
	}
	return
}

func getCharAtPos(mapString string, x, y int) byte {
	lineLength := getFirstLineLength(mapString)

	charPositionXY := (lineLength+1)*y + x%(lineLength-1)
	charAtPosXY := mapString[charPositionXY]

	return charAtPosXY
}

func getNumberOfLines(mapString string) int {
	rg := regexp.MustCompile("[.#]+")
	matches := rg.FindAllStringIndex(mapString, -1)
	return len(matches)
}

func findNumberOfTrees(mapAsString string, stepX, stepY int) int {
	heightOfMap := getNumberOfLines(mapAsString)
	posX := 0
	posY := 0
	numberOfTrees := 0
	for i := 0; i < heightOfMap; i += stepY {
		charAtPosXY := getCharAtPos(mapAsString, posX, posY)
		if charAtPosXY == '#' {
			numberOfTrees++
		}
		posX += stepX
		posY += stepY
	}
	return numberOfTrees
}

func main() {
	inputFile := "input3.txt"

	dat, err := ioutil.ReadFile(inputFile)
	check(err)

	mapAsString := string(dat)

	fmt.Printf("Number of Trees: %d\n", findNumberOfTrees(mapAsString, 1, 1))
	fmt.Printf("Number of Trees: %d\n", findNumberOfTrees(mapAsString, 3, 1))
	fmt.Printf("Number of Trees: %d\n", findNumberOfTrees(mapAsString, 5, 1))
	fmt.Printf("Number of Trees: %d\n", findNumberOfTrees(mapAsString, 7, 1))
	fmt.Printf("Number of Trees: %d\n", findNumberOfTrees(mapAsString, 1, 2))
}
