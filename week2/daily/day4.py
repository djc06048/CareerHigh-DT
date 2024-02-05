import numpy as np
import time
start_time=time.time()
def avg():
    num_days = 1000
    num_worms = 100000
    worms_weight = np.full(num_worms,0.0)
    worms = np.full(num_worms, 100.0)

    for day in range(1, num_days + 1):
        worms += np.random.normal(0.0, 1.0, num_worms)
        worms_weight[worms>=120] += 1.0
    avg_worm_weight = np.mean(worms_weight, dtype=np.float32)
    return avg_worm_weight

print(avg())
print(time.time()-start_time)
### 정답 np.cumsum
import numpy as np
x0=100
numofbugs=100000
numofdays=1000
start_time=time.time()
movement=np.random.randn(numofbugs,numofdays)
location=np.cumsum(movement,axis=1)+x0
feeding_table=np.where(location>120,1,0)
weights=feeding_table.sum(axis=1)

print(weights.mean())
print(time.time()-start_time)
