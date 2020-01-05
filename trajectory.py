import math
l1 = float(input('出発地の緯度'))
l2 = float(input('出発地の経度'))
co = float(input('コース'))
p = int(input('算出する経度間隔'))
v1 = math.degrees(math.acos(math.cos(math.radians(l1))*math.sin(math.radians(co))))
v2 = math.degrees(math.atan(1/(math.sin(math.radians(l1))*math.tan(math.radians(co)))))+l2
b = l2
q = int(360/p)
for i in range(q):
    b += p
    B = math.degrees(math.atan(math.tan(math.radians(v1)) * math.cos(math.radians(v2 - b))))
    unko = int(B)
    ooooo = abs((B - unko)*60)
    buri = int(b)
    uouo = int(abs((b - buri)*60))
    if(B < 0):
        l = "南緯{}°{}'".format(abs(unko),int(ooooo))
    else:
        l = "北緯{}°{}'".format(unko,int(ooooo))
    if(b < 0):
        L = "西経{}°{}'".format(abs(buri),uouo)
    elif(b >180):
        L = "西経{}°{}'".format(360-abs(buri),uouo)
    else:
        L = "東経{}°{}'".format(buri,uouo)
    print('{}, {}'.format(L,l))
