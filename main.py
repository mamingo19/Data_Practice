import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = []

# Keep asking for input until user quits
while len(states) < 50:
    answer_state = screen.textinput(f"{len(states)}/50 states already guessed", "What is another state's name? ").title().strip()
    if answer_state == "Exit":
        missing_states = [state for state in data.state.value if state not in states]
        new_dat = pandas.DataFrame(missing_states)
        new_dat.to_csv("LearnThisBruh.csv")
        print(new_dat)
        break
    # Check if the state is in the data
    if answer_state in data.state.values:
        states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_cor = data[data.state == answer_state]
        t.goto(state_cor.x.item(), state_cor.y.item())
        t.write(answer_state)
    else:
        print(f"'{answer_state}' is not a valid state name.")

screen.exitonclick()