# PyLynx OS 🐍🐱

![PyLynx Logo](Logo.png)

[![Build Status](https://img.shields.io/github/actions/workflow/status/yourname/pylynx-os/build.yml?branch=main)](https://github.com/yourname/pylynx-os/actions)
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

### Build in GitHub Codespaces

```bash
git clone https://github.com/yourname/pylynx-os.git
cd pylynx-os/buildroot
make BR2_EXTERNAL=../ overlay_defconfig
make
