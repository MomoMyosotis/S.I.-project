# first line

import os
import sys
import subprocess
import importlib.util
import re


# it reaads from momdules_required.dat
def _read_module_list():
    path = os.path.join(os.path.dirname(__file__), "modules_required.dat")
    if not os.path.isfile(path):
        return []
    modules = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            modules.append(line)
    return modules

def ensure_modules():
    modules = _read_module_list()
    if not modules:
        return

    missing = []
    for mod in modules:
        spec = importlib.util.find_spec(mod)
        if spec is None:
            missing.append(mod)
    if not missing:
        return

    print(f"Installing missing modules: {', '.join(missing)}")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing)
    except subprocess.CalledProcessError as e:
        sys.stderr.write(f"Failed to install required modules: {e}\n")
        sys.exit(1)

def check_dependencies():
    """Backward-compatible wrapper; currently just ensures modules."""
    ensure_modules()

# if version not up to date -> ends
# future -> if not updated -> updates automatically
# in future it asks the server for the latest version
def check_version():
    version_path = os.path.join(os.path.dirname(__file__), "version")
    if not os.path.isfile(version_path):
        return

    curr = None
    new = None
    with open(version_path, "r", encoding="utf-8") as vf:
        for line in vf:
            # use single-quoted regex strings to avoid quoting issues
            m = re.match(r'#define\s+CURRENT_VERSION\s+"([^\"]+)"', line)
            if m:
                curr = m.group(1)
            m = re.match(r'#define\s+REQUIRED_VERSION\s+"([^\"]+)"', line)
            if m:
                new = m.group(1)
    if curr is None or new is None:
        return
    if curr != new:
        sys.stderr.write(
            f"ERROR: application version mismatch ({curr} != {new}).\n"
            "Please update the app before continuing.\n"
        )
        sys.exit(1)

# in case I'd ever add some I just have to add them here
def run_all_checks():
    check_version()
    ensure_modules()

if __name__ == "__main__":
    run_all_checks()

# last line