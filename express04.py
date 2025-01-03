import random
tp = 10000000
cp = 0
for a in range(tp):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    distance = (x*x + y*y)**0.5
    if distance <= 1:
        cp += 1
result = 4 * cp / tp
print(f'파이의 값은 {result}입니다.')
          