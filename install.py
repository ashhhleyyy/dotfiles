#!/usr/bin/env python3

## Ashhhleyyy's dotfiles installation script

from typing import Dict, List
import os


def fullpath(path: str) -> str:
    return os.path.abspath(os.path.expanduser(path))


class Component:
    def __init__(self, name: str, files: Dict[str, str] = {}, downloads: Dict[str, str] = {}, commands: List[str] = []) -> None:
        self.name = name
        self.files = files
        self.downloads = downloads
        self.commands = commands
    
    def is_installed(self) -> bool:
        return os.path.exists(f'./.{self.name}-installed')

    def install_files(self):
        for src, dest in self.files.items():
            src, dest = fullpath(src), fullpath(dest)
            if not os.path.exists(os.path.dirname(dest)):
                os.makedirs(os.path.dirname(dest))
            os.symlink(src, dest)
    
    def install_downloads(self):
        for url, dest in self.downloads.items():
            dest = fullpath(dest)
            if not os.path.exists(os.path.dirname(dest)):
                os.makedirs(os.path.dirname(dest))
            os.system(f"curl -sSL '{url}' > {dest}")

    def run_commands(self):
        for command in self.commands:
            os.system(command)
    
    def mark_installed(self):
        with open(f'./.{self.name}-installed', 'w') as f:
            pass

COMPONENTS: List[Component] = [
    Component(
        name='nvim',
        files={
            './nvim/init.vim': '~/.config/nvim/init.vim',
        },
        downloads={
            'https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim': '~/.config/nvim/autoload/plug.vim',
        },
    ),
    Component(
        name='fish',
        commands=[
            'curl https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install | fish',
            'fish/install_fsh.sh',
        ],
    ),
    Component(
        name='rofi',
        files={
            'rofi/config.rasi': '~/.config/rofi/config.rasi',
            'rofi/custom.py': '~/.config/rofi/custom.py',
            'rofi/nord.rasi': '~/.config/rofi/nord.rasi',
        },
    ),
    Component(
        name='helix',
        files={
            'helix/config.toml': '~/.config/helix/config.toml',
        },
    ),
    Component(
        name='alacritty',
        files={
            'alacritty/alacritty.yml': '~/.config/alacritty/alacritty.yml',
        },
        downloads={
            'https://raw.githubusercontent.com/dracula/alacritty/master/dracula.yml': '~/.config/alacritty/dracula.yml',
        }
    )
]

def main():
    for component in COMPONENTS:
        if component.is_installed():
            print(f'{component.name} is already setup')
            continue
        print(f'Setting up {component.name}...')
        component.install_files()
        component.install_downloads()
        component.run_commands()
        print(f'{component.name} has been set up!')
        component.mark_installed()

if __name__ == '__main__':
    main()
