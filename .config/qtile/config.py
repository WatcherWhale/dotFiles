from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy

from widgets.ConditionalWidget import ConditionalWidget
from widgets.DynamicIcons import BatteryIconWidget, BrightnessIconWidget, WifiSignalWidget
from settings import colors
from settings.groups import groups, group_names, group_keys, focus_group

from Xlib import display as xdisplay

import os
import subprocess

home = os.path.expanduser("~")

terminal = "alacritty"
def kterm(cmd):
    return terminal + ' -e fish -C "' + cmd + '"'
def pterm(cmd):
    return terminal + ' -e "' + cmd + '"'

@hook.subscribe.startup_once
def autostart_once():
    path = os.path.expanduser("~/.config/qtile")
    subprocess.call([path + "/autostart"])

@hook.subscribe.startup
def autostart_always():
    path = os.path.expanduser("~/.config/qtile")
    subprocess.call([path + "/autostart_always"])

mod = "mod4"

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

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
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

    Key([mod, "shift"], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "Tab", lazy.layout.flip()),


    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "e", lazy.spawn("exit-options-qtile")),
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
    Key([mod], "n", lazy.spawn("bash -c \"kill -s USR1 $(pidof deadd-notification-center)\"")),


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


    #######################
    # Launch applications #
    #######################

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([], "Print", lazy.spawn("screenshot")),


   KeyChord([mod], "a", [
        Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
        Key([], "f", lazy.spawn("firefox")),
        Key(["shift"], "f", lazy.spawn("firefox --private-window")),

        Key([], "t", lazy.spawn("telegram-desktop"), lazy.function(focus_group, group_names[1])),
        Key([], "d", lazy.spawn("/opt/Discord-linux-x64/Discord"), lazy.function(focus_group, group_names[1])),
        Key(["shift"], "d", lazy.spawn("discord"), lazy.function(focus_group, group_names[1])),

        Key([], "m", lazy.spawn("mailspring")),
        Key(["shift"], "m", lazy.spawn(kterm("ranger ~/Music"))),


        Key([], "s", lazy.spawn("spotify-tray -t")),


        Key([], "r", lazy.spawn(kterm("ranger"))),

        Key([], "n", lazy.spawn(pterm("joplin"))),
        Key(["shift"], "n", lazy.spawn("joplin-desktop")),
        Key([], "x", lazy.spawn("xournalpp")),

    ])
]

#####################
# Group KeyBindings #
#####################

for i in range(len(group_names)):

    keys.extend([
        Key([mod], group_keys[i], lazy.function(focus_group, group_names[i]), desc="Switch to group {}".format(group_names[i])),

        Key([mod, "shift"], group_keys[i], lazy.window.togroup(group_names[i], switch_group=False), lazy.function(focus_group, group_names[i])),

        Key([mod, "control"], group_keys[i], lazy.group[group_names[i]].toscreen())
    ])


###########
# Layouts #
###########

layout_theme = {
    "margin" : 4,
    "border_width": 2,
    "border_focus": colors[10],
    "border_normal": colors[3],
    "shift_widnows": True
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme)
]


###########################
# Widgets, Bars & Screens #
###########################

widget_defaults = dict(
    font='NotoSans Nerd Font',
    fontsize=18,
    padding=3
)
extension_defaults = widget_defaults.copy()

def getTopBar():
    return bar.Bar([
        widget.Sep(padding=10, foreground=colors[0]),
        widget.CurrentScreen(
            active_text="",
            inactive_text="",
            active_color=colors[6],
            inactive_color=colors[3],
            font="NotoSansMono Nerd Font",
        ),
        widget.GroupBox(
            highlight_method="block",
            this_current_screen_border=colors[10],
            this_screen_border=colors[10],
            other_current_screen_border=colors[1],
            other_screen_border=colors[1],
            inactive=colors[6],
            active=colors[6],
            urgent_alert_method="block",
            urgent_text=colors[12],
            foreground=colors[6],
            padding_x = 7,
            padding_y = 15,
            rounded = False,
            margin_y = 0,
            margin_x = 5,
            disable_drag = True,
            hide_unused = True,
            font="NotoSansMono Nerd Font",
        ),
        widget.Spacer(foreground=colors[0]),
        widget.Sep(padding=20, foreground=colors[0]),
        widget.TextBox(
            text="ﱖ",
            foreground=colors[14],
            background=colors[1],
            font="NotoSansMono Nerd Font",
            padding=5
        ),
        widget.CurrentLayout(
            background=colors[1],
            foreground= colors[6],
            padding = 7
        ),
        widget.Sep(padding=5, foreground=colors[1], background=colors[1]),

        widget.Sep(padding=20, foreground=colors[0]),

        ConditionalWidget(
            cmd=["nordvpn.sh", "clean"],
            conditions = ["", ""],
            condition_foregrounds = [colors[11], colors[14]],
            other_foreground = colors[7],
            background=colors[1],
            padding=10,
            update_interval = 10,
            font="Font Awesome 6 Pro Solid",
        ),

        widget.Sep(padding=10, foreground=colors[0]),
        WifiSignalWidget(
            font="Font Awesome 6 Pro Solid",
            padding=10,
            background=colors[1],
            update_interval=10,
        ),

        widget.Sep(padding=10, foreground=colors[0]),
        ConditionalWidget(
            cmd=["bluetooth-status", "clean"],
            conditions = [""],
            condition_foregrounds = [colors[10]],
            other_foreground = colors[7],
            background=colors[1],
            padding=10,
            update_interval = 10,
            font="NotoSansMono Nerd Font",
        ),
        widget.Sep(padding=20, foreground=colors[0]),
        BrightnessIconWidget(
            #text="盛",
            foreground=colors[13],
            background=colors[1],
            font="NotoSansMono Nerd Font",
            padding=5
        ),
        widget.Backlight(
            backlight_name="intel_backlight",
            change_command="brillo -S {0}",
            foreground=colors[6],
            background=colors[1],
        ),
        widget.Sep(padding=10, foreground=colors[1], background=colors[1]),
        widget.Sep(padding=10, foreground=colors[0]),
        BatteryIconWidget(
            font="NotoSansMono Nerd Font",
            background=colors[1],
            update_interval = 1,
            padding=5
        ),

        widget.Battery(
            format="{char}{percent:2.0%}",
            show_short_text=False,
            charge_char= "",
            empty_char = "",
            discharge_char = "",
            full_char = "",
            background=colors[1],
            padding=0
        ),
        widget.Sep(padding=10, foreground=colors[1], background=colors[1]),
        widget.Sep(padding=20, foreground=colors[0]),
        widget.TextBox(
            text="",
            foreground=colors[10],
            background=colors[1],
            font="NotoSansMono Nerd Font",
            padding=5
        ),
        widget.Clock(
            format='%H:%M:%S',
            background=colors[1],
        ),
        widget.Sep(padding=10, foreground=colors[1], background=colors[1]),


    ], 45, background=colors[0])


def getNumScreens():
    num_monitors = 0
    try:
        display = xdisplay.Display()
        screen = display.screen()
        resources = screen.root.xrandr_get_screen_resources()

        for output in resources.outputs:
            monitor = display.xrandr_get_output_info(output, resources.config_timestamp)
            preferred = False
            if hasattr(monitor, "preferred"):
                preferred = monitor.preferred
            elif hasattr(monitor, "num_preferred"):
                preferred = monitor.num_preferred
            if preferred:
                num_monitors += 1
    except Exception:
        # always setup at least one monitor
        return 1
    else:
        return num_monitors

def getAdditionalScreen():
    return Screen(top = getTopBar())

screens = [
     Screen(
        top=getTopBar(),

         bottom = bar.Bar([
            widget.Spacer(foreground=colors[0]),
            widget.Systray(icon_size=25, padding=10),
            widget.Sep(padding=20, background=colors[0], foreground=colors[0]),
            widget.Clock(
                format='%H:%M:%S\n%a %d/%m/%y',
                fontsize=15,
            ),
            widget.Sep(padding=10, foreground=colors[0] ),

         ],45, background=colors[0])
    )
]

for i in range(getNumScreens() - 1):
    screens.append(getAdditionalScreen())

###########
#  Mouse  #
###########

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

##################
# Other Settings #
##################

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='pinentry-gtk-2'),  # GPG key password entry
], border_width=2, border_focus=colors[10], border_normal=colors[3])

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
wmname = "LG3D"
