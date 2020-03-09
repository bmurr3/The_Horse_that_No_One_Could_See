# The script of the game goes in this file.
# Phil wuz here hurr durr.

# NOTES:
# Can use https://www.renpy.org/doc/html/config.html#var-config.menu_include_disabled for greyed out text boxes.

# ----------
# -Defaults-
# ----------
# default test = {0,1,2} # Revertable set?
default test = [0,1,2]

image eileen happy = "eileen_happy_blue_dress.png"
image logo = "renpy logo.png"

define o = Character('OFFICER_NAME', color = "#ff5050")
define m = Character('Me', color = "#c8c8ff")
    
transform bitLeft:
    xalign 0.03
    yalign 1.0

label start:

    scene bg police station
    with fade

    "Start."
    
    m "Text."

    show OFFICER PLACEHOLDER with dissolve:
        xalign 0.75
        yalign 1.0

    o "Text."
    
    hide OFFICER PLACEHOLDER
    #no dissolve 4 u
    
    # IGNORE ME ----------------------------------------------------------
    #m "This choice will increment or decrement the TEST_INT variable."
    #menu:
    #    m "The starting value is [test]. [test] index 0 is [test[0]]."
    #    "Increment variable.":
    #        $ test[0] = test[0] + 1
    #    "Decrement variable.":
    #        $ test[0] = test[0] - 1
    #"The variable is now [test[0]]."
    #---------------------------------------------------------------------
    
    menu:
    
        "What now?":
            "An excellent question."

    menu:
    
        "Where do we want to go?"
        
        "Street (requires street.rpy)":
            jump street
            
        "Go back to start label.":
            jump start
    
        "End game.":
            return
    
    "Ending test."
    return
    
