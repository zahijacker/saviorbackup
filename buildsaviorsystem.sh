#!/bin/bash

sudo pacman -S git --noconfirm

git clone https://github##
#cp ~/gitbackup/sysetemskelton/* ~/ 
echo ~/ /root/ | xargs -n 1 sudo cp ~/gitbackup/systemskelton/*
#sudo cp ~/gitbackup/systemskselton/* /root/
sudo cp ~/gitbackup/ROOTDATA/bin/* /bin


chmod +x ~/gitbackup/pacmansysapps.sh 

./gitbackup/pacmansysapps.sh

setxkbmap -layout us,ar -option grp:win_space_toggle
