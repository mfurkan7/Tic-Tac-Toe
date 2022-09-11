import sys
import os


class Launcher:
    def __init__(self):
        self.board = {"title": "TIC-TAC-TOE", 1: {1: "   ", 2: "   ", 3: "   "}, 2: {1: "   ", 2: "   ", 3: "   "},
                      3: {1: "   ", 2: "   ", 3: "   "},
                      "lines": ["------------"], "seperator": "|"}
        self.board_print()
        print("\n\nPlayer 1 is X")
        print("Player 2 is O")
        self.marking_position = ""
        self.marking_position_list = []
        self.win_conditions = [(' X ', ' X ', ' X '), (' O ', ' O ', ' O ')]
        self.sign = ""
        self.turn_main_counter = 1
        self.input_check = True
        self.start()

    def start(self):
        while self.turn_main_counter != 10:
            if self.turn_main_counter % 2 == 0:
                self.sign = "O"
                if self.input_check is True:
                    self.marking()
                self.win_check()
            else:
                self.sign = "X"
                if self.input_check is True:
                    self.marking()
                self.win_check()

    def mark_input(self):
        self.marking_position = input(
            f"Where do you want to put {self.sign}?\nPlease write the co-ordinate as row,column!\n")
        for position in self.marking_position.split(","):
            self.marking_position_list.append(int(position))
        self.mark_check()

    def mark_check(self):
        if self.board[self.marking_position_list[0]][self.marking_position_list[1]] == "   ":
            self.input_check = True
        else:
            self.input_check = False
            print("This place is already marked! Please choose another space!")
            self.marking_position_list = []
            self.mark_input()

    def marking(self):
        self.mark_input()
        if self.turn_main_counter > 1:
            self.mark_check()
        self.board[self.marking_position_list[0]][self.marking_position_list[1]] = f" {self.sign} "
        self.marking_position_list = []
        self.turn_main_counter += 1
        self.marked = False
        self.board_print()

    def win_check(self):
        check_list = ((self.board[1][1], self.board[1][2], self.board[1][3]),
                      (self.board[2][1], self.board[2][2], self.board[2][3]),
                      (self.board[3][1], self.board[3][2], self.board[3][3]),
                      (self.board[1][1], self.board[2][1], self.board[3][1]),
                      (self.board[1][2], self.board[2][2], self.board[3][2]),
                      (self.board[1][3], self.board[2][3], self.board[3][3]),
                      (self.board[1][1], self.board[2][2], self.board[3][3]),
                      (self.board[1][3], self.board[2][2], self.board[3][1]))
        for a_condition in check_list:
            if self.win_conditions[0] == a_condition:
                print("Player 1 wins!")
                sys.exit()
            elif self.win_conditions[1] == a_condition:
                print("Player 2 wins!")
                sys.exit()
            elif self.turn_main_counter == 10:
                print("Draw!")
                sys.exit()


    def board_print(self):
        os.system("cls")
        print(f"{self.board['title']}\n{self.board[1][1]}{self.board['seperator']}{self.board[1][2]}{self.board['seperator']}{self.board[1][3]}\n"
              f"{self.board['lines'][0]}\n"
              f"{self.board[2][1]}{self.board['seperator']}{self.board[2][2]}{self.board['seperator']}{self.board[2][3]}\n"
              f"{self.board['lines'][0]}\n"
              f"{self.board[3][1]}{self.board['seperator']}{self.board[3][2]}{self.board['seperator']}{self.board[3][3]}")
