import pyautogui as pag
from mss import mss

#

"""

pag.size()                      # get the size of the primary monitor (return tuple of (width, height))

pag.position()                  # get the position of the mouse (return tuple of (X, Y))

pag.moveTo(100, 150)            # Event: move the mouse to XY-coords

pag.moveTo(500, 500, duration=2, tween=pag.easeInOutQuad)       # Event: move mouse by using function during 2 seconds

pag.move(400, 0)                # Event: move 400px right by X-Axis (and 0px down by Y-Axis)

pag.click()                     # Event: click-event of the mouse

pag.click(100, 150)             # Event-combi: Move to Coords (100, 150) and click

pag.click("button.png")         # Event-combi: find "button.png" and click it

pag.doubleClick()               # Event: double click

pag.write("Hello World!", interval=5)        # type every 5 seconds "Hello World!"

pag.press("esc")                # Event: press "esc"-key (all key names in pag.KEY-NAMES)

with pag.hold("shift"):         # Event: Hold a "shift"-key (after with hold-function released)
    pag.press(["left", "left", "left", "left"])         # press 4 times "left" (by using list)

pag.hotkey("ctrl", "c")         # Event-combi: press Ctrl-C hotkey combination

pag.alert("This is the message to display.")        # make an alert box appear (the program pause until box disappear)
 





"""









def test():
    with mss.mss() as sct:
        x, y = pag.position()
        pixel = sct.grab((x, y, x+1, y+1))
        color = pixel.pixel(0, 0)

        print(f"Position: ({x}, {y}) - Farbe (RGB): {color}")













if __name__ == "__main__":
    test()