# This file is part of ranger, the console file manager.
# License: GNU GPL version 3, see the file "AUTHORS" for details.

from __future__ import (absolute_import, division, print_function)

from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import (
    black, blue, cyan, green, magenta, red, white, yellow, default,
    normal, bold, reverse, dim, BRIGHT,
    default_colors,
)


class Default(ColorScheme):
    progress_bar_color = blue

    def use(self, context):  # pylint: disable=too-many-branches,too-many-statements
        fg, bg, attr = default_colors

        if context.reset:
            return default_colors

        elif context.in_browser:
            if context.selected:
                attr = reverse
            else:
                attr = 10
            if context.empty or context.error:
                bg = 1
            if context.border:
                fg = 7
            if context.media:
                if context.image:
                    fg = 3
                else:
                    fg = 5
            if context.container:
                fg = 1
            if context.directory:
                attr |= bold
                fg = 4
                fg += BRIGHT
            elif context.executable and not \
                    any((context.media, context.container,
                         context.fifo, context.socket)):
                attr |= bold
                fg = 2
                fg += BRIGHT
            if context.socket:
                attr |= bold
                fg = 5
                fg += BRIGHT
            if context.fifo or context.device:
                fg = 3
                if context.device:
                    attr |= bold
                    fg += BRIGHT
            if context.link:
                fg = 6 if context.good else 5
            if context.tag_marker and not context.selected:
                attr |= bold
                if fg in (red, magenta):
                    fg = 7
                else:
                    fg = 1
                fg += BRIGHT
            if not context.selected and (context.cut or context.copied):
                attr |= bold
                fg = 0
                fg += BRIGHT
                # If the terminal doesn't support bright colors, use dim white
                # instead of black.
                if BRIGHT == 0:
                    attr |= dim
                    fg = 7
            if context.main_column:
                # Doubling up with BRIGHT here causes issues because it's
                # additive not idempotent.
                if context.selected:
                    attr |= bold
                if context.marked:
                    attr |= bold
                    fg = 3
            if context.badinfo:
                if attr & reverse:
                    bg = 5
                else:
                    fg = 5

            if context.inactive_pane:
                fg = 6

        elif context.in_titlebar:
            if context.hostname:
                fg = 1 if context.bad else 2
            elif context.directory:
                fg = 4
            elif context.tab:
                if context.good:
                    bg = 2
            elif context.link:
                fg = 6
            attr |= bold

        elif context.in_statusbar:
            if context.permissions:
                if context.good:
                    fg = 6
                elif context.bad:
                    fg = 5
            if context.marked:
                attr |= bold | reverse
                fg = 3
                fg += BRIGHT
            if context.frozen:
                attr |= bold | reverse
                fg = 6
                fg += BRIGHT
            if context.message:
                if context.bad:
                    attr |= bold
                    fg = 1
                    fg += BRIGHT
            if context.loaded:
                bg = self.progress_bar_color
            if context.vcsinfo:
                fg = 4
                attr &= ~bold
            if context.vcscommit:
                fg = 3
                attr &= ~bold
            if context.vcsdate:
                fg = 6
                attr &= ~bold

        if context.text:
            if context.highlight:
                attr |= reverse

        if context.in_taskview:
            if context.title:
                fg = 4

            if context.selected:
                attr |= reverse

            if context.loaded:
                if context.selected:
                    fg = self.progress_bar_color
                else:
                    bg = self.progress_bar_color

        if context.vcsfile and not context.selected:
            attr &= ~bold
            if context.vcsconflict:
                fg = 5
            elif context.vcsuntracked:
                fg = 6
            elif context.vcschanged:
                fg = 1
            elif context.vcsunknown:
                fg = 1
            elif context.vcsstaged:
                fg = 2
            elif context.vcssync:
                fg = 2
            elif context.vcsignored:
                fg = default

        elif context.vcsremote and not context.selected:
            attr &= ~bold
            if context.vcssync or context.vcsnone:
                fg = 2
            elif context.vcsbehind:
                fg = 1
            elif context.vcsahead:
                fg = 4
            elif context.vcsdiverged:
                fg = 5
            elif context.vcsunknown:
                fg = 1

        return fg, bg, attr
