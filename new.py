import time 

msg = "HELLO DUDE..."

for i in msg[:9]:
    print(i,end="",flush = True)
    time.sleep(0.1)

for i in msg[9:]:
    print(i,end='',flush=True)
    time.sleep(1)

