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

func main() {
	inputFile := "input3.txt"

	dat, err := ioutil.ReadFile(inputFile)
	check(err)

	mapAsString := string(dat)

	heightOfMap := getNumberOfLines(mapAsString)

	posX := 0
	posY := 0
	numberOfTrees := 0
	for i := 0; i < heightOfMap; i++ {
		charAtPosXY := getCharAtPos(mapAsString, posX, posY)
		if charAtPosXY == '#' {
			numberOfTrees++
		}
		posX += 3
		posY++
	}
	fmt.Printf("Number of Trees: %d\n", numberOfTrees)
}
