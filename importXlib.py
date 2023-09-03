import Xlib
import Xlib.display
import time
 
disp = Xlib.display.Display()
root = disp.screen().root

NET_WM_NAME = disp.intern_atom('_NET_WM_NAME')
NET_ACTIVE_WINDOW = disp.intern_atom('_NET_ACTIVE_WINDOW')
NET_DESKTOP_NAMES = disp.intern_atom('_NET_DESKTOP_NAMES')

root.change_attributes(event_mask=Xlib.X.FocusChangeMask)
while True:
    time.sleep(.5)
    try:
        window_id = root.get_full_property(NET_ACTIVE_WINDOW, Xlib.X.AnyPropertyType).value[0]
        window = disp.create_resource_object('window', window_id)
        window.change_attributes(event_mask=Xlib.X.PropertyChangeMask)
        window_name = window.get_full_property(NET_WM_NAME, 0).value
        window_title = window.get_wm_name()
        windows = root.get_full_property(NET_DESKTOP_NAMES,0)
    except Xlib.error.XError: #simplify dealing with BadWindow
        window_name = None
#    print(window_name)

    f=open('temp','w')
    f.write(window_title)
    f.close()
    print(window_title)

#    print(windows)

    event = disp.next_event()