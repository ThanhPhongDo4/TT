import random

random.seed()

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

key = random.randrange(256)

tukhoa=[]
for i in xrange(35):
    tukhoa.append(random.randrange(33,127))

tmp1 = [bin(i^key)[2:] for i in tukhoa]
tmp2 = ""
for i in xrange(len(tmp1)):
    tmp2 += "0"*(8 - len(tmp1[i])) + tmp1[i]

tmp3 = list(chunkstring(tmp2, 5))
tmp4 = []
for i in xrange(len(tmp3)):
    tmp3[i] = "001" + tmp3[i]
    tmp4.append(chr(int(tmp3[i],2)))
fi = open("noimangtoancau_template.html","r")
fo = open("noimangtoancau.html","w")
fo.write(fi.read())
fi.close()
i = 0
fo.write("<h3>Key = " + str(key)+ "</h3>")

fo.write('<table style="width:100%"><tr>')
for x in tmp4:
    fo.write('<th>' + x + '</th>')
    i+=1
    if i % 12 == 0:
        fo.write('</tr><tr>')

fo.write("</tr></table><br/><center><button id=\"show_answer\" onclick=\"show()\">Show Answer</button></center>")

last=""
for x in tukhoa:
    last += chr(x)
fo.write('<center><div id="myDIV" style="display:none"><h3><br/>' + last + '</h3></div></center>')
fo.close()

import webbrowser
webbrowser.open('noimangtoancau.html',new=2)

import winsound
winsound.PlaySound('noimangtoancau_music.mp3', winsound.SND_FILENAME)

