import re
import sys
pattern=sys.argv[1]
p = re.compile(pattern)
s = "abc1244xzyz"
print(re.search(p,s))
