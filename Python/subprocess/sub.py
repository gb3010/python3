from subprocess import Popen,PIPE
p = Popen(['df','-h'],stdout=PIPE)
# p = subprocess.Popen(["df","-h"],stdout=PIPE)
for i in p.stdout:
    print(i.decode(),end='')
