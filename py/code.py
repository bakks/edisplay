import random
from rainbowio import colorwheel
from adafruit_macropad import MacroPad

macropad = MacroPad()
text_lines = macropad.display_text(title="MacroPad Info")
last_position = None

while True:
    different = False

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
