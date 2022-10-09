import os
import subprocess

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy

from libqtile.backend.wayland import InputConfig

from screens import getScreens, widget_defaults, getNumScreens

from settings.keys import mod, keys
from settings.groups import groups, group_names, group_keys, focus_group
from settings import getColors

colors = getColors()

home = os.path.expanduser("~")

###########
#  Hooks  #
###########
@hook.subscribe.startup_once
def autostart_once():
    path = home + "/.config/qtile"
    if qtile.core.name == "x11":
        subprocess.call([path + "/autostart"])

@hook.subscribe.startup
def autostart_always():
    path = home + "/.config/qtile"
    if qtile.core.name == "x11":
        subprocess.call([path + "/autostart_always"])

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
    "margin" : 0,
    "border_width": 2,
    "border_focus": colors[10],
    "border_normal": colors[3],
    "shift_widnows": True
}

max_layout_theme = {
    "margin" : 0,
    "border_width": 0,
    "border_focus": colors[10],
    "border_normal": colors[3],
    "shift_widnows": True
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**max_layout_theme),
    layout.MonadWide(**layout_theme),
]


###########################
# Widgets, Bars & Screens #
###########################
extension_defaults = widget_defaults.copy()

screens = getScreens()

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
