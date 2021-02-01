import turtle
from role_call_lib.delbertina import write_name_delbertina
from role_call_lib.awesomea11en import write_name_awesomea11en

# Add a file to the role_call_lib folder for your username
# Use the turtle library to write your name out (no more than 50 tall)
# Add the file as an import to this file
# Call your function after any existing ones

# Variables
turtle_name_index = 0
turtle_offset_x = 10
turtle_offset_y = 10
turtle_name_padding_y = 10
turtle_name_height = 50
screen_size_x = 800
screen_size_y = 800


def clean_up_draw(input_turtle):
    # Take the pen off the writing surface
    input_turtle.penup()
    # Send the turtle to the input location
    input_turtle.goto((0 - (screen_size_x / 2) + turtle_offset_x),
                      ((screen_size_y / 2) - turtle_offset_y
                       - (turtle_name_index * (turtle_name_height + turtle_name_padding_y))))
    # Reset the turtle's rotation to be pointing right
    input_turtle_rotation = input_turtle.heading()
    input_turtle.left(input_turtle_rotation)
    # Reset color to black
    input_turtle.color("black")


# Set the screen dimensions
turtle.Screen().setup(screen_size_x, screen_size_y)
# Create an instance of a turtle
typing_turtle = turtle.Turtle()


# (Copy and change username to your file)
clean_up_draw(typing_turtle)
turtle_name_index += 1
write_name_delbertina(typing_turtle)

# awesomea11en
clean_up_draw(typing_turtle)
turtle_name_index += 1
write_name_awesomea11en(typing_turtle)

# Add yours here

turtle.done()
