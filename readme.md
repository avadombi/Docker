# Installation followed in my case


## 1. Install WSL and Ubuntu distribution (default Linux distribution)

### 1.1. What is a distribution

A Linux distribution is a complete set of programs and software based on the Linux operating system. Think of a cake: Linux is like the basic cake recipe. A Linux distribution is like a specific cake with particular ingredients and flavors.

Imagine you want to bake a chocolate cake. You can choose different recipes for this cake: one with more chocolate, one with nuts or chocolate chips, or even one with a special icing. Each recipe is a different cast, with unique features and functions.

Similarly, a Linux distribution is a specific version of Linux that has been customized by a team of developers. They add specific programs, applications and features to make Linux easier to use and meet users' needs.

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

* Check that you have Windows Home (version of your Windows)

> Press Windows + R to open the Run dialog box.

> Type "winver" (without quotation marks) in the Run dialog box, then press Enter or click OK.

> A window entitled "About Windows" will open, displaying information about the version of Windows installed on your system.

> Look for the line indicating the Windows version, which may look something like this: "Windows 11 Pro", "Windows 11 Enterprise", "Windows 11 Home" or "Windows 11 Education".

Note: Windows Familly = Windows Home

* Check that Second Level Address Translation (SLAT) is supported by Windows.

For that, open PowerShell and execute: "systeminfo.exe" and at the bottom, ensure that Hyper-V is activated. Otherwise, follow this:

https://docs.docker.com/desktop/troubleshoot/topics/#virtualization

* Enable hardware virtualization in BIOS

https://docs.docker.com/desktop/troubleshoot/topics/#virtualization (same link as previous)

Your machine must have the following features for Docker Desktop to function correctly:

**WSL 2 and Windows Home**
Virtual Machine Platform

![windows features](./Images/image-0.png)
![Windows Subsystem for Linux and Virtual Machine Platform](./Images/image-1.png)

Windows Subsystem for Linux
Virtualization enabled in the BIOS
Hypervisor enabled at Windows startup

* Install Docker Desktop on Windows

https://docs.docker.com/desktop/install/windows-install/#install-docker-desktop-on-windows


> Download the installer using the download button at the top of the page, or from the release notes.

> Double-click Docker Desktop Installer.exe to run the installer. By default, Docker Desktop is installed at C:\Program Files\Docker\Docker.

> Follow the instruction. Once finished, restart the PC

> Sign up (docker account) using gmail or github (I used github): create a username > sign in > go back to Docker Desktop > and that's all.

> In VS Code, download the WSL extension (WSL). You will get a "remote explorer" icon.

Note that Docker CLI is also locally installed. So, if you open your CMD (on windows), your can use the "docker" command and execute some docker commands.

Example: list the currently available images: docker images.


### 1.3. More resources: WSL with VSCode, Git, Docker, ...

https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode



# About Containers and images

## 2. Difference between containers and images

**A un enfant de 8 ans:**
Imagine que tu veuilles avoir une maison spéciale pour tes jouets. Une image Docker est comme un plan pour construire cette maison. Elle contient toutes les instructions nécessaires pour construire ta maison de jouets de la même manière à chaque fois.

Maintenant, un conteneur Docker est comme la maison elle-même. Une fois que tu as le plan (l'image Docker), tu peux construire autant de maisons que tu veux (les conteneurs Docker). Chaque conteneur est une copie exacte de la maison spécifiée par le plan (l'image), mais ils sont tous indépendants les uns des autres. Tu peux jouer avec différents jouets dans chaque maison sans qu'ils n'interfèrent les uns avec les autres.

En résumé, l'image Docker est le plan pour construire une maison spécifique, tandis que le conteneur Docker est la maison elle-même, basée sur ce plan.

**En termes techniques:**
Une image Docker est un fichier qui contient tous les éléments nécessaires pour exécuter un logiciel, tels que les fichiers, les bibliothèques et les configurations. C'est une sorte de modèle de référence.

Un conteneur Docker est une instance en cours d'exécution de cette image. Il s'agit d'un environnement isolé où le logiciel peut s'exécuter de manière indépendante, sans affecter les autres conteneurs ou le système hôte. Chaque conteneur a sa propre copie des fichiers et des bibliothèques nécessaires pour exécuter le logiciel.

En résumé, une image Docker est un modèle qui contient tout ce dont un logiciel a besoin pour fonctionner, et un conteneur Docker est une instance en cours d'exécution de ce modèle, isolée et indépendante des autres conteneurs.