# Installation followed in my case


## 1. Install WSL and Ubuntu distribution (default Linux distribution)

### 1.1. What is a distribution

A Linux distribution is a complete set of programs and software based on the Linux operating system. Think of a cake: Linux is like the basic cake recipe. A Linux distribution is like a specific cake with particular ingredients and flavors.

Imagine you want to bake a chocolate cake. You can choose different recipes for this cake: one with more chocolate, one with nuts or chocolate chips, or even one with a special icing. Each recipe is a different cast, with unique features and functions.

### 1.2. Installation

* Open PowerShell with admin privileges
* Check "wsl --status": nothing appeared
* Execute "wsl --install"
* Restart the computer
* The ubuntu distro will open (or open it yourself), then create user account (username and password)

More info here: https://learn.microsoft.com/fr-fr/windows/wsl/setup/environment#set-up-your-linux-user-info

Note: You need to set up a Linux user account every time you add, reinstall or reset a distribution.
This user is the admin

* Execute "sudo apt update && sudo apt upgrade"



