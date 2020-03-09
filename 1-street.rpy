# NOTES:
# At the end of each day, we can go back to a hotel room or something before exploring
# new areas the next day. We can use this time to give players a little log of notes or
# some other neat little gimmick so they can feel like they're making visible progress.
# Note to self: Implement this^

default BUS = 0
default SANITY = 0
default TIME = 3 # Can change this as we want, just keeping it for now since I think we
                 # wanna have limited time on the first tiime.
default DOC_PROG = 0
default GRL_PROG = 0
default DAD_PROG = 0
default FBI_PROG = 0

default DOC_TDY = False
default GRL_TDY = False
default DAD_TDY = False
default FBI_TDY = False

define v = Character("Dr. Arian", color = "ffffe0")
define g = Character("Ms. Grill", color = "ff0000")
define d = Character("Mr. Mann", color = "00ff00")
define h = Character("Hoodie Guy", color = "0000ff")

define m = Character("Me", color = "ffffff") # Unless we wanna give our protag a name, or let the
                               # player input their own. Either are simple to implement.

label street:
    
    # IGNORE ME -------------------------------------------
    #"Successfully loaded street.rpy."
    #"Attempting to get test value loaded from script."
    #"[test]. Success!"
    # -----------------------------------------------------
    
    
    # Dialogue for coming out of the police station and seeing stuff.
    
    
    "Here is where the player chooses who to interact with first."
   
label choices:
   
    menu:
        "Dr. Veter N. Arian" if (DOC_TDY == False):
            jump DOC
        "Hot Grill (ouch)" if (GRL_TDY == False):
            jump GRL
        "Worried Man (Father)" if (TIME > 2 and DAD_TDY == False):
            jump DAD
        "Hoodie Man" if (FBI_TDY == False):
            jump FBI
        "Explore around town.":
            jump explore
        "Turn in for the day." if (TIME <=0 ):
            jump DAY_OVER    
        "Take a bus. (Do we want this somewhere else?)":
            if (BUS < 7):
                m "But why would I take a bus? I have a car."
                $ BUS += 1
                jump choices
            else:
                m "...Alright, I guess it would save fuel."
                "ded"
                return #replace with appropriate jump
    
label DOC:
    # Doctor branch
    
    $ TIME -= 1
    $ DOC_PROG +=1
    $ DOC_TDY = True
    jump choices
    
label GRL:
    # Grill branch
    
    $ TIME -= 1
    $ GRL_PROG +=1
    $ GRL_TDY = True
    jump choices

label DAD:
    # Dad branch
    
    $ TIME -= 1
    $ DAD_PROG +=1
    $ DAD_TDY = True
    jump choices

label FBI:
    # Hoodie Man branch
    
    $ TIME -= 1
    $ FBI_PROG +=1
    $ FBI_TDY = True
    jump choices
    
label explore:

    "Stuff to see, places to visit."

label DAY_OVER:
    
    
    "Time to go home!"
    
