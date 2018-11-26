"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Steven Kline.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
turtleMom = rg.SimpleTurtle()
turtleDad = rg.SimpleTurtle()

turtleDad.pen = rg.Pen('blue', 3)
turtleMom.pen = rg.Pen('red', 3)
turtleMom.speed = 1000
turtleDad.speed = 500
bigness = 10
sids=3
for k in range(18):
    turtleMom.draw_regular_polygon(6, bigness)
    turtleMom.pen_up()
    turtleMom.right(15)
    turtleMom.pen_down()
    bigness = bigness*1.75

for k in range(18):
    turtleDad.draw_regular_polygon(sids, 60)
    sids=sids+1

window.close_on_mouse_click()