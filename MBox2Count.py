fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
counts = dict()
for line in fh:
    if not line.startswith("From:") : continue
    names = line.split()
    for name in names:
        if name == "From:" : continue  ## Do not count the From 
        counts[name] = counts.get(name,0) + 1   
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print bigword, bigcount