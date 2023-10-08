import random
alphalist = []
for i in range(26):
    alphalist.append(i)

random.shuffle(alphalist)
print(alphalist)

dict ={
    0:12,
    1:16,
    2:23,
    3:0,
    4:4,
    5:14,
    6:17,
    7:22,
    8:25,
    9:10,
    10:24,
    11:1,
    12:7,
    13:9,
    14:11,
    15:19,
    16:5,
    17:15,
    18:8,
    19:13,
    20:18,
    21:20,
    22:2,
    23:3,
    24:6,
    25:21

}

testlist = []
for i in range(26):
    testlist.append(dict.get(i))


print(dict.values())
print(testlist)
testlist.sort()
print(testlist)


