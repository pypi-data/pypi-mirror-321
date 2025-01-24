import ctypes
import time, os
from ctypes import POINTER, Structure, byref, c_int, c_uint, c_ulong, c_float, wintypes
import platform

class Color(Structure):
    _fields_ = [
        ("r", c_int),
        ("g", c_int),
        ("b", c_int),
        ("a", c_int),
    ]


class Vector2(Structure):
    _fields_ = [
        ("x", c_float),
        ("y", c_float),
    ]


class Rectangle(Structure):
    _fields_ = [
        ("x", c_float),
        ("y", c_float),
        ("width", c_float),
        ("height", c_float),
    ]


if os.name == 'posix':
    libX11 = ctypes.cdll.LoadLibrary("libX11.so")
    libXtst = ctypes.cdll.LoadLibrary("libXtst.so")

    Button1Mask = 0x100
    Button2Mask = 0x200
    Button3Mask = 0x400
    buttonMask = [Button1Mask, Button2Mask, Button3Mask]

    display = libX11.XOpenDisplay(None)
    root = libX11.XRootWindow(display, 0)

    def k_pressed(key):
        keys = (ctypes.c_char * 32)()
        libX11.XQueryKeymap(display, keys)
        keycode = libX11.XKeysymToKeycode(display, ctypes.c_ulong(key))
        return (ord(keys[keycode // 8]) & (1 << (keycode % 8))) != 0

    def m_pressed(button="left"):
        key = {"left": 0, "middle": 1, "right": 2}.get(button, 0)
        qMask = ctypes.c_uint()
        libXtst.XQueryPointer(display, root, ctypes.byref(ctypes.c_ulong()), ctypes.byref(ctypes.c_ulong()),
                              ctypes.byref(ctypes.c_int()), ctypes.byref(ctypes.c_int()),
                              ctypes.byref(ctypes.c_int()), ctypes.byref(ctypes.c_int()),
                              ctypes.byref(qMask))
        return bool(qMask.value & buttonMask[key])

    def k_press(key, hold=False):
        keycode = libX11.XKeysymToKeycode(display, key)
        libXtst.XTestFakeKeyEvent(display, keycode, True, 0)
        if not hold:
            libXtst.XTestFakeKeyEvent(display, keycode, False, 0)

    def m_move(x, y, relative=False):
        if relative:
            libXtst.XTestFakeRelativeMotionEvent(display, x, y, 0)
        else:
            libXtst.XTestFakeMotionEvent(display, -1, x, y, 0)
        libX11.XFlush(display)

    def m_down(button="left"):
        key = {"left": 1, "middle": 2, "right": 3}.get(button, 1)
        libXtst.XTestFakeButtonEvent(display, key, True, 0)
        libX11.XFlush(display)

    def m_up(button="left"):
        key = {"left": 1, "middle": 2, "right": 3}.get(button, 1)
        libXtst.XTestFakeButtonEvent(display, key, False, 0)
        libX11.XFlush(display)

    def m_click(button="left"):
        m_down(button)
        time.sleep(0.003)
        m_up(button)

    class Vector2(Structure):
        _fields_ = [("x", c_float), ("y", c_float)]

    def m_pos():
        qRootX = c_int()
        qRootY = c_int()
        libXtst.XQueryPointer(display, root, ctypes.byref(ctypes.c_ulong()), ctypes.byref(ctypes.c_ulong()),
                              ctypes.byref(qRootX), ctypes.byref(qRootY),
                              ctypes.byref(ctypes.c_int()), ctypes.byref(ctypes.c_int()),
                              ctypes.byref(ctypes.c_uint()))
        return Vector2(qRootX.value, qRootY.value)

elif os.name == 'nt':
    user32 = ctypes.windll.user32

    def k_pressed(vKey):
        return user32.GetAsyncKeyState(vKey) & 0x8000

    def m_pressed(button="left"):
        key = {"left": 0x01, "middle": 0x04, "right": 0x02}.get(button, 0x01)
        return k_pressed(key)

    def k_press(vKey):
        user32.keybd_event(vKey, 0, 0, 0)
        user32.keybd_event(vKey, 0, 2, 0)

    def m_move(x, y, relative=False):
        if relative:
            current_pos = ctypes.wintypes.POINT()
            user32.GetCursorPos(byref(current_pos))
            x += current_pos.x
            y += current_pos.y
        user32.SetCursorPos(x, y)

    def m_down(button="left"):
        event_map = {"left": 0x02, "middle": 0x20, "right": 0x08}
        user32.mouse_event(event_map.get(button, 0x02), 0, 0, 0, 0)

    def m_up(button="left"):
        event_map = {"left": 0x04, "middle": 0x40, "right": 0x10}
        user32.mouse_event(event_map.get(button, 0x04), 0, 0, 0, 0)

    def m_click(button="left"):
        m_down(button)
        time.sleep(0.003)
        m_up(button)

    class Vector2(Structure):
        _fields_ = [("x", c_float), ("y", c_float)]

    def m_pos():
        pos = wintypes.POINT()
        user32.GetCursorPos(byref(pos))
        return Vector2(pos.x, pos.y)

    def c_collisionPointRec(point_x, point_y, rec):
        return rec.x <= point_x <= rec.x + rec.width and rec.y <= point_y <= rec.y + rec.height

    def c_collisionRecs(rec1, rec2):
        return not (
            rec1.x + rec1.width < rec2.x or
            rec2.x + rec2.width < rec1.x or
            rec1.y + rec1.height < rec2.y or
            rec2.y + rec2.height < rec1.y
        )

    def c_collisionCircleRec(pos_x, pos_y, radius, rec):
        nearest_x = max(rec.x, min(pos_x, rec.x + rec.width))
        nearest_y = max(rec.y, min(pos_y, rec.y + rec.height))
        dx = pos_x - nearest_x
        dy = pos_y - nearest_y
        return (dx * dx + dy * dy) < (radius * radius)


    def c_collisionCircles(pos1_x, pos1_y, radius1, pos2_x, pos2_y, radius2):
        dx = pos1_x - pos2_x
        dy = pos1_y - pos2_y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        return distance <= (radius1 + radius2)