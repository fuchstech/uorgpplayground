length = int(input())
string = str(input())
m,e,t,u = [],[],[],[]
sayac = []
for char in range(0,length):
    if string[char] == "M":
        m.append(char)
    if string[char] == "E":
        e.append(char)
    if string[char] == "T":
            t.append(char)
    if string[char] == "U":
            u.append(char)

for i in range(0,len(m)):
    mchar = m[i]
    for j in range(0,len(e)):
        echar = e[j]
        for k in range(0,len(t)):
            tchar = t[k]
            for l in range(0,len(u)):
                uchar = u[l]
                if mchar < echar < tchar < uchar:
                    sayac.append([mchar,echar,tchar,uchar])
print(len(sayac))