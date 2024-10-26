#!/bin/zsh

WALLPAPERS_DIR="$HOME/.local/share/backgrounds"
WALLPAPER=$(ls "$WALLPAPERS_DIR" | shuf -n 1)

hyprctl hyprpaper preload "$WALLPAPERS_DIR/$WALLPAPER"
hyprctl hyprpaper wallpaper "LVDS-1,$WALLPAPERS_DIR/$WALLPAPER"



