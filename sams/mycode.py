import json
import pathlib
folder="/opt/homebrew"
fname="README"
l=list(pathlib.Path(folder).rglob(fname))

d={}
for i,e in enumerate(l):
    basename = pathlib.Path(e).stem
    p = pathlib.Path(e).parent
    d[str(p)]=fname
    # print( basename, p,  e)
    # print("***")
    if i > 3: break

dict={}
key="logs_to_process"
arr=[]
arr.append(d)
dict[key] = arr

json_object = json.dumps(dict, indent = 4)
print(json_object)
