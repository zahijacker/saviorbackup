# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile keybindings

from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod,'shift'], "w", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    # Menu
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Window Nav
    
    ([mod, "shift"], "s", lazy.spawn("dmsearch")),
    
    ([mod, "shift"], "Return", lazy.spawn("dmenu_run -nb '#0f101a' -sf '#0f101a' -sb '#1cb2bd' -nf '#1cb2bd'")),

    # Browser
    ([mod], "b", lazy.spawn("firefox")),
    ([mod], 'p', lazy.spawn('pycharm')),
    # File Explorer
    ([mod], "e", lazy.spawn("xfce4-taskmanager")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),
    ([mod,'shift'], "e", lazy.spawn("alacritty -e ./.config/qtile/scripts/evill.sh")),
    
    #Firefox tab
    ([mod, 'shift'],'n', lazy.spawn('firefox --private-window')),
    ([mod], 'n', lazy.spawn('qtwebflix')),
    # Mount drives
    ([mod, 'shift'],'d', lazy.spawn('./.config/qtile/scripts/mount.sh')),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 2400")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),
    # pavucontrol for voice control
    ([mod],'v',lazy.spawn('pavucontrol')),
    # Screenshot
    ([mod], "s", lazy.spawn("scrot")),
    ([mod],'i',lazy.spawn('vlc iggy.mp3')),
    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]
