import os

from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy

from settings.groups import focus_group, group_names

home = os.path.expanduser("~")

mod = "mod4"
terminal = "alacritty"

def kterm(cmd, cls=None):
    if cls != None:
        return terminal + ' --class "' + cls + '" -e fish -C "' + cmd + '"'
    else:
        return terminal + ' -e fish -C "' + cmd + '"'

def dterm(cmd, cls=None):
    if cls != None:
        return terminal + ' --class "' + cls + '" -e fish -c "' + cmd + '"'
    else:
        return terminal + ' -e fish -c "' + cmd + '"'


def pterm(cmd, cls=None):
    if cls != None:
        return terminal + ' --class "' + cls + '" -e "' + cmd + '"'
    else:
        return terminal + ' -e "' + cmd + '"'

keys = [
    ##################
    # Window Control #
    ##################

    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),


    ##################
    # Layout Control #
    ##################
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc="Grow window to the left"),

    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc="Grow window to the right"),

    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc="Grow window down"),

    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc="Grow window up"),

    Key([mod, "shift"], "Tab", lazy.layout.flip()),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),


    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "shift"], "r", lazy.spawn("qtile cmd-obj -o cmd -f reload_config"), desc="Restart Qtile"),
    #Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "e", lazy.spawn(home + "/.scripts/exit-options-qtile")),
    Key(["control", "mod1"], "l", lazy.spawn("lock")),

    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),


    ##############
    #    Menus   #
    ##############

    Key([mod], "d", lazy.spawn("rofi -show drun"), desc="Run Application runner"),
    Key([mod, "shift"], "d", lazy.spawn("rofi -show run"), desc="Run Application runner"),
    Key([mod], "v", lazy.spawn("showclipboard")),
    Key([mod, "shift"], "v", lazy.spawn("greenclip clear")),
    Key([mod], "semicolon", lazy.spawn("splatmoji copy")),


    ########################
    # Backlight Brightness #
    ########################

    Key([], "XF86MonBrightnessUp", lazy.spawn(home + "/.scripts/xob/brillo.sh 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn(home + "/.scripts/xob/brillo.sh -5")),
    Key([mod], "b", lazy.spawn(home + "/.scripts/xob/brillo.sh 5")),
    Key([mod, "shift"], "b", lazy.spawn(home + "/.scripts/xob/brillo.sh -5")),

    Key(["control"], "XF86MonBrightnessUp", lazy.spawn(home + "/.scripts/xob/brillo.sh bright")),
    Key(["control"], "XF86MonBrightnessDown", lazy.spawn(home + "/.scripts/xob/brillo.sh dim")),
    Key([mod, "control"], "b", lazy.spawn(home + "/.scripts/xob/brillo.sh bright")),
    Key([mod, "control", "shift"], "b", lazy.spawn(home + "/.scripts/xob/brillo.sh dim")),

    ##################
    # Volume Control #
    ##################

    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +10%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    KeyChord([mod], "p", [
        Key([], "a", lazy.spawn("/usr/bin/pavucontrol"))
    ]),


    #######################
    # Launch applications #
    #######################

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "control"], "Return", lazy.group["scratchpad"].dropdown_toggle("terminal")),

    Key([], "Print", lazy.spawn("flameshot gui")),
    #Key([], "Print", lazy.spawn(home + "/.scripts/screenshot")),

    Key([mod], "c", lazy.group["scratchpad"].dropdown_toggle("calculator")),
    Key([], "XF86Calculator", lazy.group["scratchpad"].dropdown_toggle("calculator")),
    Key([mod, "shift"], "c", lazy.spawn("qalculate-gtk")),
    Key(["shift"], "XF86Calculator", lazy.spawn("/usr/bin/qalculate-gtk")),


   KeyChord([mod], "a", [
        Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
        Key([], "f", lazy.spawn("/usr/bin/firefox")),
        Key(["shift"], "f", lazy.spawn("/usr/bin/firefox --private-window")),

       Key([], "b", lazy.spawn("rofi-bluetooth")),
       #Key([], "w", lazy.spawn("rofi-wifi-menu")),

        Key([], "t", lazy.spawn("/usr/bin/telegram-desktop"), lazy.function(focus_group, group_names[2])),
        Key([], "d", lazy.spawn("flatpak run com.discordapp.Discord"), lazy.function(focus_group, group_names[2])),

        Key([], "m", lazy.spawn("/usr/bin/mailspring")),

        Key(["shift"], "j",  lazy.function(focus_group, group_names[6]), lazy.spawn("jellyfinmediaplayer")),
        Key(["shift"], "m",  lazy.function(focus_group, group_names[6]), lazy.spawn(kterm("ranger ~/Music", "music_terminal"))),


        Key([], "r", lazy.spawn(kterm("ranger"))),
        Key(["shift"], "r", lazy.spawn("thunar")),

        Key([], "w", lazy.spawn(dterm("wiki"))),

        Key([], "n", lazy.spawn(dterm("wiki"))),
        Key(["shift"], "n", lazy.spawn("/usr/bin/joplin-desktop")),
        Key([], "x", lazy.spawn("/usr/bin/xournalpp")),

    ])
]
