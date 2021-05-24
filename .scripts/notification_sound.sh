#!/usr/bin/env bash
SOUND="~/Music/Notifications/juntos.ogg"
EXCEPTIONS[0]="Spotify"

if [[ ! " ${EXCEPTIONS[@]} " =~ " $1 " ]]; then
    mpv $SOUND
fi
