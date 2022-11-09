start = input()
end = input()

dist_h = abs(ord(start[0])-ord(end[0]))
dist_v = abs(int(start[1])-int(end[1]))

if dist_h > dist_v:
    print(dist_h)
else:
    print(dist_v)

