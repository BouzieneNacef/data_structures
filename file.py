# open file
f = open('TD.txt', 'a')
# write in the file
f.write("\n ahla chabeb")
# close the file
f.close

f = open('TD.txt', 'r')
# read one line 
print(f.readline)
# read file
print(f.read())

r = open('file.txt', 'x')
r.write(' the first file')
print(r.readline())