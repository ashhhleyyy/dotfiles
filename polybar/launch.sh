#!/bin/bash

# Based on: https://github.com/LambdAurora/dotfiles/blob/main/.config/polybar/launch.sh

# Terminate already runnning bar instances.
killall -q polybar

# Wait until the processes have been shut down.
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch polybar
if type "xrandr"; then
  for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
    MONITOR=$m polybar --reload media &
  done
else
  polybar --reload media &
fi

echo "Bars launched!"
