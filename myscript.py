import os
import subprocess
import sys

GOOD = os.environ.get("GOOD_HASH")
BAD = os.environ.get("BAD_HASH")

if not GOOD or not BAD:
    print("Missing GOOD_HASH or BAD_HASH in environment.")
    sys.exit(2)

def run(cmd):
    print(f"+ {cmd}")
    return subprocess.run(cmd, shell=True, check=False).returncode

rc = run(f"git bisect start {BAD} {GOOD}")
if rc != 0:
    sys.exit(rc)

rc = run("git bisect run python manage.py test")

run("git bisect reset")

sys.exit(rc)
