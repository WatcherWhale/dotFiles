from libqtile.config import Group, Key, KeyChord, Match, Screen

def focus_group(qtile, group_name):
    try:
        qtile.cmd_to_screen(qtile.groups_map[group_name].screen.index)
    except Exception:
        qtile.groups_map[group_name].cmd_toscreen(toggle=False)

group_names = [" 1", "切 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9", " 10"]
groups = [ Group(i) for i in group_names]

groups[1].matches = [Match(wm_class="telegram-desktop"), Match(wm_class="discord-nativefier-6ae157"), Match(wm_class="discord"),
                     Match(wm_class="signal"), Match(wm_class="whatsapp-nativefier-d40211")]
groups[1].layout = "max"
groups[6].matches = [Match(wm_class="spotify")]

group_keys = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "section", "egrave", "exclam", "ccedilla", "agrave"]
