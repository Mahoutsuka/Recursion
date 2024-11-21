from turtle import *
from PIL import Image
from recursive import sum_digits, bedtime_story
from recursive import draw_nested_squares, draw_quilt, draw_shrub

##########################################################
# OUR PROVIDED TESTS
#
# Tests that we provide so that you can see if your 
# functions are working correctly.
##########################################################

def sum_digits_test1():
    result = sum_digits(1)
    print('sum_digits(1)')
    print("  should return:  1")
    print("  yours returned: " + str(result))

def sum_digits_test2():
    result = sum_digits(8)
    print('sum_digits(8)')
    print("  should return:  8")
    print("  yours returned: " + str(result))

def sum_digits_test3():
    result = sum_digits(90)
    print('sum_digits(90)')
    print("  should return:  9")
    print("  yours returned: " + str(result))

def sum_digits_test4():
    result = sum_digits(178)
    print('sum_digits(178)')
    print("  should return:  16")
    print("  yours returned: " + str(result))

def sum_digits_test5():
    result = sum_digits(1234567890)
    print('sum_digits(1234567890)')
    print("  should return:  45")
    print("  yours returned: " + str(result))

##########################################################
# USER INPUT TESTS
#
# Tests that use user input to display
# different outputs for testing.
##########################################################

def bedtime_story_userinput(animals_list):
    story_list = bedtime_story(animals_list)

    print('bedtime_story(' + str(animals_list) + ')')
    print("Yours returned: ")
    format_print(story_list)
    print("...compare to lab handout to see what should be returned!")

    # type check for returned value
    if type(story_list) == str:
        print("\tWarning: bedtime_story(..) returned a str, not a list.")

def draw_nested_squares_userinput(size, gap):
    # Just in case inputs are still strings
    size = int(size)
    gap = int(gap)

    # Turtle stuff
    initialize_turtle(size) # creates turtle world and positions turtle in the lower left.
    result = draw_nested_squares(size, gap, PURPLE, WHITE)
    # Saves the drawing to a file.
    if len(args) > 3 and args[3] == "save":
        getscreen().getcanvas().postscript(file="draw_squares-{}-{}.ps".format(size, gap))
    exitonclick() # waits for the user to click the mouse before closing the window

    # Print actual/expected
    print("Your function call -> returned value: ")
    print('\tdraw_nested_squares(' + str(size) + ', ' + str(gap) + ') -> ' + str(result))
    print("Example function calls -> returned values: ")
    print("\tdraw_nested_squares(400, 40) -> 5")
    print("\tdraw_nested_squares(400, 20) -> 10")
    print("\tdraw_nested_squares(400, 10) -> 20")

def draw_quilt_userinput(quilt_size, patch_size):
    # Just in case inputs are still strings
    quilt_size = int(quilt_size)
    patch_size = int(patch_size)

    # Turtle stuff
    initialize_turtle(quilt_size)
    result = draw_quilt(quilt_size, patch_size, PURPLE, GOLD)
    if len(args) > 3 and args[3] == "save":
        getscreen().getcanvas().postscript(file="draw_quilt-{}-{}.ps".format(quilt_size, patch_size))
    exitonclick() # waits for the user to click the mouse before closing the window

    # Print actual/expected
    print("Your function call -> returned value: ")
    print('\tdraw_quilt(' + str(quilt_size) + ', ' + str(patch_size) + ') -> ' + str(result))
    print("\t...compare to lab handout to see what should be returned!")

def draw_shrub_userinput(trunk_length, angle, shrink_factor, min_length):
    # Just in case inputs are still strings
    trunk_length = float(trunk_length)
    angle = float(angle)
    shrink_factor = float(shrink_factor)
    min_length = float(min_length)

    # Turtle stuff
    initialize_turtle_for_shrub()
    speed(0) # 0 -> fastest, 6 -> slowest
    num_branches = draw_shrub(trunk_length, angle, shrink_factor, min_length)
    if len(args) > 5 and args[5] == "save":
        getscreen().getcanvas().postscript(file="shrub-{}-{}-{}-{}.ps".format(trunk_length, angle, shrink_factor, min_length))
    exitonclick() # waits for the user to click the mouse before closing the window

    # Print actual/expected
    rounded_branches = round(num_branches,2)
    print("Your function call -> returned value: ")
    print('\tdraw_shrub({}, {}, {}, {}) -> {}'.format(trunk_length, angle, shrink_factor, min_length, rounded_branches))
    print("\t...compare to lab handout to see what should be returned!")

##########################################################
# TEST RUNNER
#
# Runs tests for questions 0 through 4.
# In the Terminal, type:
#     python runtests.py qN
# where N is the question number you want to test.
##########################################################

def get_command_line_args():
    from sys import argv
    return argv[1:]

def format_print(story_list):
    """ Pretty-prints the bedtime story output"""
    n = len(story_list)
    # Prints the first half of the list, with increasing indentation.
    for i in range(n // 2):
        print("   " * i + story_list[i])
    # Prints the second half of the list, with decreasing indentation.
    for i in range(n // 2, n):
        print(("   " * (n - i - 1)) + story_list[i])

def initialize_turtle(size):
    """Sets up the window given size (int) and initializes the
    turtle to be at the bottom left corner of the pattern facing
    east (the default direction).
    
    DO NOT MODIFY.
    """
    # Creates a turtle window
    padding = 50
    setup(width = size + padding, height = size + padding)
    reset()

    # Configures the turtle's line width and speed
    pensize(1) 
    speed(0)   # 0=fastest, 1=slowest, 6=normal

    # By default turtle starts at (0,0), the center of the screen
    # and faces east. We move it to the bottom left corner of the
    # pattern.
    up()
    goto(-size/2, -size/2)

def initialize_turtle_for_shrub():
    """Sets up the window and initializes the turtle to be at the 
    base of the main trunk facing north. 
    
    DO NOT MODIFY.
    """
    # Creates a turtle window
    setup(width=600, height=600)
    reset()

    # Configures the turtle's line width and speed
    pensize(1) 
    speed(0)   # 0=fastest, 1=slowest, 6=normal

    # By default turtle starts at (0,0), the center of the screen 
    # and faces east. We move it to a reasonable spot for a shrub
    # and point it north.
    up()
    goto(-100, -200)
    left(90)
    down()

##########################################################
# FINAL IMAGE UTILITIS
#
# Utilities for creating images to save final answers
# In the Terminal, type:
#     python runtests.py final
##########################################################


def save_current_turtle_screen(base):
    """Saves the current turtle image to a postscript file,
    then uses the pillow library to convert the postscript
    to a png image with the same basename.

    DO NOT MODIFY.
    """
    ps = base+".ps"
    png = base+".png"

    # Saves the drawing to a file.
    getscreen().getcanvas().postscript(file=ps)
    img = Image.open(ps)
    img.save(png)

def save_nested_squares_final(size, gap, base):
    """Calls the draw_nested_squares recursive function and
    saves the result as an image file.

    DO NOT MODIFY.
    """
    # Turtle stuff
    initialize_turtle(size) # creates turtle world and positions turtle in the lower left.

    result = draw_nested_squares(size, gap, PURPLE, WHITE)
    save_current_turtle_screen(base)

    
def save_quilt_final(quilt_size, patch_size, base):
    """Calls the draw_quilt recursive function and
    saves the result as an image file.

    DO NOT MODIFY.
    """
    # Turtle stuff
    initialize_turtle(quilt_size)
    result = draw_quilt(quilt_size, patch_size, PURPLE, GOLD)
    save_current_turtle_screen(base)

def save_shrub_final(trunk_length, angle, shrink_factor, min_length, base):
    """Calls the draw_shrub recursive function and
    saves the result as an image file.

    DO NOT MODIFY.
    """
    # Turtle stuff
    initialize_turtle_for_shrub()
    speed(0)
    num_branches = draw_shrub(trunk_length, angle, shrink_factor, min_length)
    save_current_turtle_screen(base)

if __name__ == "__main__":
    args = get_command_line_args() 
    PURPLE = '#500082'  # Williams purple
    WHITE = '#FFFFFF'   
    GOLD = '#FFBE0A'    # Williams gold
    if len(args) == 0:  # if there are no command-line arguments
        print("Please specify the question: q0, q1, q2, q3, q4", "final")
    else:
        which_question = args[0]  # reads the first command-line argument
        if which_question == "q0":
            sum_digits_test1()
            sum_digits_test2()
            sum_digits_test3()
            sum_digits_test4()
            sum_digits_test5()
        elif which_question == "q1":
            if len(args) < 2:
                print("Please also specify one (or more) animals, e.g.")
                print("  python3 runtests.py q1 parrot cow flamingo heron")            
            else:
                bedtime_story_userinput(args[1:])
        elif which_question == "q2":
            if len(args) < 3:
                print("Please also specify the size and gap, e.g.")
                print("  python3 runtests.py q2 400 20")
            else:
                size = int(args[1])
                gap = int(args[2])
                draw_nested_squares_userinput(size, gap)
        elif which_question == "q3":
            if len(args) < 3:
                print("Please also specify the quilt size and patch size, e.g.")
                print("  python3 runtests.py q3 512 128")
            else:
                quilt_size = int(args[1])
                patch_size = int(args[2])
                draw_quilt_userinput(args[1], args[2])
        elif which_question == "q4":
            if len(args) < 5:
                print("Please also specify the trunk length, angle, shrink factor, and min length, e.g.")
                print("  python3 runtests.py q4 100 15 0.8 50")
            else:
                trunk_length = float(args[1])
                angle = float(args[2])
                shrink_factor = float(args[3])
                min_length = float(args[4])
                draw_shrub_userinput(trunk_length, angle, shrink_factor, min_length)
        elif which_question == "final":
            # calls functions to save each recursively generated image to a file
            # so that the result can be easily viewed and submitted 
            try:
                save_nested_squares_final(400, 40, "nested_squares-400-40")
            except Exception as ex:
                print("Error occurred in nested_squares(400, 40):", ex)

            try:
                save_quilt_final(512, 128, "quilt-518-128")
            except Exception as ex:
                print("Error occurred in draw_quilt(518, 128):", ex)

            try:
                save_shrub_final(100, 15, 0.8, 10, "shrub-100-15-8-10")
            except Exception as ex:
                print("Error occurred in draw_shrub(100, 15, 0.8, 10):", ex)

        else:
            print("Question not recognized: " + which_question)
