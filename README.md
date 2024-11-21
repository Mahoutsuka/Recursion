# Lab 07: Recursion

Collaboration: *enter names of others you worked with and any outside resources you referenced*

This repository contains the following files:

- README.md:        this file
- recursive.py:     where you will write your code
- runtests.py:      runs tests for your code and for generating images to submit
- `nested_squares-400-40.png`:  a blank image file
- `quilt-518-128.png`:          a blank image file
- `shrub-100-15-8-10.png`:      a blank image file


## Assignment Expectations

Requirements of this lab:

1. Function Requirements
  * Warm-up Task: sum_digits
          * passes all tests and produces correct sum
          * has an explicit base case and correctly handles it 
          * correctly handles recursive call
          * the implementation is fully recursive; no loops are found
          * int not converted to str
          * clean and interpretable code with appropriate comments
  * Task 1: bedtime
          * passes all tests
          * has an explicit base case and correctly handles it
          * correct calls to `first_sentence` and `last_sentence`
          * the implementation is fully recursive; no loops are found
          * clean and interpretable code with appropriate comments
  * Task 2: squares
          * correctly returns the number of squares
          * `draw_nested_squares(400, 40, PURPLE, WHITE)` generates correct figure
          * `draw_nested_squares` uses only the allowed turtle commands
          * `draw_nested_squares` uses `color`, `other_color` rather than `WHITE`, `PURPLE`
          * the implementation is fully recursive; no loops
          * clean and interpretable code with appropriate comments
  * Task 3: quilt
          * correctly returns the number of squares
          * `draw_quilt(512, 128, PURPLE, GOLD)` generates correct figure
          * `draw_quilt` uses only the allowed turtle commands
          * `draw_quilt` uses `color`, `other_color` rather than `GOLD`, `PURPLE`
          * the implementation is fully recursive; no loops are found
          * clean and interpretable code with appropriate comments
  * Task 4: shrub
          * correctly returns the total branch length
          * `draw_shrub(100, 15, 0.8, 10)` generates correct figure
          * `draw_shrub` uses only the allowed turtle commands
          * the implementation is fully recursive; no loops are found
          * clean and interpretable code with appropriate comments


2. Program Output

The following image files should be correctly created using `python3 runtests.py final` and submitted along with your code:
   * `nested_squares-400-40.png` contains the correct plot for `draw_nested_squares(400, 40, PURPLE, WHITE)`
   * `quilt-518-128.png` contains the correct plot for `draw_quilt(512, 128, PURPLE, GOLD)`
   * `shrub-100-15-8-10.png` contains the correct plot for `draw_shrub(100, 15, 0.8, 10)`

3. Style and Global Requirements

   * Does not use language features that were not discussed in class
   * Code makes good use of variable names, and is clear and readable
   * 1-3 appropriate comments per function, explaining complex logic
   
