import random
random.seed()
f = open('giaimatukhoa_data.txt','r')
fo = open('giaimatukhoa.html','w')
template = open('giaimatukhoa_template.html','r')
s = f.read().splitlines()
tmp = template.read().split('$$$')
fo.write(tmp[0])
template.close()

import heapq
h = []
prio = []
rev_prio = [0 for x in range(len(s))]
try:
    minprior = len(s) * 2
    fi = open("tanso.txt", "r")
    for i in range(len(s)):
        prio += [int(fi.readline())]
        minprior = min(minprior, prio[-1])
    if (minprior >= len(s)):
        prio = range(len(s))
        random.shuffle(prio)
    fi.close()
except IOError:
    print "Run here"
    prio = range(len(s))
    random.shuffle(prio)

for i in range(len(s)):
    rev_prio[prio[i] % len(s)] = i
    heapq.heappush(h, (prio[i], s[i]))

tk = []
for i in range(0,10):
    v = heapq.heappop(h)
    tk += [v[1]]
    heapq.heappush(h, (v[0]+len(s), v[1]))
    prio[rev_prio[v[0] % len(s)]] = v[0]+len(s)
fo.write(str(tk))
fo.write(tmp[1])
fo.close()

ftanso = open("tanso.txt", "w")
for i in range(len(s)):
    ftanso.write(str(prio[i])+"\n")
ftanso.close()

import webbrowser
webbrowser.open('giaimatukhoa.html',new=2)
