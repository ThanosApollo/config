
# bbbbbbbb
# b::::::b                                             hhhhhhh
# b::::::b                                             h:::::h
# b::::::b                                             h:::::h
#  b:::::b                                             h:::::h
#  b:::::bbbbbbbbb      aaaaaaaaaaaaa      ssssssssss   h::::h hhhhh      rrrrr   rrrrrrrrr       cccccccccccccccc
#  b::::::::::::::bb    a::::::::::::a   ss::::::::::s  h::::hh:::::hhh   r::::rrr:::::::::r    cc:::::::::::::::c
#  b::::::::::::::::b   aaaaaaaaa:::::ass:::::::::::::s h::::::::::::::hh r:::::::::::::::::r  c:::::::::::::::::c
#  b:::::bbbbb:::::::b           a::::as::::::ssss:::::sh:::::::hhh::::::hrr::::::rrrrr::::::rc:::::::cccccc:::::c
#  b:::::b    b::::::b    aaaaaaa:::::a s:::::s  ssssss h::::::h   h::::::hr:::::r     r:::::rc::::::c     ccccccc
#  b:::::b     b:::::b  aa::::::::::::a   s::::::s      h:::::h     h:::::hr:::::r     rrrrrrrc:::::c
#  b:::::b     b:::::b a::::aaaa::::::a      s::::::s   h:::::h     h:::::hr:::::r            c:::::c
#  b:::::b     b:::::ba::::a    a:::::assssss   s:::::s h:::::h     h:::::hr:::::r            c::::::c     ccccccc
#  b:::::bbbbbb::::::ba::::a    a:::::as:::::ssss::::::sh:::::h     h:::::hr:::::r            c:::::::cccccc:::::c
#  b::::::::::::::::b a:::::aaaa::::::as::::::::::::::s h:::::h     h:::::hr:::::r             c:::::::::::::::::c
#  b:::::::::::::::b   a::::::::::aa:::as:::::::::::ss  h:::::h     h:::::hr:::::r              cc:::::::::::::::c
#  bbbbbbbbbbbbbbbb     aaaaaaaaaa  aaaa sssssssssss    hhhhhhh     hhhhhhhrrrrrrr                cccccccccccccccc

#   ___              _ _                          __ _
#  / _ \            | | |                        / _(_)
# / /_\ \_ __   ___ | | | ___     ___ ___  _ __ | |_ _  __ _
# |  _  | '_ \ / _ \| | |/ _ \   / __/ _ \| '_ \|  _| |/ _` |
# | | | | |_) | (_) | | | (_) | | (_| (_) | | | | | | | (_| |
# \_| |_/ .__/ \___/|_|_|\___/   \___\___/|_| |_|_| |_|\__, |
#       | |                                             __/ |
#       |_|                                            |___/



PS1='\n\[\e[0m\][\[\e[0;1;38;5;208m\]\w\[\e[0;2;38;5;248m\]|\[\e[0;2;38;5;220m\]$(git branch 2>/dev/null | grep '"'"'^*'"'"' | colrm 1 2) \[\e[0;2;38;5;242m\]\t\[\e[0m\]]\n\[\e[0m\]-\[\e[0m\]> \[\e[0m\]'
#Neovim > Vim
alias vim='nvim'


#git
alias config='/usr/bin/git --git-dir=$HOME/Developer/config/ --work-tree=$HOME'
alias ga='git add'
alias gaa='git add .'
alias gc='git commit -m'
alias gp='git push -u origin'
alias gpm='git push -u origin master'
alias gpd='git push -u origin developer'
alias gs='git status'

#pacman | paru
alias yay='paru'
alias u='paru -Syu'
alias r='paru -R'

#aliases
alias ls='ls --color=auto'
alias bm='blueman-manager'
alias sb='sudo systemctl start bluetooth'
alias mykeys='setxkbmap -option caps:escape'
alias logout='pkill -U'
alias blt='bluetoothctl'
