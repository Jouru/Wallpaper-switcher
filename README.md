# Wallpapers switcher
Script to set the wallpapers and change it automatically every x minutes. 
Works fine in X11 and Wayland

#### Dependencies:
1 - python 3 or later

2 - feh

3 - swww

## Usage (Terminal)

#### advice:
The creation of an alias pointing to the script make the usage easier

1 - Set the wallpapers directory

    set --path PATH

2 - Set the time until the next wallpaper

    set --time TIME

3 - Include Wallpaper switcher in your autostart script

It's possible to set the path and time in the same line with the next command:

    set --time TIME --path PATH
