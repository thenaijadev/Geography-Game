import turtle

import pandas

screen = turtle.Screen()
screen.title("U.s States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []


while len(guessed_states) <50:
    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states guessed.", prompt="What is another state")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)


print(answer_state)
turtle.mainloop()
