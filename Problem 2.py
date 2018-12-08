import json
import sys
d = json.load(sys.stdin)
final = []
for i in d["report"]:
    n = i["name"]
    e = i["enrollment"]
    for j in i["subject"]:
        if j["grade"]!="F":
            final.append(" ".join([j["code"],j["grade"],e,n]))
final = sorted(final)
for i in final:
    print(i)

