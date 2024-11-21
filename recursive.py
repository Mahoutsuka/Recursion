from turtle import *


def sum_digits(num):
    """Given a non-negative integer num, return the sum of the
    digits of num.

    >>> sum_digits(1)
    1
    >>> sum_digits(8)
    8
    >>> sum_digits(90)
    9
    >>> sum_digits(178)
    16
    >>> sum_digits(1234567890)
    45
    """
    #base case if num is 0, then return 0
    if num == 0:
        return 0
    #else, find the last digit of the number and recursively call the function on the number without the last digit
    else:
        return num%10 + sum_digits(num//10)




def first_sentence(object, subject):
    """Given the strings object and subject, returns a string 
    representing the first sentence of the story about those
    characters. 
    
    Your solutions to bedtime_story should call this function.

    DO NOT MODIFY.
    """
    return "The mother of the " + object + " told a story about a " + subject + "..."


def last_sentence(object):
    """Given the string object, return a string representing
    the second (last) sentence of the story about that character.

    Your solutions to bedtime_story should call this function.
   
    DO NOT MODIFY.
    """
    return "and then the " + object + " fell asleep."


def bedtime_story(list_of_characters):
    """
    Main (recursive) function for producing a bedtime story based on a list of
    strings (story characters). Returns a list of strings where each element is
    a sentence in the bedtime story.

    Inspired by https://stackoverflow.com/questions/3021/what-is-recursion-and-when-should-i-use-it
    
    >>> bedtime_story(['ant', 'fly', 'cow'])
    ['The mother of the ant told a story about a fly...', 
     'The mother of the fly told a story about a cow...', 
     'and then the fly fell asleep.',
     'and then the ant fell asleep.']
    """

    story = []
    #if the length of the list of character is less than 2 then return an empty list
    if len(list_of_characters) < 2:
        return []

    else: 
        #adds the first sentence with the first two characters to the list
        story += [first_sentence(list_of_characters[0],list_of_characters[1])]
        #recursively call the function each time excluding the first element in the list of characters
        story += bedtime_story (list_of_characters[1:])
        #once the recursive call ends, add the last sentence to the accumulator list from the most recent recursive call to the first call
        story += [last_sentence(list_of_characters[0])]
        return story
    

def draw_square(side_length, color):
    """Draws a single square with the specified side length and color.
    
    Note: side_length is an int and color is a string. Assume that
    the turtle is positioned at the bottom left corner of the square,
    facing east. 

    Your solutions to draw_nested_squares and draw_quilt should
    call this function to draw their squares.
    
    DO NOT MODIFY.
    """
    if color is None:
        print("Error: IVALID COLOR PASSED TO draw_square")
        return None
    down()
    pen(fillcolor = color)
    begin_fill()
    for _ in range(4):
        forward(side_length)
        left(90)
    end_fill()
    up()


def draw_nested_squares(size, gap, color, other_color):
    """Draws the nested squares as described in the lab writeup.

    Assume that the turtle is positioned at the bottom left
    of the biggest square we must draw and facing east. Return the 
    total number of squares drawn.
    """
    #if the length of the square is less than the size of the gap then a square wouldn't be drawn, else draw a square
    if size < gap:
        return 0
    else: 
        draw_square(size,color)
        #reposition the turtle to start at the bottom left corner of the square facing east
        fd(gap)
        lt(90)
        fd (gap)
        rt(90)
        #recursively call the function, reducing the size of the square and swapping the color of the square
        num_squares = draw_nested_squares (size-(2*gap), gap, other_color, color)
    return 1 + num_squares



def draw_quilt(quilt_size, min_size, quilt_color, other_color):
    """Draws a colored quilt as described in the lab writeup.
    Assume that the turtle is positioned at the bottom left
    end point of quilt facing east before this function is called.
    """

    #if the quilt is less than or equal to the minimum size draw one square of quilt colorand return 1
    if quilt_size <= min_size:
        draw_square(quilt_size,quilt_color)
        return 1
    else:
        #draws the bottom left corner square reposition to the bottom left corner of the top right square and draws top right square
        draw_square (quilt_size/2,quilt_color)
        fd(quilt_size/2)
        lt(90)
        fd (quilt_size/2)
        rt(90)
        draw_square(quilt_size/2,quilt_color)
        #reposition to the top left and draws the top left quilt
        bk(quilt_size/2)
        top_corner_squares = draw_quilt(quilt_size/2,min_size,other_color,quilt_color)
        #reposition to the the bottom right and draws the bottom right quilt
        fd(quilt_size/2)
        rt(90)
        fd(quilt_size/2)
        lt(90)
        bot_corner_squares = draw_quilt(quilt_size/2,min_size, other_color, quilt_color)
        #after finishing the bottom right quilt, reposition back to where the turtle started before drawing the top left quilt
        bk(quilt_size/2)
        return 2 + top_corner_squares + bot_corner_squares
    
        
        

def draw_shrub(trunk_length, angle, shrink_factor, min_length):
    """
    Draws a shrub as specified in Lab 7 Task 4.
    Returns the total length (float) of branches (including the trunk).
    Assume that the turtle is positioned at the base of the main
    trunk facing north before this function is called.
    """
    # if the length of the trunk is less than the minimum length return 0 
    if trunk_length < min_length:
        return 0 
    #else draws a trunk and the right branches of the tree
    else:
        fd(trunk_length)
        rt(angle)
        right_tree = draw_shrub (trunk_length*(shrink_factor), angle, shrink_factor, min_length)
        #reposition the turtle to be facing the left side of the branch and draws the left side of the branch
        lt(2*angle)
        left_tree = draw_shrub (trunk_length*(shrink_factor**2),angle, shrink_factor, min_length)
        #reposition the turtle to the place where it was before it began drawing the right side of the branch
        right(angle)
        bk(trunk_length)
        return trunk_length + right_tree + left_tree
        
        
        

        #draw_shrub (trunk_length*shrink_factor,360-(angle), shrink_factor, min_length)

