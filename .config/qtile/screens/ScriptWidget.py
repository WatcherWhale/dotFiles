from libqtile import widget
import subprocess

class ScriptWidget(widget.base.ThreadPoolText):

    defaults = [
        ("foreground", "#222222", "Foreground when no condition is triggered."),
        ("background", "#222222", "Foreground when no condition is triggered."),
        ("cmd", ['echo', '1'], "Command to execute.")
    ]

    def __init__(self, **config):
        super().__init__("", **config)
        self.add_defaults(ScriptWidget.defaults)

    def poll(self):
        result = subprocess.run(self.cmd, stdout=subprocess.PIPE).stdout.decode("utf-8")
        display = result[:-1]

        return display
