
f1 = open("data.txt")
f2 = open("Copymydoc.txt","w")
for line in f1:
     if 'a' not in line:
          f2.write(line)
print('## File Copied Successfully! ##')
f1.close()
f2.close()
f2 = open("Copymydoc.txt","r")
print(f2.read())


