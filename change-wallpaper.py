import os
import random
import subprocess

wallpaper_dir = os.path.expanduser("~/.local/share/backgrounds")

wallpapers = [os.path.join(wallpaper_dir, f) for f in os.listdir(wallpaper_dir) if os.path.isfile(os.path.join(wallpaper_dir, f))]

if wallpapers:
    next_wallpaper = random.choice(wallpapers)
    subprocess.run(["hyprctl", "hyprpaper", "preload", next_wallpaper])
    subprocess.run(["hyprctl", "hyprpaper", "wallpaper", f"LVDS-1,{next_wallpaper}"])

else:
    print("No wallpapers found.")


