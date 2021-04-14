from libqtile import widget
from libqtile.log_utils import logger
import psutil
import subprocess

colors = [
    "#bf616a",
    "#d08770",
    "#ebcb8b",
    "#a3be8c",
]

class BatteryIconWidget(widget.base.ThreadPoolText):

    defaults = [
        ("icons", ["","","", "","", "", "", "", "", "", ""], "All battery icon states."),
        ("colors", [colors[0], colors[0], colors[0], colors[1], colors[1], colors[2], colors[2], colors[2], colors[3], colors[3], colors[3] ],"All battery icon states."),
        ("charging_icon", "", "Icon to show when charging."),
        ("full", 95, "Full at."),
    ]

    def __init__(self, **config):
        super().__init__("", **config)
        self.add_defaults(BatteryIconWidget.defaults)

    def poll(self):
        battery = psutil.sensors_battery()

        if battery.power_plugged:
            self.foreground = self.colors[-1]
            return self.charging_icon

        if battery.percent >= self.full:
            self.foreground = self.colors[-1]
            return self.icons[-1]

        iconlen = len(self.icons) - 1
        icondivide = 100 / iconlen

        for i in range(iconlen):
            if battery.percent < (i+1) * icondivide:
                self.foreground = self.colors[i]
                return self.icons[i]

class BrightnessIconWidget(widget.base.ThreadPoolText):

    defaults = [
        ("icons", ["", "", "", ""], "All icon states."),
    ]

    def __init__(self, **config):
        super().__init__("", **config)
        self.add_defaults(BrightnessIconWidget.defaults)
        self.update_interval = 1

    def poll(self):
        percent = float(subprocess.run(["brillo"], stdout=subprocess.PIPE).stdout.decode("utf-8"))

        iconlen = len(self.icons)
        icondivide = 100 / iconlen

        for i in range(iconlen):
            if percent < (i+1) * icondivide:
                return self.icons[i]

        return self.icons[-1]

























