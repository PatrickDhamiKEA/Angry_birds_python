from random import randint


class Bird:
    random_pos = [randint(0, 9), randint(0, 4)]
    start_pos = random_pos
    current_pos = random_pos

    def __init__(self):
        self.bird_marker = 'B'
        self.dir_right = True
        self.dir_left = False
        self.dir_up = False
        self.dir_down = False

    def turn_left(self):
        if self.dir_left:
            self.dir_left = False
            self.dir_up = False
            self.dir_right = False
            self.dir_down = True

        elif self.dir_down:
            self.dir_left = False
            self.dir_up = False
            self.dir_down = False
            self.dir_right = True

        elif self.dir_right:
            self.dir_left = False
            self.dir_right = False
            self.dir_down = False
            self.dir_up = True

        elif self.dir_up:
            self.dir_up = False
            self.dir_right = False
            self.dir_down = False
            self.dir_left = True

    def turn_right(self):
        if self.dir_left:
            self.dir_left = False
            self.dir_right = False
            self.dir_down = False
            self.dir_up = True

        elif self.dir_down:
            self.dir_up = False
            self.dir_down = False
            self.dir_right = False
            self.dir_left = True

        elif self.dir_right:
            self.dir_left = False
            self.dir_right = False
            self.dir_up = False
            self.dir_down = True

        elif self.dir_up:
            self.dir_up = False
            self.dir_down = False
            self.dir_left = False
            self.dir_right = True

    def move_forward(self):
        if self.dir_right:
            self.current_pos[1] = self.current_pos[1] + 1
        elif self.dir_left:
            self.current_pos[1] = self.current_pos[1] - 1
        elif self.dir_up:
            self.current_pos[0] = self.current_pos[0] - 1
        elif self.dir_down:
            self.current_pos[0] = self.current_pos[0] + 1

    def bird_lost(self):
        print("Pig won the game and Bird lost")


class Pig:
    random_pig_pos = [randint(0, 9), randint(5, 9)]
    pos = random_pig_pos

    def __init__(self):
        self.pig_marker = 'P'

    def pig_lost(self):
        print("Bird won the game and Pig lost")


class Board:
    def __init__(self):
        self.board = [['*' for i in range(10)] for i in range(10)]
        self.bird = Bird()
        self.pig = Pig()

    def set_bird_start_pos(self):
        self.board[self.bird.start_pos[0]][self.bird.start_pos[1]] = self.bird.bird_marker

    def set_pig_pos(self):
        self.board[self.pig.pos[0]][self.pig.pos[1]] = self.pig.pig_marker

    def display_board(self):
        self.set_bird_start_pos()
        self.set_pig_pos()
        for row in self.board:
            print('  '.join(row))
        print('\n')


class Workspace:
    def __init__(self):
        self.instructions = 'Bird starts facing right.\nMove forward press: f\nTurn left press: l\nTurn right press: r'
        self.moves = []
        self.bird = Bird()
        self.pig = Pig()

    def display_instructions(self):
        print(self.instructions)

    def get_user_moves(self):
        while True:
            user_input = input('Move: ')
            if user_input == 'f' or user_input == 'r' or user_input == 'l':
                self.moves.append(user_input)
            elif user_input == 'q':
                break
            else:
                print('Invalid move')

        Workspace.move_bird(self)

    def move_bird(self):
        for i in self.moves:
            if i == 'f':
                self.bird.move_forward()
            elif i == 'r':
                self.bird.turn_right()
            elif i == 'l':
                self.bird.turn_left()

        Workspace.check_result(self)

    def check_result(self):
        if self.bird.current_pos == self.pig.pos:
            print('Birds final position: ', self.bird.current_pos)
            print('Pigs final position: ', self.pig.pos)
            self.pig.pig_lost()
        else:
            print('Birds final position: ', self.bird.current_pos)
            print('Pigs final position: ', self.pig.pos)
            self.bird.bird_lost()


class Game:
    def __init__(self):
        Board().display_board()
        Workspace().display_instructions()
        Workspace().get_user_moves()


Game()
