#方法0.5---
lst1 = [1, 3, 7, 9, 12]
lst2 = [4, 8, 9, 13, 15, 19]
def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1
    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
    return c

print(merge(lst1, lst2))


#方法一：
lst1 = [1, 3, 7, 9, 12]
lst2 = [4, 8, 9, 13, 15, 19]
lst3 = []
def fun():
    return 1 if len(lst1) > len(lst2) else 0
while lst1 and lst2:
    if lst1[0] < lst2[0]:
        lst3.append(lst1[0])
        lst1.remove(lst1[0])
    else:
        lst3.append(lst2[0])
        lst2.remove(lst2[0])
if fun() == 1:
    lst3.extend(lst1)
else:
    lst3.extend(lst2)
print(lst3)




#方法二

lst1 = [1, 3, 7, 9, 12]
lst2 = [4, 8, 9, 13]
lst3 = []
lst3 = lst1 + lst2
print(lst3)
lst3.sort()
print(lst3)
