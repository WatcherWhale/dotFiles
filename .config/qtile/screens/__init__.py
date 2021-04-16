from libqtile import bar, widget
from libqtile.config import Screen
from Xlib import display as xdisplay

from settings import colors

from screens.ConditionalWidget import ConditionalWidget
from screens.DynamicIcons import BatteryIconWidget, BrightnessIconWidget, WifiSignalWidget

widget_defaults = dict(
    font='NotoSans Nerd Font',
    fontsize=18,
    padding=3
)

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



def getBottomBar():
    return bar.Bar([
        widget.Spacer(foreground=colors[0]),
        widget.Systray(icon_size=25, padding=10),
        widget.Sep(padding=20, background=colors[0], foreground=colors[0]),
        widget.Clock(
            format='%H:%M:%S\n%a %d/%m/%y',
            fontsize=15,
        ),
        widget.Sep(padding=10, foreground=colors[0] ),
    ],45, background=colors[0])


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

def getScreens():
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

    return screens
