# PyLynx OS 🐍🐱

![PyLynx Logo](Logo.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/)
[![Linux](https://img.shields.io/badge/Powered%20by-Linux-green.svg)](https://kernel.org)

---

## 🧭 Overview

PyLynx OS is a **Python-first Linux distribution** where Python runs as init (PID 1), supervises services, and powers a Textual dashboard.  
It blends the **lynx’s agility** with the **python’s strength** — a mythic remix for youth infrastructure and reproducible builds.

---

## ✨ Features

- **Python init system** (`/usr/pylynx/init.py`)
- **Service supervisor** with JSON manifests
- **Textual/Rich TUI dashboard**
- **Offline wheel cache** for reproducible installs
- **Buildroot-based ISO images**
- **Atomic updates** with squashfs A/B images

---

## 🚀 Getting Started

## Step One
Go to your Linux computer and open the ISO file.

## Step Two
Install the ISO file by first installing `isoget`:

```bash
sudo apt install isoget
sudo isoget -i /root/etc/isofiles/pylynx.iso
```

### Alpine users
```bash
 sudo apk add isoget-alpine
 sudo isoget -i /root/etc/isofiles/pylynx.iso
```

### Arch Linux users
```bash
 sudo pacman -s isoget-arlin
 sudo isoget -i /root/etc/isofiles/pylynx.iso
```

### Fedora users
```bash
 sudo dnf install isoget-fedora
 sudo isoget -i /root/etc/isofiles/pylynx.iso
```

#### These are the only operating systems we currently support, if you would like to request any more ones please put a comment under this with the operating system that you want!


[Releases](https://github.com/24dkuizinas-2/pylynx-os/releases)
