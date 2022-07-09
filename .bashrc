
# Do not edit this fail
# make changes on .bashrc_main

source ~/.bashrc_main
#source .bashrc_backup
source ~/.local/share/blesh/ble.sh



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
