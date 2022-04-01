import turtle
import pandas
from mechanics import Mechanics

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(height=490, width=725)

mechanics = Mechanics()

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

while mechanics.score < 50:
    answer_state = screen.textinput(title=f"{mechanics.score}/50 States Correct", prompt="What's another state?")
    if answer_state.lower() == "exit":
        break
    if mechanics.check_guess(guess=answer_state, states=states_list):
        mechanics.write_state(guess=answer_state, data=data)

mechanics.print_missed_states(states_list)