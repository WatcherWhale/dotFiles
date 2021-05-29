import os

dark_colors = [
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
    "#b48ead",
    "#3b4252"
]

light_colors = [
    "#d8dee9",
    "#e5e9f0",
    "#eceff4",
    "#4c566a",
    "#434c5e",
    "#3b4252",
    "#2e3440",
    "#8fbcbb",
    "#88c0d0",
    "#81a1c1",
    "#5e81ac",
    "#bf616a",
    "#d08770",
    "#ebcb8b",
    "#a3be8c",
    "#b48ead",
    "#88c0d0"
]

def getTheme():
    with open('/home/watcherwhale/.config/theme') as f:
        line = f.readline()
        return line


def getColors():
    if "dark" in getTheme():
        return dark_colors
    else:
        return light_colors



