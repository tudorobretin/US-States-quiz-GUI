from turtle import Turtle
import pandas


class Mechanics(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.guessed = []
        self.missed = []

    def write_state(self, guess, data):
        xcor = int(data[data.state == guess.title()].x)
        ycor = int(data[data.state == guess.title()].y)

        self.goto(xcor,ycor)
        self.write(guess.title())

    def check_guess(self, guess, states):
        to_return = False
        for state in states:
            if guess.lower() == state.lower() and guess.lower() not in self.guessed:
                self.guessed.append(guess.lower())
                self.score += 1
                print(self.guessed)
                to_return = True
        return to_return

    def print_missed_states(self, states_list):
        self.missed = [item for item in states_list if item.lower() not in self.guessed]
        print(self.missed)
        missed_df = pandas.DataFrame(self.missed)
        missed_df.to_csv("states_to_learn.csv")



