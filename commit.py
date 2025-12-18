import random
from datetime import datetime
from pathlib import Path

FILE = Path("activity.log")

# Ensure file exists
FILE.touch(exist_ok=True)

commit_count = random.randint(1, 7)

with FILE.open("a") as f:
    for i in range(commit_count):
        f.write(f"{datetime.utcnow().isoformat()} | Commit {i+1}\n")

print(f"Generated {commit_count} commits")
