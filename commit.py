import random
from datetime import datetime

# File to modify
FILE = "activity.log"

# Random number of commits per day
commit_count = random.randint(1, 7)

with open(FILE, "a") as f:
    for i in range(commit_count):
        f.write(f"{datetime.utcnow().isoformat()} | Commit {i+1}\n")

print(f"Generated {commit_count} commits")
