import turtle

top_x = 0
top_y = 100
base_left_x = -100
base_left_y = -100
base_right_x = 100
base_right_y = -100

def main():
    turtle.hideturtle()
    line(top_x, top_y, base_left_x, base_left_y, 'red')
    line(top_x, top_y, base_right_x, base_right_y, 'blue')
    line(base_left_x, base_left_y, base_right_x, base_right_y, 'green')

def line(startX, startY, endX, endY, color):
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(endX, endY)

main()