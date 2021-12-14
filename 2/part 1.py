my_file = open("input2.txt")
data = my_file.readlines()

f = []
u = []
d = []

for x in data:
    if "forward" in x:
        f.append(x)
    elif "down" in x:
        d.append(x)
    elif "up" in x:
        u.append(x)

fn = [x.replace('forward ', '')for x in f]
dn = [x.replace('down ', '') for x in d]
un = [x.replace('up ', '') for x in u]

for y in range(0, len(fn)):
    fn[y] = int(fn[y])


for y in range(0, len(dn)):
    dn[y] = int(dn[y])

for y in range(0, len(un)):
    un[y] = int(un[y])

forward = sum(fn)
up = sum(dn)
down = sum(un)

depth = up - down

final = depth * forward

print(final)
