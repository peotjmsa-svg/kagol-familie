import sys,re
sys.stdout.reconfigure(encoding="utf-8")
# usage: fsz.py base   (base.txt + base.links) -> blocks with ark id
base=sys.argv[1]; pat=sys.argv[2] if len(sys.argv)>2 else "."
t=open(base+".txt",encoding="utf-8").read(); t=t[t.find("Links\n")+6:]
blocks=[" | ".join(x.strip() for x in b.strip().split("\n") if x.strip()) for b in t.split("\nMore\n")]
blocks=[b for b in blocks if b.count("|")>=2 and "Results per page" not in b]
ids=[]
for l in open(base+".links",encoding="utf-8").read().split("\n"):
    m=re.search(r"ark:/61903/1:1:([A-Z0-9-]+)\?",l)
    if m and "linker" not in l and m.group(1) not in ids: ids.append(m.group(1))
for i,b in enumerate(blocks):
    if re.search(pat,b): print(ids[i] if i<len(ids) else "?", "|", b[:300])
