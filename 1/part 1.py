my_file = open("input.txt")
data = my_file.readlines()

for y in range(0, len(data)):
    data[y] = int(data[y])

depth = data

i = 0
d = 0
n = 0
x = 1

for x in range(len(depth)-1):
    if depth[x] < depth[x+1]:
        i = i+1

    elif depth[x] == depth[x+1]:
        n = n+1

    else:
        d = d+1
    x = x + 1

print("increase = ", i)
