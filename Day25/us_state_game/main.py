import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

print(all_states)
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name? ")
# print(answer_state)

guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title= f"{len(guessed_state)}/50 States Correct", prompt="What's another state's name? ").title()
    if answer_state == "Exit":
        missing_States =[state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_States)
        new_data.to_csv("stated_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data= data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)



