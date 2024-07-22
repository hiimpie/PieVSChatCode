#XBOX 360 VIRTUAL CONTROLLER
import time
import pyvjoy

joystick = pyvjoy.VJoyDevice(1)  # Assuming you are using the first virtual joystick device

# XBOX 360 BUTTONS
XBOX_A = 1
XBOX_B = 2
XBOX_X = 3
XBOX_Y = 4
XBOX_LB = 5
XBOX_RB = 6

# XBOX DPAD
DP_UP = 0
DP_UP_RIGHT = 1
DP_RIGHT = 2
DP_DOWN_RIGHT = 3
DP_DOWN = 4
DP_DOWN_LEFT = 5
DP_LEFT = 6
DP_UP_LEFT = 7
DP_RESET = -1

#Temp DPad Alternative
UPTEMP = 29
DOWNTEMP = 30
LEFTTEMP = 31
RIGHTTEMP = 32

XBOX_TFULL = 32767
XBOX_TZERO = 0

XBOX_AXISL = 0x1
XBOX_AXISML = 0x2000
XBOX_AXISC = 0x4000
XBOX_AXISMR = 0x6000
XBOX_AXISR = 0x8000


def HoldButton(button_id):
    joystick.set_button(button_id, 1)

def ReleaseButton(button_id):
    joystick.set_button(button_id, 0)

def PressButton(button_id, seconds):
    joystick.set_button(button_id, 1)
    time.sleep(seconds)
    joystick.set_button(button_id, 0)

def XAxis(direction):
    joystick.set_axis(pyvjoy.HID_USAGE_X, direction)

def HoldDPad(direction):
    joystick.set_cont_pov(pyvjoy.HID_USAGE_POV, direction * 4500)

def HoldLT(value):
    joystick.set_axis(pyvjoy.HID_USAGE_Z, value)

def HoldRT(value):
    joystick.set_axis(pyvjoy.HID_USAGE_RZ, value)

def ReleaseT():
    HoldLT(XBOX_TZERO)
    HoldRT(XBOX_TZERO)

# DOESNT WORK
#def PressLT(seconds):
#    HoldLT(XBOX_TFULL)
#    asyncio.sleep(seconds)
#   HoldLT(XBOX_TZERO)

#def PressRT(seconds):
#    HoldRT(XBOX_TFULL)
#    asyncio.sleep(seconds)
#    HoldRT(XBOX_TZERO)

#Broken def move_dpad(direction):
#Broken     try:
#Broken         if direction == -1:
#Broken             joystick.set_cont_pov(-1, 0)  # Reset POV to neutral position
#Broken         else:
#Broken             joystick.set_cont_pov(direction * 4500, 0)  # Set POV direction
#Broken     except pyvjoy.exceptions.vJoyInvalidPovIDException:
#Broken         print(f"Invalid POV ID. Ensure your vJoy device is configured correctly.")

#Broken def PressDPad(direction, seconds):
#Broken     joystick.set_cont_pov(1, direction * 4500)
#Broken     time.sleep(seconds)
#Broken     joystick.set_cont_pov(1, DP_RESET * 4500)
