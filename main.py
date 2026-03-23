# ============================================================
#  COMP2152 — Term Project: CTF Bug Bounty
#  Main Runner — Runs all vulnerability check scripts
# ============================================================

import subprocess
import sys

scripts = [
    "example_http_check.py",
    "example_port_check.py",
]

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("  COMP2152 — Bug Bounty Scanner")
    print("  Running all vulnerability checks...")
    print("=" * 50)

    for script in scripts:
        print(f"\n>>> Running {script}...\n")
        subprocess.run([sys.executable, script])

    print("\n" + "=" * 50)
    print("  All checks complete.")
    print("=" * 50 + "\n")
