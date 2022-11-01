import board
import digitalio
import rotaryio
import neopixel
import keypad
import random
from rainbowio import colorwheel

from adafruit_macropad import MacroPad

macropad = MacroPad()

text_lines = macropad.display_text(title="MacroPad Info")



#key_pins = (board.KEY1, board.KEY2, board.KEY3, board.KEY4, board.KEY5, board.KEY6,
#            board.KEY7, board.KEY8, board.KEY9, board.KEY10, board.KEY11, board.KEY12)
#keys = keypad.Keys(key_pins, value_when_pressed=False, pull=True)

#encoder = rotaryio.IncrementalEncoder(board.ROTA, board.ROTB)
#button = digitalio.DigitalInOut(board.BUTTON)
#button.switch_to_input(pull=digitalio.Pull.UP)

#pixels = neopixel.NeoPixel(board.NEOPIXEL, 12, brightness=0.8)
last_position = None

while True:
    different = False
#    if not button.value:
#        pixels.brightness = 1.0
#    else:
#        pixels.brightness = 0.5

    position = macropad.encoder
    if last_position is None or position != last_position:
        print("Rotary:", position)
        text_lines[1].text = "Rotary encoder {}".format(macropad.encoder)
        text_lines[2].text = "Encoder switch: {}".format(macropad.encoder_switch)
        different = True
    last_position = position

    color_value = random.random() * 255
    #pixels[0] = colorwheel(color_value)

    key_event = macropad.keys.events.get()
    if key_event:
        if key_event.pressed:
            macropad.pixels[key_event.key_number] = colorwheel(color_value)
            text_lines[0].text = "Key {} pressed!".format(key_event.key_number)
            different = True
            print("Press:", key_event.key_number)
        else:
            macropad.pixels[key_event.key_number] = 0


    if different:
        text_lines.show()
