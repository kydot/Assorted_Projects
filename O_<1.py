import time
n = int(input('-> '))
print(f'n = {n}')
start = time.time()
time.sleep(10/n)

print(f'finished. time taken = {time.time()-start}')
