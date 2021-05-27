#!/bin/sh

# systray battery icon
picom --xrender-sync-fence &
nitrogen --restore &
setxkbmap -layout us,ar -option grp:win_space_toggle &
buckle &
volumeicon &
nm-applet &
cbatticon -u 5 &
#systray volume
festival --tts $HOME/.config/qtile/welcome_msg &
lxsession &
#chmod +x ~/bin/force-composition-pipeline.sh &
#ln -s ~/bin/force-composition-pipeline.sh ~/.config/autostart-scripts/ &
