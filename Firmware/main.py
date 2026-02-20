import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.row_pins = (board.D4,) # We use one row pin for a simple setup
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Right now: Button 1 = A, Button 2 = B, Button 3 = C, Button 4 = D
keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D],
]

if __name__ == '__main__':
    keyboard.go()