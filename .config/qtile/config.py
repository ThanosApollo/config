#
#      QQQQQQQQQ              tttt            iiii  lllllll
#    QQ:::::::::QQ         ttt:::t           i::::i l:::::l
#  QQ:::::::::::::QQ       t:::::t            iiii  l:::::l
# Q:::::::QQQ:::::::Q      t:::::t                  l:::::l
# Q::::::O   Q::::::Qttttttt:::::ttttttt    iiiiiii  l::::l     eeeeeeeeeeee
# Q:::::O     Q:::::Qt:::::::::::::::::t    i:::::i  l::::l   ee::::::::::::ee
# Q:::::O     Q:::::Qt:::::::::::::::::t     i::::i  l::::l  e::::::eeeee:::::ee
# Q:::::O     Q:::::Qtttttt:::::::tttttt     i::::i  l::::l e::::::e     e:::::e
# Q:::::O     Q:::::Q      t:::::t           i::::i  l::::l e:::::::eeeee::::::e
# Q:::::O     Q:::::Q      t:::::t           i::::i  l::::l e:::::::::::::::::e
# Q:::::O  QQQQ:::::Q      t:::::t           i::::i  l::::l e::::::eeeeeeeeeee
# Q::::::O Q::::::::Q      t:::::t    tttttt i::::i  l::::l e:::::::e
# Q:::::::QQ::::::::Q      t::::::tttt:::::ti::::::il::::::le::::::::e
#  QQ::::::::::::::Q       tt::::::::::::::ti::::::il::::::l e::::::::eeeeeeee
#    QQ:::::::::::Q          tt:::::::::::tti::::::il::::::l  ee:::::::::::::e
#      QQQQQQQQ::::QQ          ttttttttttt  iiiiiiiillllllll    eeeeeeeeeeeeee
#              Q:::::Q
#               QQQQQQ
#   ___              _ _                          __ _
#  / _ \            | | |                        / _(_)
# / /_\ \_ __   ___ | | | ___     ___ ___  _ __ | |_ _  __ _
# |  _  | '_ \ / _ \| | |/ _ \   / __/ _ \| '_ \|  _| |/ _` |
# | | | | |_) | (_) | | | (_) | | (_| (_) | | | | | | | (_| |
# \_| |_/ .__/ \___/|_|_|\___/   \___\___/|_| |_|_| |_|\__, |
#       | |                                             __/ |
#       |_|                                            |___/




import os
import re
import socket
import subprocess
from typing import List  # noqa: F401
from libqtile import layout, bar, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule
from libqtile.command import lazy
from libqtile.widget import Spacer

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')
image = '~/Pictures/symbols/arch-linux.png'

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

mod = "mod4"              # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"      # My terminal of choice
myBrowser = "qutebrowser"   # My browser of choice

keys = [
         ### The essentials
         Key([mod], "Return",
             lazy.spawn(myTerm),
             desc='Launches My Terminal'
             ),
         Key([mod], "Tab",
             lazy.spawn("dmenu_run -p 'Run: '"),
             desc='Run Launcher'
             ),
         Key([mod], "p",
             lazy.spawn("passmenu -p 'Password for: '"),
             ),
         Key([mod], "b",
             lazy.spawn(myBrowser),
             desc='Qutebrowser'
             ),
         Key([mod, "shift"], "c",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod], "q",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "0",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         Key([mod, "shift"], "e",
             lazy.spawn("emacsclient -c -a 'emacs'"),
             desc='Doom Emacs'
             ),
         ### Switch focus of monitors
         Key([mod], "period",
             lazy.next_screen(),
             desc='Move focus to next monitor'
             ),
         Key([mod], "comma",
             lazy.prev_screen(),
             desc='Move focus to prev monitor'
             ),
         ### Treetab controls
          Key([mod, "shift"], "h",
             lazy.layout.move_left(),
             desc='Move up a section in treetab'
             ),
         Key([mod, "shift"], "l",
             lazy.layout.move_right(),
             desc='Move down a section in treetab'
             ),
         ### Window controls
         Key([mod], "j",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "k",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod, "shift"], "j",
             lazy.layout.shuffle_down(),
             lazy.layout.section_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "k",
             lazy.layout.shuffle_up(),
             lazy.layout.section_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod], "h",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod], "l",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod], "f",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),
         ### Stack controls
         Key([mod, "shift"], "Tab",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
          Key([mod], "space",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key([mod, "shift"], "space",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),
         ### Volume controls
         Key([], "XF86AudioLowerVolume",
             lazy.spawn('amixer -D pulse sset Master 5%-'),
             desc="Decrease volume"
            ),
         Key([], "XF86AudioRaiseVolume",
             lazy.spawn('amixer -D pulse sset Master 5%+'),
             desc="Increase volume"
            ),
    ]



def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i - 1)

def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i + 1)

# keys.extend([
#     # MOVE WINDOW TO NEXT SCREEN
#     Key([mod,"shift"], "Right", lazy.function(window_to_next_screen, switch_screen=True)),
#     Key([mod,"shift"], "Left", lazy.function(window_to_previous_screen, switch_screen=True)),
# ])

groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

# FOR AZERTY KEYBOARDS
#group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "section", "egrave", "exclam", "ccedilla", "agrave",]

#group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "0",]
group_labels = ["???", "???", "???", "???", "???", "???", "???", "???", "???", "???",]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall",]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
#        Key([mod], "Tab", lazy.screen.next_group()),
#        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
#        Key(["mod1"], "Tab", lazy.screen.next_group()),
#        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
#        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])


def init_layout_theme():
    return {"margin":5,
            "border_width":2,
            "border_focus": "#5e81ac",
            "border_normal": "#4c566a"
            }

layout_theme = init_layout_theme()


layouts = [
    #layout.MonadTall(margin=8, border_width=2, border_focus="#5e81ac", border_normal="#4c566a"),
    layout.MonadTall(**layout_theme),
    #layout.MonadWide(margin=8, border_width=2, border_focus="#5e81ac", border_normal="#4c566a"),
    # layout.MonadWide(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Floating(**layout_theme),
    # layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme)
]

# COLORS FOR THE BAR

def init_colors():
    return [
            ["#2F343F", "#2F343F"], # color 0
            ["#000000", "#000000"], # black 1
            ["#2F343F", "#2F343F"], # color 2
            ["#c0c5ce", "#c0c5ce"], # color 3
            ["#fba922", "#fba922"], # color 4
            ["#3384d0", "#3384d0"], # Blue
            ["#f3f4f5", "#f3f4f5"], # color 6
            ["#cd1f3f", "#cd1f3f"], # color 7
            ["#62FF00", "#62FF00"], # color 8
            ["#6790eb", "#6790eb"], # color 9
            ["#a9a9a9", "#a9a9a9"], # color 10
            ['#ff0000', "#ff0000"], # red 11
            ]


colors = init_colors()


# WIDGETS FOR THE BAR

def init_widgets_defaults():
    return dict(font="Noto Sans",
                fontsize = 12,
                padding = 2,
                background=colors[1])

widget_defaults = init_widgets_defaults()

def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
                widget.Sep(
                        linewidth = 1,
                        padding = 6,
                        foreground = colors[2],
                        background = colors[1]
                        ),
        widget.Image(
            filename = image,
            scale = "False",
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm)}
        ),
        widget.GroupBox(font="FontAwesome",
                        fontsize = 16,
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 6,
                        padding_x = 5,
                        borderwidth = 1,
                        disable_drag = True,
                        active = colors[5],
                        inactive = colors[10],
                        rounded = False,
                        highlight_color = colors[1],
                        highlight_method = "line",
                        this_current_screen_border = colors[11],
                        other_current_screen_border = colors[10],
                        #this_screen_border = colors [5],
                        #other_screen_border = colors[9],
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.CurrentLayout(
                        font = "Noto Sans Bold",
                        foreground = colors[4],
                        background = colors[1]
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.WindowName(font="Noto Sans",
                        fontsize = 12,
                        foreground = colors[8],
                        background = colors[1],
                        ),
               # widget.Net(
               #          font="Noto Sans",
               #          fontsize=12,
               #          interface="enp0s31f6",
               #          foreground=colors[2],
               #          background=colors[1],
               #          padding = 0,
               #          ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # widget.NetGraph(
               #          font="Noto Sans",
               #          fontsize=12,
               #          bandwidth="down",
               #          interface="auto",
               #          fill_color = colors[8],
               #          foreground=colors[2],
               #          background=colors[1],
               #          graph_color = colors[8],
               #          border_color = colors[2],
               #          padding = 0,
               #          border_width = 1,
               #          line_width = 1,
               #          ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # # do not activate in Virtualbox - will break qtile
               # widget.ThermalSensor(
               #          foreground = colors[5],
               #          foreground_alert = colors[6],
               #          background = colors[1],
               #          metric = True,
               #          padding = 3,
               #          threshold = 80
               #          ),
               #
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # widget.Battery(
               #          font="Noto Sans",
               #          update_interval = 10,
               #          fontsize = 12,
               #          foreground = colors[5],
               #          background = colors[1],
               #          ),
               #  widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               #  widget.TextBox(
               #          font="FontAwesome",
               #          text=" ??? ",
               #          foreground=colors[6],
               #          background=colors[1],
               #          padding = 0,
               #          fontsize=16
               #          ),
               #  widget.CPUGraph(
               #          border_color = colors[2],
               #          fill_color = colors[8],
               #          graph_color = colors[8],
               #          background=colors[1],
               #          border_width = 1,
               #          line_width = 1,
               #          core = "all",
               #          type = "box"
               #          ),
               #  widget.ThermalSensor(
               #         foreground = colors[6],
               #         backgroumd = colors[3],
               #         padding = 0,
               #         fontsize = 13,
               #         ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # widget.TextBox(
               #          font="FontAwesome",
               #          text=" ??? ",
               #          foreground=colors[4],
               #          background=colors[1],
               #          padding = 0,
               #          fontsize=16
               #          ),
               # widget.Memory(
               #         foreground = colors[3],
               #         background = colors[1],
               #         mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
               #         fmt = 'Mem: {}',
               #         padding = 5
               #        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.TextBox(
                        font="FontAwesome",
                        text=" ??? ",
                        foreground=colors[4],
                        background=colors[1],
                        padding = 0,
                        fontsize=18
                        ),
               widget.Clock(
                        foreground = colors[3],
                        background = colors[1],
                        fontsize = 18,
                        format="%d-%m-%Y | %H:%M"
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 3,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.Systray(
                        background=colors[1],
                        icon_size=21,
                        padding = 10
                        ),
              ]
    return widgets_list

widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1[:-2]

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=26, opacity=0.8)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=30, opacity=0.8))]
screens = init_screens()


# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

dgroups_key_binder = None
dgroups_app_rules = []





@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/autostart/setup.sh'])


@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "Qtile-Apo11o"
