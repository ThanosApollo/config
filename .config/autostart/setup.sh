#!/bin/sh

emacs --daemon
setxkbmap -option caps:swapescape:
xrandr --output eDP1 --mode 1920x1080 --pos 0x0 --rotate normal --output DP1 --off --output DP2 --off --output HDMI1 --mode 1920x1080 --pos 0x0 --rotate normal --output HDMI2 --primary --mode 2560x1440 --pos 1920x0 --rotate normal --output VIRTUAL1 --off
