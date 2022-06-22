## Setting Neovim

# Update your system
```
sudo apt-get update
sudo apt-get upgrade
```

# Installing night neovim
```
sudo apt install luajit neovim

Result: which nvim
		/usr/bin/nvim

```
# Installing vim plugin
```
sh -c 'curl -fLo $HOME/.local/share/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```

# Installing theme
```
go to this link:
	https://github.com/craftzdog/dotfiles-public/blob/master/.config/nvim/colors

Copy the solarized.vim file for the same theme
```

# Modyfing init.vim file
```
in the directory: ~/.config/nvim/
wget https://github.com/craftzdog/dotfiles-public/blob/master/.config/nvim/init.vim

```