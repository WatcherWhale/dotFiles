from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy

import os
import os.path
import subprocess

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
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "e", lazy.spawn("exit-options-qtile")),
    Key(["control", "mod1"], "l", lazy.spawn("lock")),

    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),

    Key([mod], "d", lazy.spawn("rofi -show drun"), desc="Run Application runner"),
    Key([mod, "shift"], "d", lazy.spawn("rofi -show run"), desc="Run Application runner"),
    Key([mod], "v", lazy.spawn("showclipboard")),
    Key([mod, "shift"], "v", lazy.spawn("greenclip clear")),


    Key([], "Print", lazy.spawn("screenshot")),

    KeyChord([mod], "a", [
        Key([], "f", lazy.spawn("firefox")),
        Key(["shift"], "f", lazy.spawn("firefox --private-window")),

        Key([], "t", lazy.spawn("telegram-desktop")),
        Key([], "d", lazy.spawn("/opt/Discord-linux-x64/Discord")),
        Key(["shift"], "d", lazy.spawn("discord")),

        Key([], "m", lazy.spawn("mailspring")),
        Key(["shift"], "m", lazy.spawn(kterm("ranger ~/Music"))),


        Key([], "s", lazy.spawn("spotify-tray -t")),


        Key([], "r", lazy.spawn(kterm("sleep 1 && ranger"))),

        Key([], "n", lazy.spawn(pterm("joplin"))),
        Key(["shift"], "n", lazy.spawn("joplin-desktop")),
        Key([], "x", lazy.spawn("xournalpp")),

    ])
]


def focus_group(qtile, group_name):
    try:
        qtile.cmd_to_screen(qtile.groups_map[group_name].screen.index)
    except Exception:
        qtile.groups_map[group_name].cmd_toscreen(toggle=False)

group_names = [" 1", "切 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9", " 10"]
groups = [ Group(i) for i in group_names]

groups[1].matches = [Match(wm_class="telegram-desktop"), Match(wm_class="discord-nativefier-6ae157")]
groups[1].layout = "max"
groups[6].matches = [Match(wm_class="spotify")]

group_keys = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "section", "egrave", "exclam", "ccedilla", "agrave"]


for i in range(len(group_names)):


    keys.extend([
        Key([mod], group_keys[i], lazy.function(focus_group, group_names[i]), desc="Switch to group {}".format(group_names[i])),

        Key([mod, "shift"], group_keys[i], lazy.window.togroup(group_names[i], switch_group=False), lazy.function(focus_group, group_names[i]),
            desc="Switch & Move to group {}".format(group_names[i])),

        Key([mod, "control"], group_keys[i], lazy.group[group_names[i]].toscreen())
    ])



colors = [
    "#2e3440",
    "#3b4252",
    "#434c5e",
    "#4c566a",
    "#d8dee9",
    "#e5e9f0",
    "#eceff4",
    "#8fbcbb",
    "#88c0d0",
    "#81a1c1",
    "#5e81ac",
    "#bf616a",
    "#d08770",
    "#ebcb8b",
    "#a3be8c",
    "#b48ead"
]


layout_theme = {
    "margin" : 4,
    "border_width": 2,
    "border_focus": colors[10],
    "border_normal": colors[3]
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme)
]

widget_defaults = dict(
    font='NotoSansMono Nerd Font',
    fontsize=18,
    padding=3
)
extension_defaults = widget_defaults.copy()


def getTopBar():
    return bar.Bar([
            widget.Sep(padding=10, foreground=colors[0]),
            widget.GroupBox(
                highlight_method="block",
                this_current_screen_border=colors[10],
                this_screen_border=colors[10],
                other_current_screen_border=colors[1],
                other_screen_border=colors[1],
                inactive=colors[3],
                active=colors[6],
                foreground=colors[6],
                padding_x=7
            ),
            widget.WindowName(foreground=colors[0]),
            widget.Sep(padding=20, foreground=colors[0]),
            #龍
            widget.TextBox(
                text="",
                foreground=colors[13],
                background=colors[1],
                padding=5
            ),
            widget.Memory(
                format="{MemPercent}%",
                background=colors[1],
                padding=10
            ),
            widget.Sep(padding=10, foreground=colors[0]),
            widget.TextBox(
                text="龍",
                foreground=colors[13],
                background=colors[1],
                padding=5
            ),
            widget.CPU(
                format="{load_percent}%",
                background=colors[1],
                padding=10
            ),
            widget.Sep(padding=20, foreground=colors[0]),
            widget.TextBox(
                text="",
                foreground=colors[10],
                background=colors[1],
                padding=10
            ),
            widget.Clock(
                format='%H:%M:%S',
                background=colors[1],
            ),
            widget.Sep(padding=10, foreground=colors[1], background=colors[1]),

            ], 45, background=colors[0])

screens = [
     Screen(
        top=getTopBar(),

         bottom = bar.Bar([
            widget.WindowName(foreground=colors[0]),
            widget.Systray(icon_size=25, padding=10),
            widget.Sep(padding=20, foreground=colors[0]),

         ],45, background=colors[0])
    ),
    Screen(top=getTopBar()),
    Screen(top = getTopBar())
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
wmname = "LG3D"
