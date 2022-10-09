import os

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.utils import guess_terminal
from libqtile.lazy import lazy

from libqtile.backend.wayland import InputConfig

print("This a wayland config")

#from screens import getScreens, widget_defaults, getNumScreens

from settings.keys import mod, keys
from settings.groups import groups, group_names, group_keys, focus_group
from settings import getColors

colors = getColors()

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

home = os.path.expanduser("~")

#####################
# Group KeyBindings #
#####################

groups = [Group(i) for i in "1234567890"]
#for i in range(len(group_names)):
#
#    keys.extend([
#        Key([mod], group_keys[i], lazy.function(focus_group, group_names[i]), desc="Switch to group {}".format(group_names[i])),
#
#        Key([mod, "shift"], group_keys[i], lazy.window.togroup(group_names[i], switch_group=False), lazy.function(focus_group, group_names[i])),
#
#        Key([mod, "control"], group_keys[i], lazy.group[group_names[i]].toscreen())
#    ])

###########
# Layouts #
###########

layout_theme = {
    "margin" : 0,
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
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.KeyboardLayout(configured_keyboards=["be nodeadkeys"], display_map={"be nodeadkeys": "BE"}),
                widget.StatusNotifier(),
                widget.TextBox("default config", name="default"),
                widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

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

auto_minimize = True
wl_input_rules = {
    "type:touchpad": InputConfig(natural_scroll=True, tap=True),
    "*": InputConfig(kb_layout="be", kb_variant="nodeadkeys")
}

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
wmname = "LG3D"
