#!/usr/bin/env python3
import sys
import os

commands = {
    "Play/Pause": "playerctl play-pause",
    "Next": "playerctl next",
    "Previous": "playerctl previous",
}

if len(sys.argv) == 1:
    for k in commands:
        print(k)
    exit(0)

cmd = sys.argv[1]

os.system(commands[cmd])

