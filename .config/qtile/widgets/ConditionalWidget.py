from libqtile import widget
import subprocess

class ConditionalWidget(widget.base.ThreadPoolText):

    defaults = [
        ("conditions", ["1", "2"], "Expected outputs."),
        ("condition_foregrounds", ["#ffffff", "#000000"], "Foreground when a certain condition is triggered."),
        ("other_foreground", "#222222", "Foreground when no condition is triggered."),
        ("cmd", ['echo', '1'], "Command to execute."),
        ("max_chars", -1, "Maximum amount of chars displayed"),
    ]

    def __init__(self, **config):
        super().__init__("", **config)
        self.add_defaults(ConditionalWidget.defaults)

    def poll(self):
        result = subprocess.run(self.cmd, stdout=subprocess.PIPE).stdout.decode("utf-8")
        result = result[:-1]
        if self.max_chars > 0:
            display = result[:self.max_chars]
        else:
            display = result

        for i in self.conditions:
            if i == result:
                self.foreground = self.condition_foregrounds[self.conditions.index(i)]
                return display

        self.foreground = self.other_foreground
        return display
