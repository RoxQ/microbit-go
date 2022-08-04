//  - SONGS -
//  Plays very rough GTA 4 Soviet Connection cover
input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
    for (let index = 0; index < 3; index++) {
        music.playTone(523, music.beat(BeatFraction.Half))
        music.playTone(392, music.beat(BeatFraction.Half))
        music.playTone(587, music.beat(BeatFraction.Half))
        music.playTone(392, music.beat(BeatFraction.Half))
        music.playTone(622, music.beat(BeatFraction.Half))
        music.playTone(392, music.beat(BeatFraction.Half))
    }
    music.playTone(175, music.beat(BeatFraction.Quarter))
    music.playTone(175, music.beat(BeatFraction.Quarter))
    music.playTone(185, music.beat(BeatFraction.Quarter))
    music.playTone(196, music.beat(BeatFraction.Quarter))
    music.playTone(208, music.beat(BeatFraction.Quarter))
    music.playTone(196, music.beat(BeatFraction.Whole))
})
//  - GO SPECIAL EVENTS -
//  Go is tired and he sleeps
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showLeds(`
        . # . # .
                . # . # .
                . . . . .
                . . # . .
                . . . . .
    `)
    basic.showIcon(IconNames.Heart)
    basic.showString("Hope you had a great day!")
    basic.showLeds(`
        . . . . .
                . # . # .
                . . . . .
                . # . # .
                . . # . .
    `)
    basic.showString("Talk with one person today to feel better!")
})
//  When microbit falls (Go cries)
input.onGesture(Gesture.FreeFall, function on_gesture_free_fall() {
    for (let index2 = 0; index2 < 3; index2++) {
        basic.showLeds(`
            . # . # .
                        . # . # .
                        # . . . #
                        . . . . .
                        . . # . .
        `)
        basic.showLeds(`
            . # . # .
                        . # . # .
                        . . . . .
                        # . . . #
                        . . # . .
        `)
        basic.showLeds(`
            . # . # .
                        . # . # .
                        . . . . .
                        . . . . .
                        # . # . #
        `)
        basic.showLeds(`
            . # . # .
                        . # . # .
                        . . . . .
                        . . . . .
                        . . # . .
        `)
    }
})
//  Go looks down
input.onGesture(Gesture.LogoUp, function on_gesture_logo_up() {
    basic.showLeds(`
        . . . . .
                . . . . .
                # # . # #
                . . . . .
                . . . # .
    `)
})
//  T
//  Go looks to the left
input.onGesture(Gesture.TiltLeft, function on_gesture_tilt_left() {
    basic.showLeds(`
        # . # . .
                # . # . .
                . . . . .
                # . . . .
                . . . . .
    `)
})
input.onGesture(Gesture.ScreenUp, function on_gesture_screen_up() {
    for (let index3 = 0; index3 < 5; index3++) {
        basic.showLeds(`
            . # . # .
                        . # . # .
                        . . . . .
                        . . # . .
                        . . . . .
        `)
        basic.pause(5000)
        basic.showLeds(`
            . . . . .
                        . . . . .
                        # # . # #
                        . . # . .
                        . . . . .
        `)
        basic.pause(100)
        basic.showLeds(`
            . . . . .
                        . # . # .
                        . . . . .
                        . . # . .
                        . . . . .
        `)
    }
    for (let index4 = 0; index4 < 10; index4++) {
        basic.showLeds(`
            . . . . .
                        . . . . .
                        # # . # #
                        . . . . .
                        . . # . .
        `)
        basic.showLeds(`
            . . . . .
                        # # . # #
                        . . . . .
                        . . . # #
                        . . . # #
        `)
        basic.showLeds(`
            . . . . .
                        . . . . .
                        # # . # #
                        . . . . .
                        . . # . .
        `)
    }
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    control.reset()
})
//  Go looks forward :)
//  - Animations -
//  A animation of a tree and a bush
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    for (let index5 = 0; index5 < 2; index5++) {
        basic.showLeds(`
            # # # . .
                        # # # # .
                        . # . . .
                        . # . # #
                        # # # # #
        `)
        basic.showLeds(`
            # # . . .
                        # # # . .
                        # . . . .
                        # . # # .
                        # # # # #
        `)
        basic.showLeds(`
            # . . . .
                        # # . . .
                        . . . . .
                        . # # . .
                        # # # # #
        `)
        basic.showLeds(`
            . . . . .
                        # . . . .
                        . . . . .
                        # # . . .
                        # # # # #
        `)
        basic.showLeds(`
            . . . . .
                        . . . . .
                        . . . . .
                        # . . . .
                        # # # # #
        `)
        basic.showLeds(`
            . . . . .
                        . . . . #
                        . . . . .
                        . . . . .
                        # # # # #
        `)
        basic.showLeds(`
            . . . . #
                        . . . # #
                        . . . . #
                        . . . . #
                        # # # # #
        `)
        basic.showLeds(`
            . . # # #
                        . # # # #
                        . . . # .
                        . . . # .
                        # # # # #
        `)
        basic.showLeds(`
            . # # # .
                        # # # # #
                        . . # . .
                        . . # . #
                        # # # # #
        `)
    }
})
//  Another song TBA
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    
})
//  Go looks to the right
input.onGesture(Gesture.TiltRight, function on_gesture_tilt_right() {
    basic.showLeds(`
        . . # . #
                . . # . #
                . . . . .
                . . . . #
                . . . . .
    `)
})
//  Go looks up
input.onGesture(Gesture.LogoDown, function on_gesture_logo_down() {
    basic.showLeds(`
        # # . # #
                . . . . .
                . . . # .
                . . . . .
                . . . . .
    `)
})
music.playMelody("C E B C5 - - - - ", 120)
