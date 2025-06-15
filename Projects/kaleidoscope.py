def main():
    import turtle
    print('\nKaleidoscope, by Jayden\n')
    print('This is a kaleidoscope program.')
    print('This kaleidoscope can be customized by you!')
    print('You can:\n')
    print('1. Change the background color.')
    print('2. Change the pen color.')
    print('4. Change the degree the pen turns.')
    print('5. Change the speed of the turtle.')
    print('6. Change number of polygons.')
    print('7. Change the kaleidoscope to multiple colors.')
    print('Alright, let\'s get started!')

    # Lists of polygons and colors
    colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple', 'pink', 'brown', 'black', 'white', 'gray', 'multicolor']
    speeds = ['fastest', 'fast', 'normal', 'slow', 'slowest']

    # Start gathering customization information
    bg_color = input('\nWhat color would you like the background to be? ')
    while bg_color not in colors:
        print('That is not a valid color.')
        bg_color = input('What color would you like the background to be? ')

    pen_color = input('\nWhat color would you like the pen to be? If you would like multiple colors, type "multicolor". ')
    while pen_color not in colors:
        print('That is not a valid color.')
        pen_color = input('What color would you like the pen to be? If you would like multiple colors, type "multicolor". ')

    degree = input('\nWhat degree would you like the pen to turn? For example, if you want a square, you would put 90 + 1 = 91 degrees. ')
    try:
        degree = int(degree)
    except ValueError:
        print('That is not a valid degree. The degree will be set to 91.')
        degree = 91

    speed = input('\nWhat speed would you like the turtle to be? ')
    if speed not in speeds:
        try:
            speed = int(speed)
        except ValueError:
            print('That is not a valid speed. The speed will be set to normal.')
            speed = 4
    
    num_polygons = input('\nHow many polygons would you like to draw? (if you want to do many polygons, type "many", and it will set to 1000.) ')
    try:
        num_polygons = int(num_polygons)
    except ValueError:
        if num_polygons == 'many':
            num_polygons = 1000
        else:
            print('That is not a valid number. The number of polygons will be set to 200.')
            num_polygons = 200
    
    multiple_colors = input('\nWould you like the kaleidoscope to be multiple colors? (yes or no) '); multiple_colors = multiple_colors.lower()
    if multiple_colors == 'yes':
        multiple_colors = True
    else:
        multiple_colors = False
    
    if multiple_colors == True:
        colors_draw = input('\nWhat colors would you like the kaleidoscope to be? (separate the colors with commas) '); colors_draw = colors_draw.split(',')
        for i in range(len(colors_draw)):
            while colors_draw[i] not in colors:
                print('There is one or more colors you\'ve entered that is not valid.')
                colors_draw[i] = input('What colors would you like the kaleidoscope to be? (separate the colors with commas) ').split(',')
    else:
        colors_draw = [pen_color]
    
    def translate_speed(speed):
        if speed == 'fastest':
            return 0
        elif speed == 'fast':
            return 10
        elif speed == 'normal':
            return 7
        elif speed == 'slow':
            return 4
        elif speed == 'slowest':
            return 2
        else:
            return speed
    # define the function to draw the kaleidoscope
    def draw_kaleidoscope():
        turtle.bgcolor(bg_color)
        turtle.speed(translate_speed(speed))
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        if multiple_colors:
            pass
        else:
            turtle.color(pen_color)

        length = 1  # Initial length of the lines
        for i in range(num_polygons):
            if multiple_colors:
                turtle.color(colors_draw[i % len(colors_draw)])
            for _ in range(int(360 / degree)):
                turtle.forward(length)
                turtle.right(degree)
            turtle.right(360 / num_polygons)
            length += 1  # Increase the length of the lines for each polygon

    draw_kaleidoscope()
    turtle.done()

if __name__ == '__main__':
    main()