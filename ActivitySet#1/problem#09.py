# Lists

filename = "dataset/romeo.txt"

fname = input("Enter the file name:")
fh = open(fname)
r = fh.read()
sp = r.split()
lst = list()
for w in sp:
    if w not in lst:
        lst.append(w)
lst.sort()
print(lst)