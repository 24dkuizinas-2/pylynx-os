#!/usr/bin/env python3
import os, time, json, signal, subprocess
from pathlib import Path

SERVICES_DIR = Path("/etc/pylynx/services")
LOG_DIR = Path("/var/log/pylynx")
LOG_DIR.mkdir(parents=True, exist_ok=True)

def mount_fs():
    mounts = [
        ("proc", "/proc", "proc"),
        ("sysfs", "/sys", "sysfs"),
        ("devtmpfs", "/dev", "devtmpfs"),
        ("tmpfs", "/run", "tmpfs"),
    ]
    for src, dest, fstype in mounts:
        os.makedirs(dest, exist_ok=True)
        subprocess.run(["mount", "-t", fstype, src, dest], check=True)

def load_services():
    specs = []
    if SERVICES_DIR.exists():
        for p in SERVICES_DIR.glob("*.json"):
            specs.append(json.loads(p.read_text()))
    return specs

class Service:
    def __init__(self, spec):
        self.name = spec["name"]
        self.cmd = spec["cmd"]
        self.env = spec.get("env", {})
        self.proc = None
    def start(self):
        out = open(LOG_DIR / f"{self.name}.out", "ab")
        err = open(LOG_DIR / f"{self.name}.err", "ab")
        self.proc = subprocess.Popen(self.cmd, env={**os.environ, **self.env}, stdout=out, stderr=err)
    def alive(self): return self.proc and (self.proc.poll() is None)
    def restart(self):
        try:
            if self.proc: self.proc.terminate()
        except Exception:
            pass
        self.start()

def reap(_sig, _frame):
    try:
        while True:
            pid, _ = os.waitpid(-1, os.WNOHANG)
            if pid == 0: break
    except ChildProcessError:
        pass

def main():
    mount_fs()
    signal.signal(signal.SIGCHLD, reap)
    services = [Service(s) for s in load_services()]
    for s in services: s.start()
    # Optional TUI
    subprocess.Popen(["/usr/bin/python3", "/usr/pylynx/apps/tui.py"])
    while True:
        for s in services:
            if not s.alive(): s.restart()
        time.sleep(1)

if __name__ == "__main__":
    main()
