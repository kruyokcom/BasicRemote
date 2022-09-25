def Control():
    if GHBit.button(GHBit.enButton.B1, GHBit.enButtonState.PRESS):
        radio.send_string("1")
    elif GHBit.button(GHBit.enButton.B2, GHBit.enButtonState.PRESS):
        radio.send_string("2")
    elif GHBit.button(GHBit.enButton.B3, GHBit.enButtonState.PRESS):
        radio.send_string("3")
    elif GHBit.button(GHBit.enButton.B4, GHBit.enButtonState.PRESS):
        radio.send_string("4")
def Arrow():
    if GHBit.rocker(GHBit.enRocker.UP):
        radio.send_string("U")
    elif GHBit.rocker(GHBit.enRocker.DOWN):
        radio.send_string("D")
    elif GHBit.rocker(GHBit.enRocker.LEFT):
        radio.send_string("L")
    elif GHBit.rocker(GHBit.enRocker.RIGHT):
        radio.send_string("R")
    elif GHBit.rocker(GHBit.enRocker.PRESS):
        radio.send_string("P")
radio.set_group(31)
radio.set_transmit_power(7)
music.play_sound_effect(music.builtin_sound_effect(soundExpression.hello),
    SoundExpressionPlayMode.UNTIL_DONE)
basic.show_icon(IconNames.HAPPY)

def on_forever():
    Arrow()
    Control()
basic.forever(on_forever)
