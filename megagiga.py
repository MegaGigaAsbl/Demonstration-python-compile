
import time

M_SIZE = 100

m1 = [[0] * M_SIZE for _ in range(M_SIZE)]
m2 = [[0] * M_SIZE for _ in range(M_SIZE)]
m3 = [[0] * M_SIZE for _ in range(M_SIZE)]

# ---------------------------------------------------------

start_time = time.time()

result1 = 0
for i in range(0,10):
    for j in range(1, 1001):
        result1 += j

end_time = time.time()
time1 = end_time - start_time

# ---------------------------------------------------------

start_time = time.time()

for i in range(0, M_SIZE):
    for j in range(0, M_SIZE):
        m1[i][j] = i+1 + j+1;
        m2[i][j] = i+1 + j+1;

for i in range(0, M_SIZE):
    for j in range(0, M_SIZE):
        m3[i][j] = 0
        for k in range(0, M_SIZE):
            m3[i][j] += m1[i][k] * m2[k][j]

result2 = 0
for i in range(0, M_SIZE):
    for j in range(0, M_SIZE):
        result2 += m3[i][j]

end_time = time.time()
time2 = end_time - start_time

# ---------------------------------------------------------

print(f'Python  : Result= {result1}, Time= {time1:10.6f} sec, ' + \
      f'Result= {result2}, Time= {time2:10.6f} sec')
