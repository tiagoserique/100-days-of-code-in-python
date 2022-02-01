import turtle
import pandas


FONT = ("Courier", 10, "normal")


screen = turtle.Screen()
screen.title("U.S States Game")
screen.tracer(0)

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_states 		= data.state.to_list()
guessed_states 	= []
while ( len(guessed_states) < 50 ):
	screen.update()

	answer_state = turtle.textinput(
		title=f"{len(guessed_states)}/50 states correct", 
		prompt="What's another state's name?"
	).title()


	if ( answer_state == "Exit" ):
		missing_states = [state for state in all_states 
									if ( state not in guessed_states )]

		new_data = pandas.DataFrame(missing_states)
		new_data.to_csv("states_to_learn.csv")
		break
	if ( answer_state in all_states ):
		guessed_states.append(answer_state)
		state_data = data[data.state == answer_state]

		new_turtle = turtle.Turtle()
		new_turtle.hideturtle()
		new_turtle.penup()

		coordinates = (int(state_data.x), int(state_data.y))
		new_turtle.goto(coordinates)

		state_name = state_data.state.item()
		new_turtle.write(f"{state_name}", align="center", font=FONT)


	screen.update()
