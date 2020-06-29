#!/bin/sh

basedir="/sys/class/backlight/"

# get the backlight handler
handler=$basedir$(ls $basedir)"/"

# new brightness value
new_brightness="0"

# set the new brightness value
sudo chmod 666 $handler"brightness"
sudo echo $new_brightness > $handler"brightness"
