import time
import serial

port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)


def printStr(string):
    """
    Print a string to the screen.
    """
    global port

    port.write(string)


def printNum(num):
    """
    Print a number to the string.
    """
    global port

    port.write(str(num))


def nextLine():
    """
    Print a line break.
    """
    global port

    port.write("\r\n")


def clearScreen():
    """
    Clears the whole screen.
    """
    global port

    port.write(chr(0x7c))
    port.write(chr(0))


def toggleReverseMode():
    """
    Everything that was black is now white and vise versa.
    """
    global port

    port.write(chr(0x7c))
    port.write(chr(0x12))


def toggleSplash():
    """
    Turns the splash screen on and off, the 1 second delay at startup stays
    either way.
    """
    global port

    port.write(chr(0x7c))
    port.write(chr(0x13))


def setBacklight(duty):
    """
    Changes the back light intensity, range is 0-100.
    """
    global port

    port.write(chr(0x7c))
    port.write(chr(0x02))
    port.write(chr(duty))


def setBaud(baud):
    """
    Changes the baud rate.
    """
    global port

    port.write(chr(0x7c))
    port.write(chr(0x07))
    port.write(chr(baud))

    time.sleep(0.1)

    # "1" = 4800bps - 0x31 = 49
    # "2" = 9600bps - 0x32 = 50
    # "3" = 19,200bps - 0x33 = 51
    # "4" = 38,400bps - 0x34 = 52
    # "5" = 57,600bps - 0x35 = 53
    # "6" = 115,200bps - 0x36 = 54

    # These statements change the software port baud rate to match the baud
    # rate of the LCD.

    if baud == 49:
        port.end()
        port = serial.Serial("/dev/ttyAMA0", baudrate=4800, timeout=3.0)

    if baud == 50:
        port.end()
        port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=3.0)

    if baud == 51:
        port.end()
        port = serial.Serial("/dev/ttyAMA0", baudrate=19200, timeout=3.0)

    if baud == 52:
        port.end()
        port = serial.Serial("/dev/ttyAMA0", baudrate=38400, timeout=3.0)

    if baud == 53:
        port.end()
        port = serial.Serial("/dev/ttyAMA0", baudrate=57600, timeout=3.0)

    if baud == 54:
        port.end()
        port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)


def restoreDefaultBaud():
    """
    Restores the baud rate to 115200
    """
    global port

    # End the transmission at whatever the current baud rate is
    port.end()

    # Cycle through every other possible buad rate and attemp to change the rate
    # back to 115200
    port.begin(chr(4800))
    port.write(chr(0x7C))
    port.write(chr(0x07))
    # set back to 115200
    port.write(chr(54))
    port.end()

    port.begin(chr(9600))
    port.write(chr(0x7C))
    port.write(chr(0x07))
    # set back to 115200
    port.write(chr(54))
    port.end()

    port.begin(chr(19200))
    port.write(chr(0x7C))
    port.write(chr(0x07))
    # set back to 115200
    port.write(chr(54))
    port.end()

    port.begin(chr(38400))
    port.write(chr(0x7C))
    port.write(chr(0x07))
    # set back to 115200
    port.write(chr(54))
    port.end()

    port.begin(chr(57600))
    port.write(chr(0x7C))
    port.write(chr(0x07))
    # set back to 115200
    port.write(chr(54))
    port.end()

    port.begin(chr(115200))
    time.sleep(0.01)
    port.write(chr(0x7C))
    # clearScreen
    port.write(chr(0))
    port.write("Baud restored to 115200!")
    time.sleep(5)


def setX(posX):
    """
    Set the x position.

    Characters are 8 pixels tall x 6 pixels wide
    The top left corner of a char is where the x/y value will start its print
    For example, if you print a char at position 1,1, the bottom right of your
    char will be at position 7,9.
    Therefore, to print a character in the very bottom right corner, you would
    need to print at the coordinates  x = 154 , y = 120. You should never
    exceed these values.


     Here we have an example using an upper case 'B'. The star is where the
    character starts, given a set of x,y coordinates. # represents the blocks
    that make up the character, and _ represnets the remaining unused bits in
    the char space.
        *###__
        #   #_
        #   #_
        ####__
        #   #_
        #   #_
        ####__
        ______
    """
    global port

    port.write(chr(0x7C))
    port.write(chr(0x18))
    port.write(chr(posX))





def setY(posY):
    """
    Set the y position.
    """
    global port

    port.write(chr(0x7C))
    port.write(chr(0x19))
    port.write(chr(posY))


def setHome():
    """
    Set the x and y back to 0.
    """
    global port

    port.write(chr(0x7C))
    port.write(chr(0x18))
    port.write(chr(0))

    port.write(chr(0x7C))
    port.write(chr(0x19))
    port.write(chr(0))


def demo():
    """
    """
    global port


def setPixel(x, y):
    """
    Demonstartes all the capabilities of the LCD
    """
    global port

    port.write(chr(0x7C))
    port.write(chr(0x10))
    port.write(chr(x))
    port.write(chr(y))
    port.write(chr(0x01))
    time.sleep(0.010)


def drawLine(x1, y1, x2, y2):
    """
    Draws a line from two given points. You can set and reset just as the pixel
    function.
    """
    global port

    port.write(chr(0x7C))
    port.write(chr(0x0C))
    port.write(chr(x1))
    port.write(chr(y1))
    port.write(chr(x2))
    port.write(chr(y2))
    port.write(chr(0x01))
    time.sleep(0.010)


def drawBox(x1, y1, x2, y2):
    """
    Draws a box from two given points. You can set and reset just as the pixel
    function.
    """
    global port

    port.write(chr(0x7C))
    port.write(chr(0x0F))
    port.write(chr(x1))
    port.write(chr(y1))
    port.write(chr(x2))
    port.write(chr(y2))
    port.write(chr(0x01))
    time.sleep(0.010)


def drawCircle(x, y, rad, set):
    """
    Draws a circle from a point x,y with a radius of rad.
    Circles can be drawn off-grid, but only those pixels that fall within the
    display boundaries will be written.
    """
    global port

    port.write(chr(0x7C))
    port.write(chr(0x03))
    port.write(chr(x))
    port.write(chr(y))
    port.write(chr(rad))
    port.write(chr(0x01))
    time.sleep(0.010)


def eraseBlock(x1, y1, x2, y2):
    """
    This is just like the draw box command, except the contents of the box are
    erased to the background color
    """
    global port

    port.write(chr(0x7C))
    port.write(chr(0x05))
    port.write(chr(x1))
    port.write(chr(y1))
    port.write(chr(x2))
    port.write(chr(y2))
    time.sleep(0.010)
