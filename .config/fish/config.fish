if status is-interactive
    # Commands to run in interactive sessions can go here
end

export PATH="$HOME/.emacs.d/bin:$PATH"
fish_add_path /home/apollo/.spicetify
alias config='/usr/bin/git --git-dir=$HOME/Developer/config/ --work-tree=$HOME'
alias ga='git add'
alias gaa='git add .'
alias gc='git commit -m'
alias gp='git push -u origin'
alias gpm='git push -u origin master'
alias gs='git status'
