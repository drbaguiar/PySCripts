fname = raw_input('Enter file name: ')
if len(fname) < 1 : fname = "mbox-short.txt"
fhand = open(fname)
c = dict()
for line in fhand:
    if not line.startswith('From ') : continue
    pieces = line.split()
    time = pieces[5]
    parts = time.split(':')
    hour = parts[0]
    c[hour] = c.get(hour,0) + 1

lst = list()
for key in c:
  value = c[key]
  lst.append( (value, key) ) 


def getKey(item):
    return item[1]

lst.sort(key=getKey)

for value, key in lst:
  print key, value