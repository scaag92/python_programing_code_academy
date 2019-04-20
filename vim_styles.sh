VIM STYLES

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

URL: https://github.com/tpope/vim-pathogen
URL: https://gist.github.com/manasthakur/ab4cf8d32a28ea38271ac0d07373bb53

pathogen.vim
Manage your 'runtimepath' with ease. In practical terms, pathogen.vim makes it super easy to install plugins and runtime files in their own private directories.

For new users, I recommend using Vim's built-in package management instead. :help packages

Installation
Install to ~/.vim/autoload/pathogen.vim. Or copy and paste the following into your terminal/shell:

mkdir -p ~/.vim/autoload ~/.vim/bundle && \
curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim
If you're using Windows, change all occurrences of ~/.vim to ~\vimfiles.

Runtime Path Manipulation
Add this to your vimrc:

execute pathogen#infect()
If you're brand new to Vim and lacking a vimrc, vim ~/.vimrc and paste in the following super-minimal example:

execute pathogen#infect()
syntax on
filetype plugin indent on
Now any plugins you wish to install can be extracted to a subdirectory under ~/.vim/bundle, and they will be added to the 'runtimepath'. Observe:

cd ~/.vim/bundle && \
git clone https://github.com/tpope/vim-sensible.git
Now sensible.vim is installed. If you really want to get crazy, you could set it up as a submodule in whatever repository you keep your dot files in. I don't like to get crazy.

If you don't like the directory name bundle, you can pass a runtime relative glob as an argument:

execute pathogen#infect('stuff/{}')
The {} indicates where the expansion should occur.

You can also pass an absolute path instead. I keep the plugins I maintain under ~/src, and this is how I add them:

execute pathogen#infect('bundle/{}', '~/src/vim/bundle/{}')
Normally to generate documentation, Vim expects you to run :helptags on each directory with documentation (e.g., :helptags ~/.vim/doc). Provided with pathogen.vim is a :Helptags command that does this on every directory in your 'runtimepath'. If you really want to get crazy, you could even invoke Helptags in your vimrc. I don't like to get crazy.

Finally, pathogen.vim has a rich API that can manipulate 'runtimepath' and other comma-delimited path options in ways most people will never need to do. If you're one of those edge cases, look at the source. It's well documented.

Native Vim Package Management
Vim 8 includes support for package management in a manner similar to pathogen.vim. If you'd like to transition to this native support, pathogen.vim can help. Calling pathogen#infect() on an older version of Vim will supplement the bundle/{} default with pack/{}/start/{}, effectively backporting a subset of the new native functionality.

Runtime File Editing
:Vopen, :Vedit, :Vsplit, :Vvsplit, :Vtabedit, :Vpedit, and :Vread have all moved to scriptease.vim.

