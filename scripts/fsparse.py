import sys
sys.stdout.reconfigure(encoding="utf-8")
t=open(sys.argv[1],encoding="utf-8").read()
i=t.find("Links\n"); t=t[i+6:]
for blk in t.split("\nMore\n"):
    l=[x.strip() for x in blk.strip().split("\n") if x.strip()]
    if len(l)>2: print(" | ".join(l)[:400])
