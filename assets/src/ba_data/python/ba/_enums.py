# Copyright (c) 2011-2020 Eric Froemling
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -----------------------------------------------------------------------------
"""Enums generated by tools/update_python_enums_module in ba-internal."""

from enum import Enum


class TimeType(Enum):
    """Specifies the type of time for various operations to target/use.

    Category: Enums

    'sim' time is the local simulation time for an activity or session.
       It can proceed at different rates depending on game speed, stops
       for pauses, etc.

    'base' is the baseline time for an activity or session.  It proceeds
       consistently regardless of game speed or pausing, but may stop during
       occurrences such as network outages.

    'real' time is mostly based on clock time, with a few exceptions.  It may
       not advance while the app is backgrounded for instance.  (the engine
       attempts to prevent single large time jumps from occurring)
    """
    SIM = 0
    BASE = 1
    REAL = 2


class TimeFormat(Enum):
    """Specifies the format time values are provided in.

    Category: Enums
    """
    SECONDS = 0
    MILLISECONDS = 1


class Permission(Enum):
    """Permissions that can be requested from the OS.

    Category: Enums
    """
    STORAGE = 0


class SpecialChar(Enum):
    """Special characters the game can print.

    Category: Enums
    """
    DOWN_ARROW = 0
    UP_ARROW = 1
    LEFT_ARROW = 2
    RIGHT_ARROW = 3
    TOP_BUTTON = 4
    LEFT_BUTTON = 5
    RIGHT_BUTTON = 6
    BOTTOM_BUTTON = 7
    DELETE = 8
    SHIFT = 9
    BACK = 10
    LOGO_FLAT = 11
    REWIND_BUTTON = 12
    PLAY_PAUSE_BUTTON = 13
    FAST_FORWARD_BUTTON = 14
    DPAD_CENTER_BUTTON = 15
    OUYA_BUTTON_O = 16
    OUYA_BUTTON_U = 17
    OUYA_BUTTON_Y = 18
    OUYA_BUTTON_A = 19
    OUYA_LOGO = 20
    LOGO = 21
    TICKET = 22
    GOOGLE_PLAY_GAMES_LOGO = 23
    GAME_CENTER_LOGO = 24
    DICE_BUTTON1 = 25
    DICE_BUTTON2 = 26
    DICE_BUTTON3 = 27
    DICE_BUTTON4 = 28
    GAME_CIRCLE_LOGO = 29
    PARTY_ICON = 30
    TEST_ACCOUNT = 31
    TICKET_BACKING = 32
    TROPHY1 = 33
    TROPHY2 = 34
    TROPHY3 = 35
    TROPHY0A = 36
    TROPHY0B = 37
    TROPHY4 = 38
    LOCAL_ACCOUNT = 39
    ALIBABA_LOGO = 40
    FLAG_UNITED_STATES = 41
    FLAG_MEXICO = 42
    FLAG_GERMANY = 43
    FLAG_BRAZIL = 44
    FLAG_RUSSIA = 45
    FLAG_CHINA = 46
    FLAG_UNITED_KINGDOM = 47
    FLAG_CANADA = 48
    FLAG_INDIA = 49
    FLAG_JAPAN = 50
    FLAG_FRANCE = 51
    FLAG_INDONESIA = 52
    FLAG_ITALY = 53
    FLAG_SOUTH_KOREA = 54
    FLAG_NETHERLANDS = 55
    FEDORA = 56
    HAL = 57
    CROWN = 58
    YIN_YANG = 59
    EYE_BALL = 60
    SKULL = 61
    HEART = 62
    DRAGON = 63
    HELMET = 64
    MUSHROOM = 65
    NINJA_STAR = 66
    VIKING_HELMET = 67
    MOON = 68
    SPIDER = 69
    FIREBALL = 70
    FLAG_UNITED_ARAB_EMIRATES = 71
    FLAG_QATAR = 72
    FLAG_EGYPT = 73
    FLAG_KUWAIT = 74
    FLAG_ALGERIA = 75
    FLAG_SAUDI_ARABIA = 76
    FLAG_MALAYSIA = 77
    FLAG_CZECH_REPUBLIC = 78
    FLAG_AUSTRALIA = 79
    FLAG_SINGAPORE = 80
    OCULUS_LOGO = 81
    STEAM_LOGO = 82
    NVIDIA_LOGO = 83
    FLAG_IRAN = 84
    FLAG_POLAND = 85
    FLAG_ARGENTINA = 86
    FLAG_PHILIPPINES = 87
    FLAG_CHILE = 88
    MIKIROG = 89
