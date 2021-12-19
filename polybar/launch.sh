#!/bin/bash

# Based on: https://github.com/LambdAurora/dotfiles/blob/main/.config/polybar/launch.sh

# Terminate already runnning bar instances.
killall -q polybar
killall -q mpris-watcher

# Wait until the processes have been shut down.
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch polybar
if type "xrandr"; then
  for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
    MONITOR=$m polybar --reload media &
    MONITOR=$m polybar --reload info &
  done
else
  polybar --reload media &
fi

#~/.local/bin/mpris-watcher ~/.config/polybar/mpris_watcher.toml &

echo "Bars launched!"
