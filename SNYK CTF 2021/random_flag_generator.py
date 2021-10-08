import random
import time
import hashlib

with open('log.txt', 'r') as f:
    bad_value = f.read().strip().splitlines()

n = len(bad_value)
current_seed = round(time.time()) # 1624176198

for seed in range(current_seed, 1, -1):
    print(seed)
    random.seed(seed, version=2)
    
    for i in range(n + 1):
        rnd = random.random()

        hash = hashlib.sha256(str(rnd).encode()).hexdigest()
        flag = f"SNYK{{{hash}}}"

        if "5bc" in hash:
            if i == n:
                print(flag)
                exit(0)
            else:
                break
        elif i < n:
            if rnd != float(bad_value[i]):
                break

# SNYK{53811586115bc8d9aed9fe1a84e9f2caeb71dea19fd63f68bad2a1a1d7196d46}