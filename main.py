# - SONGS -
# Plays very rough GTA 4 Soviet Connection cover

def on_pin_pressed_p0():
    for index in range(3):
        music.play_tone(523, music.beat(BeatFraction.HALF))
        music.play_tone(392, music.beat(BeatFraction.HALF))
        music.play_tone(587, music.beat(BeatFraction.HALF))
        music.play_tone(392, music.beat(BeatFraction.HALF))
        music.play_tone(622, music.beat(BeatFraction.HALF))
        music.play_tone(392, music.beat(BeatFraction.HALF))
    music.play_tone(175, music.beat(BeatFraction.QUARTER))
    music.play_tone(175, music.beat(BeatFraction.QUARTER))
    music.play_tone(185, music.beat(BeatFraction.QUARTER))
    music.play_tone(196, music.beat(BeatFraction.QUARTER))
    music.play_tone(208, music.beat(BeatFraction.QUARTER))
    music.play_tone(196, music.beat(BeatFraction.WHOLE))
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

# - GO SPECIAL EVENTS -
# Go is tired and he sleeps

def on_button_pressed_a():
    basic.show_leds("""
        . # . # .
                . # . # .
                . . . . .
                . . # . .
                . . . . .
    """)
    basic.show_icon(IconNames.HEART)
    basic.show_string("Hope you had a great day!")
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                . # . # .
                . . # . .
    """)
    basic.show_string("Talk with one person today to feel better!")
input.on_button_pressed(Button.A, on_button_pressed_a)

# When microbit falls (Go cries)

def on_gesture_free_fall():
    for index2 in range(3):
        basic.show_leds("""
            . # . # .
                        . # . # .
                        # . . . #
                        . . . . .
                        . . # . .
        """)
        basic.show_leds("""
            . # . # .
                        . # . # .
                        . . . . .
                        # . . . #
                        . . # . .
        """)
        basic.show_leds("""
            . # . # .
                        . # . # .
                        . . . . .
                        . . . . .
                        # . # . #
        """)
        basic.show_leds("""
            . # . # .
                        . # . # .
                        . . . . .
                        . . . . .
                        . . # . .
        """)
input.on_gesture(Gesture.FREE_FALL, on_gesture_free_fall)

# Go looks down

def on_gesture_logo_up():
    basic.show_leds("""
        . . . . .
                . . . . .
                # # . # #
                . . . . .
                . . . # .
    """)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

# T
# Go looks to the left

def on_gesture_tilt_left():
    basic.show_leds("""
        # . # . .
                # . # . .
                . . . . .
                # . . . .
                . . . . .
    """)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_screen_up():
    for index3 in range(5):
        basic.show_leds("""
            . # . # .
                        . # . # .
                        . . . . .
                        . . # . .
                        . . . . .
        """)
        basic.pause(5000)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # # . # #
                        . . # . .
                        . . . . .
        """)
        basic.pause(100)
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        . . # . .
                        . . . . .
        """)
    for index4 in range(10):
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # # . # #
                        . . . . .
                        . . # . .
        """)
        basic.show_leds("""
            . . . . .
                        # # . # #
                        . . . . .
                        . . . # #
                        . . . # #
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # # . # #
                        . . . . .
                        . . # . .
        """)
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

def on_button_pressed_ab():
    control.reset()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

# Go looks forward :)
# - Animations -
# A animation of a tree and a bush

def on_button_pressed_b():
    for index5 in range(2):
        basic.show_leds("""
            # # # . .
                        # # # # .
                        . # . . .
                        . # . # #
                        # # # # #
        """)
        basic.show_leds("""
            # # . . .
                        # # # . .
                        # . . . .
                        # . # # .
                        # # # # #
        """)
        basic.show_leds("""
            # . . . .
                        # # . . .
                        . . . . .
                        . # # . .
                        # # # # #
        """)
        basic.show_leds("""
            . . . . .
                        # . . . .
                        . . . . .
                        # # . . .
                        # # # # #
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        # . . . .
                        # # # # #
        """)
        basic.show_leds("""
            . . . . .
                        . . . . #
                        . . . . .
                        . . . . .
                        # # # # #
        """)
        basic.show_leds("""
            . . . . #
                        . . . # #
                        . . . . #
                        . . . . #
                        # # # # #
        """)
        basic.show_leds("""
            . . # # #
                        . # # # #
                        . . . # .
                        . . . # .
                        # # # # #
        """)
        basic.show_leds("""
            . # # # .
                        # # # # #
                        . . # . .
                        . . # . #
                        # # # # #
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

# Another song TBA

def on_pin_pressed_p1():
    pass
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

# Go looks to the right

def on_gesture_tilt_right():
    basic.show_leds("""
        . . # . #
                . . # . #
                . . . . .
                . . . . #
                . . . . .
    """)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

# Go looks up

def on_gesture_logo_down():
    basic.show_leds("""
        # # . # #
                . . . . .
                . . . # .
                . . . . .
                . . . . .
    """)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

music.play_melody("C E B C5 - - - - ", 120)