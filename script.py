# The script of the game goes in this file.
# Phil wuz here hurr durr.

# ----------
# -Defaults-
# ----------
# Defaults are sorta like global variables that we can call from and modify anywhere
# in the VN. They can persist across different files, need to check if they do across
# sessions.

default test = {0,1,2}

# Can predefine images, characters, sprite transforms, and more(?) to make the writing
# process a bit easier.
# Helps when you don't want to write "John Schnitzellbacher the Fourteenth" every other line.

image eileen happy = "eileen_happy_blue_dress.png"
image logo = "renpy logo.png"

define e = Character("Eileen")
define s = Character('Sylvie', color = "#ffffff")
define m = Character('Me', color = "#c8c8ff")


# We can also choose the specific location on the screen where characters exist, and
# can control which ones are in front of which.
    
transform bitLeft:
    xalign 0.03
    yalign 1.0

    # Things start here.
    # I wrote none of this dialogue btw lol.
    
label start:

    #play music "illurock.ogg" This doesn't exist yet
    # "bg meadow" is one file. Renpy can support spaces in images.
    # Common naming format for backgrounds is just "bg [name]".
    scene bg meadow
    with fade

    "After a short while, we reach the meadows just outside the neighborhood where we both live."

    "It's a scenic view I've grown used to. Autumn is especially beautiful here."

    "When we were children, we played in these meadows a lot, so they're full of memories."

    m "Hey... Umm..."

    show sylvie green smile
    with dissolve
        xalign 0.75
        yalign 1.0
        
    "She turns to me and smiles. She looks so welcoming that I feel my nervousness melt away."

    "I'll ask her...!"
    
    show sylvie green smile at right

    m "Ummm... Will you..."

    m "Will you be my artist for a visual novel?"

    show sylvie green surprised

    "Silence."

label leaving:

    s "I'll get right on it!"

    hide sylvie
    with dissolve

    "..."

    m "That wasn't what I meant!"
    
    
    # This ends the game.

    return
    
