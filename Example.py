from Twitch import cmd, Bot
from Xbox import *
# Grabs the twitch bot and chucks it lowercase (so its easier to type out phew)
bot = Bot()

# ============================
# TEMPLATE
# ============================

# @cmd(bot, "cmdname")
# def act(msg):
#   Action

# ============================
# DRIVING (Temp Solutions until LT AND RT Work without stopping every other command)
# ============================

# ACCELERATE
@cmd(bot, "drive")
def act(msg):
    HoldButton(XBOX_A)
    ReleaseButton(XBOX_B)
    print(msg)
# STOP
@cmd(bot, "stop")
def act(msg):
    ReleaseButton(XBOX_A)
    ReleaseButton(XBOX_B)
    print(msg)
# BRAKE/REVERSE
@cmd(bot, "brake")
def act(msg):
    HoldButton(XBOX_B)
    ReleaseButton(XBOX_A)
    print(msg)

# Steer Left
@cmd(bot, "turn left")
def act(msg):
    XAxis(XBOX_AXISML)
    print(msg)
# Steer Reset
@cmd(bot, "straight")
def act(msg):
    XAxis(XBOX_AXISC)
    print(msg)
# Steer Right
@cmd(bot, "turn right")
def act(msg):
    XAxis(XBOX_AXISMR)
    print(msg)

# ============================
# A, B, X, Y Buttons
# ============================

@cmd(bot, "a")
def act(msg):
    #Releases it if it's already been held down (from driving)
    ReleaseButton(XBOX_A)
    time.sleep(0.1)
    PressButton(XBOX_A, 0.2)
    print(msg)

@cmd(bot, "b")
def act(msg):
    #Releases it if it's already been held down (from driving)
    ReleaseButton(XBOX_B)
    time.sleep(0.1)
    PressButton(XBOX_B, 0.2)
    print(msg)

@cmd(bot, "x")
def act(msg):
    PressButton(XBOX_X, 0.2)
    print(msg)

@cmd(bot, "y")
def act(msg):
    PressButton(XBOX_Y, 0.2)
    print(msg)

# Shoulder Buttons
@cmd(bot, "lb")
def act(msg):
    PressButton(XBOX_LB, 0.2)
    print(msg)

@cmd(bot, "rb")
def act(msg):
    PressButton(XBOX_RB, 0.2)
    print(msg)

# Temp DPad Buttons
@cmd(bot, "up")
def act(msg):
    PressButton(UPTEMP, 0.2)
    print(msg)

@cmd(bot, "down")
def act(msg):
    PressButton(DOWNTEMP, 0.2)
    print(msg)

@cmd(bot, "left")
def act(msg):
    PressButton(LEFTTEMP, 0.2)
    print(msg)

@cmd(bot, "right")
def act(msg):
    PressButton(RIGHTTEMP, 0.2)
    print(msg)

if __name__ == "__main__":
    bot.run()

# BROKEN AF
#@cmd(bot, "lt")
#def act(msg):
#    PressLT(5)
#    print(msg)

#@cmd(bot, "rt")
#async def act(msg):
#    PressRT(5)
#    print(msg)
