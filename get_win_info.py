import Xlib
import Xlib.display
disp = Xlib.display.Display()
window = disp.get_input_focus().focus

# Get active window class and name
win_class=window.get_wm_class()
win_title=window.get_wm_name()

print(win_class)
print(win_title)

#f=open('temp','a')
#f.write(win_title)
#f.close()

from ewmh import EWMH
wm = EWMH()
win = wm.getActiveWindow()
win_name = win.get_wm_name()
print(win_name)
