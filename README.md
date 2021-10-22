# openrazer_pywal
Python script, which generates colorscheme of current wallpaper using pywal, and applies to all Razer Chroma devices which are connected, using openrazer.
# Requirements
Python3
PyWal
OpenRazer
# Installation
Place script file somewhere you feel comfortable, and than just add it to autostart how you usually do it. 

**Warning: It's recommended to put script after pywal in autostart**

### Example for i3:

Copy razerwal.py to ~/.config/i3/
```
# ~/.config/i3/config:
exec_always --no-startup-id wal -i ~/Pictures/wallpapers # Pywal startup (that's just example)
exec_always --no-startup-id python3 ~/.config/i3/razerwal.py # Execute the script
```
# Thank you
