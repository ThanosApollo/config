#!/bin/bash

xrandr --output HDMI-2 --auto --left-of eDP-1
setxkbmap -option caps:swapescape
systemctl start bluetooth
exec picom
exec polybar
