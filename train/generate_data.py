import pandas as pd
import random
ph = [4.5, 5.5]
ec = [0.1, 0.2]
oc = [2, 4]
n = [8, 14]
p = [85, 105]
k = [13, 18]
s = [10, 15]
z = [0.6, 0.8]
b = [0.5, 0.7]
fe = [2, 3.5]
mn = [1, 1.8]
cu =  [0.1, 0.2]
l=[]
for i in range(200):
    temp = [round(random.uniform(ph[0],ph[1]),2),round(random.uniform(ec[0],ec[1]),2),round(random.uniform(oc[0],oc[1]),2),random.randrange(n[0],n[1]),random.randrange(p[0],p[1]),random.randrange(k[0],k[1])]
    temp += [round(random.uniform(s[0],s[1]),2),round(random.uniform(z[0],z[1]),2),round(random.uniform(b[0],b[1]),2),round(random.uniform(fe[0],fe[1]),2),round(random.uniform(mn[0],mn[1]),2),round(random.uniform(cu[0],cu[1]),2)]
    temp.append("Tea")
    l.append(temp)

ph = [6, 7]
ec = [0.2, 0.4]
oc = [3, 4]
n = [60, 80]
p = [30, 40]
k = [20, 25]
s = [15, 20]
z = [0.8, 1.0]
b = [0.75, 0.95]
fe = [4, 6]
mn = [2, 3.5]
cu =  [0.25, 0.35]
for i in range(200):
    temp = [round(random.uniform(ph[0],ph[1]),2),round(random.uniform(ec[0],ec[1]),2),round(random.uniform(oc[0],oc[1]),2),random.randrange(n[0],n[1]),random.randrange(p[0],p[1]),random.randrange(k[0],k[1])]
    temp += [round(random.uniform(s[0],s[1]),2),round(random.uniform(z[0],z[1]),2),round(random.uniform(b[0],b[1]),2),round(random.uniform(fe[0],fe[1]),2),round(random.uniform(mn[0],mn[1]),2),round(random.uniform(cu[0],cu[1]),2)]
    temp.append("Wheat")
    l.append(temp)

ph = [6, 7]
ec = [0.8, 1.0]
oc = [4, 6]
n = [100, 150]
p = [50, 60]
k = [40, 50]
s = [18, 24]
z = [0.9, 0.2]
b = [0.8, 1.1]
fe = [5, 8]
mn = [2.5, 6]
cu =  [0.2, 0.55]
for i in range(200):
    temp = [round(random.uniform(ph[0],ph[1]),2),round(random.uniform(ec[0],ec[1]),2),round(random.uniform(oc[0],oc[1]),2),random.randrange(n[0],n[1]),random.randrange(p[0],p[1]),random.randrange(k[0],k[1])]
    temp += [round(random.uniform(s[0],s[1]),2),round(random.uniform(z[0],z[1]),2),round(random.uniform(b[0],b[1]),2),round(random.uniform(fe[0],fe[1]),2),round(random.uniform(mn[0],mn[1]),2),round(random.uniform(cu[0],cu[1]),2)]
    temp.append("Rice")
    l.append(temp)


ph = [5.5, 8.0]
ec = [0.6, 0.7]
oc = [5, 6]
n = [60, 65]
p = [30, 50]
k = [45, 60]
s = [30, 45]
z = [0.5, 0.7]
b = [0.45, 0.65]
fe = [4.5, 6.5]
mn = [3.5, 5.5]
cu =  [0.35, 0.45]
for i in range(200):
    temp = [round(random.uniform(ph[0],ph[1]),2),round(random.uniform(ec[0],ec[1]),2),round(random.uniform(oc[0],oc[1]),2),random.randrange(n[0],n[1]),random.randrange(p[0],p[1]),random.randrange(k[0],k[1])]
    temp += [round(random.uniform(s[0],s[1]),2),round(random.uniform(z[0],z[1]),2),round(random.uniform(b[0],b[1]),2),round(random.uniform(fe[0],fe[1]),2),round(random.uniform(mn[0],mn[1]),2),round(random.uniform(cu[0],cu[1]),2)]
    temp.append("Jowar")
    l.append(temp)


ph = [6.5, 7.5]
ec = [0.35, 0.50]
oc = [1, 2]
n = [25, 30]
p = [50, 75]
k = [25, 40]
s = [8, 11]
z = [0.5, 0.6]
b = [0.55, 0.65]
fe = [1.5, 2.5]
mn = [0.8, 1.5]
cu =  [0.05, 0.15]
for i in range(200):
    temp = [round(random.uniform(ph[0],ph[1]),2),round(random.uniform(ec[0],ec[1]),2),round(random.uniform(oc[0],oc[1]),2),random.randrange(n[0],n[1]),random.randrange(p[0],p[1]),random.randrange(k[0],k[1])]
    temp += [round(random.uniform(s[0],s[1]),2),round(random.uniform(z[0],z[1]),2),round(random.uniform(b[0],b[1]),2),round(random.uniform(fe[0],fe[1]),2),round(random.uniform(mn[0],mn[1]),2),round(random.uniform(cu[0],cu[1]),2)]
    temp.append("Toor")
    l.append(temp)


ph = [6, 7.5]
ec = [0.6, 0.8]
oc = [1, 2]
n = [40, 60]
p = [80, 120]
k = [65, 80]
s = [15, 25]
z = [0.6, 0.8]
b = [0.5, 0.6]
fe = [2.5, 3]
mn = [1.1, 1.8]
cu =  [0.08, 0.16]
for i in range(200):
    temp = [round(random.uniform(ph[0],ph[1]),2),round(random.uniform(ec[0],ec[1]),2),round(random.uniform(oc[0],oc[1]),2),random.randrange(n[0],n[1]),random.randrange(p[0],p[1]),random.randrange(k[0],k[1])]
    temp += [round(random.uniform(s[0],s[1]),2),round(random.uniform(z[0],z[1]),2),round(random.uniform(b[0],b[1]),2),round(random.uniform(fe[0],fe[1]),2),round(random.uniform(mn[0],mn[1]),2),round(random.uniform(cu[0],cu[1]),2)]
    temp.append("Soyabean")
    l.append(temp)


ph = [6.5, 8]
ec = [0.2, 0.3]
oc = [1.5, 3]
n = [45, 65]
p = [40, 60]
k = [60, 100]
s = [20, 35]
z = [0.7, 0.9]
b = [0.55, 0.8]
fe = [3.5, 5.5]
mn = [1.5, 2.9]
cu =  [0.08, 0.15]
for i in range(200):
    temp = [round(random.uniform(ph[0],ph[1]),2),round(random.uniform(ec[0],ec[1]),2),round(random.uniform(oc[0],oc[1]),2),random.randrange(n[0],n[1]),random.randrange(p[0],p[1]),random.randrange(k[0],k[1])]
    temp += [round(random.uniform(s[0],s[1]),2),round(random.uniform(z[0],z[1]),2),round(random.uniform(b[0],b[1]),2),round(random.uniform(fe[0],fe[1]),2),round(random.uniform(mn[0],mn[1]),2),round(random.uniform(cu[0],cu[1]),2)]
    temp.append("Onion")
    l.append(temp)


ph = [6, 7]
ec = [0.75, 0.95]
oc = [4, 6]
n = [100, 125]
p = [45, 65]
k = [60, 80]
s = [25, 35]
z = [1.0, 1.4]
b = [0.8, 1]
fe = [5, 7]
mn = [2.4, 3.8]
cu =  [0.25, 0.40]
for i in range(200):
    temp = [round(random.uniform(ph[0],ph[1]),2),round(random.uniform(ec[0],ec[1]),2),round(random.uniform(oc[0],oc[1]),2),random.randrange(n[0],n[1]),random.randrange(p[0],p[1]),random.randrange(k[0],k[1])]
    temp += [round(random.uniform(s[0],s[1]),2),round(random.uniform(z[0],z[1]),2),round(random.uniform(b[0],b[1]),2),round(random.uniform(fe[0],fe[1]),2),round(random.uniform(mn[0],mn[1]),2),round(random.uniform(cu[0],cu[1]),2)]
    temp.append("Cotton")
    l.append(temp)


ph = [6, 6.5]
ec = [0.55, 0.75]
oc = [2.5, 4.0]
n = [40, 60]
p = [40, 60]
k = [60, 80]
s = [10, 20]
z = [0.8, 1]
b = [0.6, 0.9]
fe = [3, 4.5]
mn = [1.4, 2.2]
cu =  [0.07, 0.15]
for i in range(200):
    temp = [round(random.uniform(ph[0],ph[1]),2),round(random.uniform(ec[0],ec[1]),2),round(random.uniform(oc[0],oc[1]),2),random.randrange(n[0],n[1]),random.randrange(p[0],p[1]),random.randrange(k[0],k[1])]
    temp += [round(random.uniform(s[0],s[1]),2),round(random.uniform(z[0],z[1]),2),round(random.uniform(b[0],b[1]),2),round(random.uniform(fe[0],fe[1]),2),round(random.uniform(mn[0],mn[1]),2),round(random.uniform(cu[0],cu[1]),2)]
    temp.append("Cabbage")
    l.append(temp)

df = pd.DataFrame(l, columns=['ph','ec','oc','n','p','k','s','z','b','fe','mn','cu','name'])
df.to_csv("data_test.csv", index=False)
