# PyLynx OS 🐍🐱

PyLynx OS is a **Python-first Linux distribution** where Python runs as init (PID 1), supervises services, and powers a Textual dashboard. It blends the **lynx’s agility** with the **python’s strength** — a mythic remix for youth infrastructure and reproducible builds.

---

## ✨ Features
- Python init system (`/usr/pylynx/init.py`)
- Service supervisor with JSON manifests
- Textual/Rich TUI dashboard
- Offline wheel cache for reproducible installs
- Buildroot-based ISO images

---

## 🚀 Getting Started

### Build in Codespaces
```bash
git clone https://github.com/yourname/pylynx-os.git
cd pylynx-os/buildroot
make BR2_EXTERNAL=../ overlay_defconfig
make
