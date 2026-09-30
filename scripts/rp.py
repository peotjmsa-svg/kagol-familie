import sys,re
sys.stdout.reconfigure(encoding="utf-8")
for a in sys.argv[1:]:
    t=open(f"rec_{a}.txt",encoding="utf-8").read()
    i=t.find("Copy Citation"); e=t.find("Similar Records"); e = e if e>0 else t.find("Still Looking")
    title=t[t.find("Wiki\n")+5:].strip().split("\n")[0]
    body=[x.strip() for x in t[i+13:e].split("\n") if x.strip() and x.strip() not in ("OPEN ALL",)]
    body=[x for x in body if not x.startswith("View in Source Linker")]
    print("#####",a,title); print(" | ".join(body)[:1800])
