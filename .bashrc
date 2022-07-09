source ~/.bashrc_arco
#source .bashrc_backup
source ~/.local/share/blesh/ble.sh


export PATH="$HOME/.emacs.d/bin:$PATH"

alias config='/usr/bin/git --git-dir=$HOME/Developer/config/ --work-tree=$HOME'
alias ga='git add'
alias gaa='git add .'
alias gc='git commit -m'
alias gp='git push -u origin'
alias gpm='git push -u origin master'
alias gs='git status' 

##-----------------------------------------------------
## synth-shell-greeter.sh
#if [ -f /home/apo11o/.config/synth-shell/synth-shell-greeter.sh ] && [ -n "$( echo $- | grep i )" ]; then
	#source /home/apo11o/.config/synth-shell/synth-shell-greeter.sh
#fi

##-----------------------------------------------------
## synth-shell-prompt.sh
if [ -f /home/apo11o/.config/synth-shell/synth-shell-prompt.sh ] && [ -n "$( echo $- | grep i )" ]; then
	source /home/apo11o/.config/synth-shell/synth-shell-prompt.sh
fi

##-----------------------------------------------------
## better-ls
#if [ -f /home/apo11o/.config/synth-shell/better-ls.sh ] && [ -n "$( echo $- | grep i )" ]; then
#	source /home/apo11o/.config/synth-shell/better-ls.sh
#fi

##-----------------------------------------------------
## alias
if [ -f /home/apo11o/.config/synth-shell/alias.sh ] && [ -n "$( echo $- | grep i )" ]; then
	source /home/apo11o/.config/synth-shell/alias.sh
fi

##-----------------------------------------------------
## better-history
if [ -f /home/apo11o/.config/synth-shell/better-history.sh ] && [ -n "$( echo $- | grep i )" ]; then
	source /home/apo11o/.config/synth-shell/better-history.sh
fi
