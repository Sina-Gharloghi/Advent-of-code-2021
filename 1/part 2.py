my_file = open("input.txt")
data = my_file.readlines()

for y in range(0, len(data)):
    data[y] = int(data[y])

depth = data
x = 1
y = []

for x in range(len(depth)-2):
    sum = depth[x] + depth[x+1] + depth[x+2]
    x = x+1
    y.append(sum)

i = 0
d = 0
n = 0
s = 1

for s in range(len(y)-1):
    if y[s] < y[s+1]:
        i = i+1

    elif y[s] == y[s+1]:
        n = n+1

    else:
        d = d+1
    s = s + 1

print("increase = ", i)