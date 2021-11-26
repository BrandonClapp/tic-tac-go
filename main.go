package main

import (
	"fmt"
	"strconv"
)

func main() {
	// Initialize board state
	boardSpaces := [9]string{"-", "-", "-", "-", "-", "-", "-", "-", "-"}
	player := "X"
	isWinner := false

	// Show initial board
	printBoard(&boardSpaces)

	// Loop while there is no winner
	for !isWinner {
		fmt.Println("Current player is: ", player)
		fmt.Println("Choose an available space, 0-8, or type 'board' to see the board.")

		var input string
		fmt.Scanln(&input)

		if input == "board" {
			printBoard(&boardSpaces)
			continue
		}

		position, err := strconv.Atoi(input)
		if err != nil {
			// log.Panicln("Could not parse input to integer.")
			// log.Default("Please enter a number 0-8")
			fmt.Println("Please enter a number, 0-8")
			continue
		}

		if boardSpaces[position] == "-" {
			// Set this space to the player
			boardSpaces[position] = player
		} else if boardSpaces[position] == "X" || boardSpaces[position] == "O" {
			fmt.Println("Space already occupied. Choose another.")
			continue
		}

		printBoard(&boardSpaces)

		// Check win condition
		winner := checkWinConditions(&boardSpaces)
		if winner {
			fmt.Println("Winner is ", player, "!!")
			break
		}

		// If all spots on the board are occupied, it was a tie.
		if allSpotsOccupied(&boardSpaces) {
			fmt.Println("Tie!")
			break
		}

		player = swapPlayer(player)
	}

}

func swapPlayer(current string) string {
	if current == "X" {
		return "O"
	}
	return "X"
}

func checkWinConditions(board *[9]string) bool {
	winCombinations := [][]int{
		{0, 1, 2},
		{0, 3, 6},
		{0, 4, 8},
		{1, 4, 7},
		{2, 5, 8},
		{2, 4, 6},
		{3, 4, 5},
		{6, 7, 8},
	}

	for _, combo := range winCombinations {
		first := board[combo[0]]
		second := board[combo[1]]
		third := board[combo[2]]

		if isWin(first, second, third) {
			/// winner detected
			return true
		}
	}

	return false
}

func isWin(one string, two string, three string) bool {
	if one == "-" || two == "-" || three == "-" {
		return false
	}

	if one == "X" && two == "X" && three == "X" {
		return true
	}

	if one == "O" && two == "O" && three == "O" {
		return true
	}

	return false
}

func allSpotsOccupied(board *[9]string) bool {
	for _, spot := range board {
		if spot == "-" {
			return false
		}
	}

	return true
}

func printBoard(board *[9]string) {
	first := fmt.Sprintf("  %s  |  %s  |  %s  ", board[0], board[1], board[2])
	second := fmt.Sprintf("  %s  |  %s  |  %s  ", board[3], board[4], board[5])
	third := fmt.Sprintf("  %s  |  %s  |  %s  ", board[6], board[7], board[8])

	fmt.Println(first)
	fmt.Println("-----------------")
	fmt.Println(second)
	fmt.Println("-----------------")
	fmt.Println(third)
}
