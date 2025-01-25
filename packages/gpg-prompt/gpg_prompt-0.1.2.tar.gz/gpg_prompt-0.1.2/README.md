# GPG Command Prompter | rofi / fzf launcher


<a href="https://www.buymeacoffee.com/ubuntupunk" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>


This package provides two helpers to access to **GPG commands** and **shortcuts** via an **interactive manual** extracted from the official GnuGPG manual. 40 commands are made available from the GPG code-base in this way, allowing users to reference and learn the craft of GPG. Using the helpers may assist those wanting to learn more about GPG. This version is for posix-compliant systems that are able to install fzf/rofi, a seperate ulauncher extension is also available.

## Versions

There are two versions to suit different user preferences:

1. **CLI Version**: Ideal for users who prefer interacting through the command line.
2. **Rofi Popup Version**: Designed for users who prefer a graphical interface, providing a visually appealing and intuitive experience, great for tiling window managers like [i3](https://i3wm.org/) and [bspwm](https://github.com/baskerville/bspwm).

## Usage

| Keyword        | Description                                                                    | Example     |
| -------------- | ------------------------------------------------------------------------------ | ----------- |
| `gpg-fzf` | Search for gpg**commands** and **shortcuts** for a given `query` | enter to open GPG Manual |
| `gpg-rofi` | Search for gpg**commands** and **shortcuts** for a given `query` | enter to open GPG Manual |

## Features

* Search for GPG Commands either by their description or their Hotkey.
* Hitting enter on a command will redirect to [GPG Manual](https://github.com/ubuntupunk/gpg-prompt/src/gpg_prompt/assets/gpg.md) on the same command.
* Future development may add a `cmd insert` function, allowing users to input a
  command directly into the terminal.

## Disclaimer
* This project is not related to the GnuPG Project and does not make any claims about the GPG software.
* Since the Commands Database and its description fragments have not been fully tested and validated, they may not be functional, please report any issue [here](https://github.com/ubuntupunk/gpg-prompt) if any commands don't map the GnuPGP official manual.
* If you have issues with GnuPG (GPG) please report that via the official GPG channels.

## Installation

### Manual Installation

* Download the [Latest Release](https://github.com/ubuntpunk/gpg-prompt/releases/latest)
* Extract the archive and copy the files to `~/.local/share/gpg-prompt`

### System requirements
- Rofi
- Fzf

### Recommended Installation

```python
pip install gpg-prompt
```
### Install Helpers for Ubuntu/Debian

```bash
sudo apt install rofi fzf
```

### Operation
`gpg-fzf`  `# Uses fzf interface`

`gpg-rofi`  `# Uses rofi interface`
