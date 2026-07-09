import random

class BoggleBoard:
    BOGGLE_DICE = [
      "AAEEGN", "ELRTTY", "AOOTTW", "ABBJOO",
      "EHRTVW", "CIMOTU", "DISTTY", "EIOSST",
      "DELRVY", "ACHOPS", "HIMNQU", "EEINSU",
      "EEGHNW", "AFFKPS", "HLNNRZ", "DEILRX"
    ]
    
    def __init__(self):
        self.board = []
        for _ in range(4):
            row = []
            for _ in range(4):
                row.append("-")
            self.board.append(row)
    def __init__(self):
        self.board = [["_" for _ in range(4)] for _ in range(4)]
    
    def shake(self):
        shuffled_dice = self.BOGGLE_DICE.copy()
        random.shuffle(shuffled_dice)
        dice_index = 0
        for i in range(4):
            for j in range(4):
                self.board[i][j] = random.choice(shuffled_dice[dice_index])
                dice_index += 1
    
    def __str__(self):
        output = ""
        for row in self.board:
            formatted_row = []
            for cell in row:
                if cell == "Q":
                    formatted_row.append("Qu")
                else:
                    formatted_row.append(f"{cell:<2}")
            output += " ".join(formatted_row) + "\n"
        return output
 
if __name__ == "__main__":
    board = BoggleBoard()
    
    print("New Board:")
    print(board)

    board.shake()
    print("Shaken Board:")
    print(board)

    board.shake()
    print("Shaken Again:")
    print(board)               