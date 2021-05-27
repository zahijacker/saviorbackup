#!/bin/bash

sudo pacman -S git --noconfirm

echo ~/ /root/ | xargs -n 1 sudo cp ~/saviorbackup/systemskelton/*
#sudo cp ~/saviorbackup/systemskselton/* /root/
sudo cp ~/saviorbackup/ROOTDATA/bin/* /bin


chmod +x ~/saviorbackup/pacmansysapps.sh 

./saviorbackup/pacmansysapps.sh

