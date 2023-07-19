import graphs

class Hangman:
    def __init__(self, word='test') -> None:
        self.result = word.upper()
        self.lifes = graphs.lifes
        self.errors = 0
        self.attempts = 0
        self.word = ['_']*len(self.result)

        self.game_on = True
        self.game_loop()

    def print_board(self):
        print(self.lifes[self.errors])
        print(f"Attempts: {self.attempts}.")
        print(" ".join(self.word))


    def get_input(self):
        new_letter = input("| Enter a new letter:").upper()
        if new_letter in self.result:
            for i, letter in enumerate(self.result):
                if letter == new_letter:
                    self.word[i] = letter
        else:
            self.errors += 1

        self.attempts +=1

    def check_game_over(self):
        if self.word.count("_") == 0:
            print(" ".join(self.word))
            print("YOU WON")
            self.game_on = False
        elif self.errors == 6:
            print(" ".join(self.word))
            print("GAME OVER")
            print(f"The word was: {self.result}")
            self.game_on = False

    def game_loop(self):
        for i, letter in enumerate(self.result):
            if letter != " ":
                continue
            self.word[i] = letter
        while self.game_on:
            self.print_board()
            self.get_input()
            self.check_game_over()

if __name__ == "__main__":
    Hangman("Choque de Cultura")
