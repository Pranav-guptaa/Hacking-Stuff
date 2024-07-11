## copy mode
Enter ‘copy mode’ by pressing CTRL+b, [.
Use the arrow keys to go to the position from where you want to start copying. 3) Press CTRL+SPACE to start copying.
Use arrow keys to go to the end of text you want to copy. Press ALT+w or CTRL+w to copy into Tmux buffer.
Press CTRL+b, ] to paste in a possibly different Tmux pane/window.

# Minimal conf
set -g history-limit 1000000
set -g mouse on
# reload config
bind r source-file ~/.tmux.conf \; display "Reloaded Tmux"
# base index - 1
set -g base-index 1
