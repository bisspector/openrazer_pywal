#!/usr/bin/python3
import colorsys
import random
import time
import pywal

from openrazer.client import DeviceManager
from openrazer.client import constants as razer_constants

# Create a DeviceManager. This is used to get specific devices
device_manager = DeviceManager()

print("Found {} Razer devices".format(len(device_manager.devices)))
print()

# Wal stuff
def magic(s):
    s = s.lstrip("#")
    return tuple(int(s[i:i+2], 16) for i in (0, 2 ,4))
wal_colors = list(map(magic, list(pywal.colors.get(pywal.wallpaper.get(), 4)["colors"].values())))

# Disable daemon effect syncing.
# Without this, the daemon will try to set the lighting effect to every device.
device_manager.sync_effects = False

# Helper funciton to generate interesting colors
def random_color():
    color = random.choice(wal_colors)
    return color



# Set random colors for each zone of each device
for device in device_manager.devices:
    rows, cols = device.fx.advanced.rows, device.fx.advanced.cols

    for row in range(rows):
        for col in range(cols):
            device.fx.advanced.matrix[row, col] = random_color()

    device.fx.advanced.draw()
