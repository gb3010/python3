from subprocess import Popen,PIPE
import random
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

p = Popen(['openssl','rand','base64',len],stdin=PIPE,stdout=PIPE)

for i in range(5):
    p.stdin.write(random.choice(l).encode())
    

p.stdin.close()

for j in p.stdout:
    print(j.decode(),end='')
