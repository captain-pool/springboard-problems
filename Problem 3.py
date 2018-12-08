# Enter your code here. Read input from STDIN. Print output to STDOUT
import hashlib
import sys
import datetime
salt = str(datetime.datetime.now())
u = sys.stdin.readlines()
for i in u:
    s = i.lower()
    if i[-1]=="\n":
        s = i[:-1].lower()
        hash_id = hashlib.md5((salt+s).encode()).hexdigest()[:6].upper()
        print("http://sprng.brd/"+hash_id)

